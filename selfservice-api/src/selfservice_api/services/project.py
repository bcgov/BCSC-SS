# Copyright © 2020 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This manages Project Service."""

from flask import current_app

from ..models import OIDCConfig, Project, ProjectUsersAssociation, TechnicalReq, TestAccount
from ..models.enums import ProjectStatus
from .external import get_dynamic_api
from .external.models import CreateRequestModel, CreateResponseModel, UpdateRequestModel, UpdateResponseModel
from .notification import EmailService, EmailType


class ProjectService():
    """Service to manage Project actions."""

    @staticmethod
    def on_development_status(project: Project):
        """When the project status is moving to development from draft."""
        EmailService.save_and_send(EmailType.DEV_REQUEST, {'project_name': project.project_name})

        test_accounts = TestAccount.find_all_by_project_id(project.id)
        technical_req: TechnicalReq = project.technical_req[0]
        response = {
            'testAccountSuccess': True
        }
        if len(test_accounts) < technical_req.no_of_test_account:
            response['testAccountSuccess'] = False

        return response

    @staticmethod
    def validate_before_status_update(project: Project, project_json):
        """Validate the project details before updating status."""
        is_valid = False
        if 'update' in project_json and project_json['update'] == 'status':
            status = project_json.get('status')
            if status == ProjectStatus.Development:
                technical_req = TechnicalReq.find_by_project_id(project.id, False)
                project_members = ProjectUsersAssociation.find_all_by_project_id(project.id)
                if len(project_members) > 0 and \
                    technical_req is not None and \
                    technical_req.scope_package_id is not None and \
                        technical_req.no_of_test_account is not None:
                    is_valid = True
            elif status == ProjectStatus.DevelopmentComplete:
                is_valid = project.status == ProjectStatus.Development

        return is_valid

    @staticmethod
    def dynamic_api_delete(project: Project, including_prod: bool):
        """Delete OIDC config for this project."""
        dynamic_api = get_dynamic_api()

        # Delete test config by default
        oidc_config = OIDCConfig.find_by_project_id(project.id, False)
        if oidc_config:
            api_url = current_app.config.get('DYNAMIC_TEST_API_URL')
            dynamic_api.delete(oidc_config.client_id, oidc_config.registration_access_token, api_url)

        # Delete prod config as well if `including_prod` true
        if including_prod:
            oidc_config = OIDCConfig.find_by_project_id(project.id, True)
            if oidc_config:
                api_url = current_app.config.get('DYNAMIC_PROD_API_URL')
                dynamic_api.delete(oidc_config.client_id, oidc_config.registration_access_token, api_url)

    @staticmethod
    def dynamic_api_save(project: Project, is_prod: bool):
        """Generate OIDC config for this project."""
        api_call_succeeded = True
        dynamic_api = get_dynamic_api()

        oidc_config = OIDCConfig.find_by_project_id(project.id, is_prod)
        api_request = ProjectService.generate_api_request(project, is_prod, oidc_config)

        if oidc_config is None:
            api_response: CreateResponseModel = dynamic_api.create(api_request)

            if api_response is not None:
                dict_oidc = ProjectService.map_response_to_oidc_config(False, project, api_response)
                dict_oidc['is_prod'] = is_prod
                OIDCConfig.create_from_dict(dict_oidc)
            else:
                api_call_succeeded = False
        else:
            api_request.client_id = oidc_config.client_id
            api_response: UpdateResponseModel = \
                dynamic_api.update(oidc_config.registration_access_token, api_request)

            if api_response is not None:
                oidc_config.update(
                    ProjectService.map_response_to_oidc_config(True, project, api_response))
            else:
                api_call_succeeded = False

        if not is_prod and api_call_succeeded:
            technical_req: TechnicalReq = project.technical_req[0]
            TestAccount.map_test_accounts(project.id, technical_req.no_of_test_account)
            trigger_count = current_app.config.get('LIMITED_TEST_ACCOUNT_TRIGGER_COUNT')
            if TestAccount.get_availability_count() <= trigger_count:

                EmailService.save_and_send(EmailType.TEST_ACCOUNT, {})

        return api_call_succeeded

    @staticmethod
    def generate_api_request(project: Project, is_prod: bool, oidc_config: OIDCConfig):
        """Create dynaamic api request object."""
        if oidc_config is None:
            api_request = CreateRequestModel()
        else:
            api_request = UpdateRequestModel()

        api_request.client_name = project.project_name
        api_request.contacts = []
        for user_association in project.users:
            api_request.contacts.append(user_association.user.email)

        technical_req: TechnicalReq = project.technical_req[0]
        api_request.client_uri = technical_req.client_uri
        api_request.redirect_uris = technical_req.redirect_uris
        api_request.scope = technical_req.scope_package.scope
        api_request.jwks_uri = technical_req.jwks_uri
        api_request.id_token_signed_response_alg = technical_req.id_token_signed_response_alg
        api_request.userinfo_signed_response_alg = technical_req.userinfo_signed_response_alg
        api_request.token_endpoint_auth_method = ''
        api_request.id_token_encrypted_response_alg = technical_req.id_token_encrypted_response_alg
        api_request.id_token_encrypted_response_enc = technical_req.id_token_encrypted_response_enc
        api_request.userinfo_encrypted_response_alg = technical_req.userinfo_encrypted_response_alg
        api_request.userinfo_encrypted_response_enc = technical_req.userinfo_encrypted_response_enc

        if is_prod:
            api_request.api_url = current_app.config.get('DYNAMIC_PROD_API_URL')
            api_request.api_token = current_app.config.get('DYNAMIC_PROD_API_TOKEN')
        else:
            api_request.api_url = current_app.config.get('DYNAMIC_TEST_API_URL')
            api_request.api_token = current_app.config.get('DYNAMIC_TEST_API_TOKEN')

        return api_request

    @staticmethod
    def map_response_to_oidc_config(is_update: bool, project, api_response):
        """Map response to OIDC config."""
        data = {
            'project_id': project.id,
            'client_id': api_response.client_id,
            'client_secret': api_response.client_secret,
            'registration_access_token': api_response.registration_access_token,
            'registration_client_uri': api_response.registration_client_uri,
            'client_id_issued_at': api_response.client_id_issued_at,
            'client_secret_expires_at': api_response.client_secret_expires_at,
            'token_endpoint_auth_method': api_response.token_endpoint_auth_method
        }

        if not is_update:
            data['application_type'] = api_response.application_type
            data['subject_type'] = api_response.subject_type

        return data
