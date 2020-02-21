# Copyright © 2019 Province of British Columbia
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
"""API endpoints for managing an project resource."""

from http import HTTPStatus

from flask import g, jsonify, request
from flask_restplus import Namespace, Resource, cors
from marshmallow import ValidationError

from ..models import OIDCConfig, Project, TechnicalReq, User
from ..models.enums import ProjectRoles, ProjectStatus
from ..schemas.project import ProjectSchema
from ..services.external import DynamicClientRegistrationService
from ..services.external.models import CreateRequestModel, CreateResponseModel
from ..utils.auth import jwt
from ..utils.util import cors_preflight


API = Namespace('Project', description='Project')


@cors_preflight('GET,POST,OPTIONS')
@API.route('', methods=['GET', 'POST', 'OPTIONS'])
class ProjectResource(Resource):
    """Resource for managing create project."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def get():
        """Get all project."""
        oidc_token_info = g.jwt_oidc_token_info
        projects = Project.find_by_user(oidc_token_info.get('sub'))
        for info in projects:
            info['status'] = ProjectStatus(info['status']).name
            info['role'] = ProjectRoles(info['role']).name
        return jsonify({'projects': projects}), HTTPStatus.OK

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def post():
        """Post a new project using the request body."""
        project_json = request.get_json()

        try:
            token_info = g.jwt_oidc_token_info
            project_schema = ProjectSchema()
            dict_data = project_schema.load(project_json)
            project = Project.create_from_dict(dict_data, token_info.get('sub'))
            response, status = project_schema.dump(project), HTTPStatus.CREATED
        except ValidationError as project_err:
            response, status = {'message': str(project_err.messages)}, \
                HTTPStatus.BAD_REQUEST
        return response, status


@cors_preflight('GET,PUT,PATCH,OPTIONS')
@API.route('/<int:project_id>', methods=['GET', 'PUT', 'PATCH', 'OPTIONS'])
class ProjectResourceById(Resource):
    """Resource for managing get project by id."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def get(project_id):
        """Get project details."""
        token_info = g.jwt_oidc_token_info
        user = User.find_by_oauth_id(token_info.get('sub'))
        project = Project.find_by_id(project_id)
        project_dump = ProjectSchema().dump(project)
        for project_users in project.users:
            if project_users.user_id == user.id:
                project_dump['my_role'] = project_users.role
        return project_dump, HTTPStatus.OK

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def put(project_id):
        """Update project details."""
        project_json = request.get_json()

        try:
            project_schema = ProjectSchema()
            dict_data = project_schema.load(project_json)

            project = Project.find_by_id(project_id)
            token_info = g.jwt_oidc_token_info
            project.update(token_info.get('sub'), dict_data)
            response, status = 'Updated successfully', HTTPStatus.OK
        except ValidationError as project_err:
            response, status = {'message': str(project_err.messages)}, \
                HTTPStatus.BAD_REQUEST
        return response, status

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def patch(project_id):
        """Update project status."""
        project_patch_json = request.get_json()

        project = Project.find_by_id(project_id)
        token_info = g.jwt_oidc_token_info
        if 'update' in project_patch_json:
            if project_patch_json['update'] == 'status' and \
                    ProjectResourceById._validate_before_status_update_(project, project_patch_json.get('status')):

                project.update_status(token_info.get('sub'), project_patch_json['status'])
                ProjectResourceById._dynamic_api_call_(project)
                return 'Updated successfully', HTTPStatus.OK

        return 'Update failed', HTTPStatus.BAD_REQUEST

    @staticmethod
    def _validate_before_status_update_(project: Project, status):
        """Validate the project details before updating status."""
        if project is not None:
            if status == ProjectStatus.DevSubmitted:
                technical_req = TechnicalReq.find_by_project_id(project.id)
                if technical_req is not None and \
                    technical_req.scope_package_id is not None and \
                        technical_req.no_of_test_account is not None:
                    return True

        return False

    @staticmethod
    def _dynamic_api_call_(project: Project):
        """Generate OIDC config for this project."""
        oidc_config = OIDCConfig.find_by_project_id(project.id)
        if oidc_config is None:
            api_request = CreateRequestModel()
            api_request.client_name = project.project_name
            api_request.contacts = []
            for user_association in project.users:
                api_request.contacts.append(user_association.user.email)

            technical_req = project.technical_req[0]
            api_request.client_uri = technical_req.client_uri
            api_request.redirect_uris = technical_req.redirect_uris
            api_request.scope = technical_req.scope_package.scope
            api_request.jwks_uri = technical_req.jwks_uri
            api_request.id_token_signed_response_alg = technical_req.id_token_signed_response_alg
            api_request.userinfo_signed_response_alg = technical_req.userinfo_signed_response_alg
            api_request.token_endpoint_auth_method = None
            api_request.id_token_encrypted_response_alg = None
            api_request.id_token_encrypted_response_enc = None
            api_request.userinfo_encrypted_response_alg = None
            api_request.userinfo_encrypted_response_enc = None

            api_response: CreateResponseModel = DynamicClientRegistrationService.create(api_request)
            OIDCConfig.create_from_dict({
                'project_id': project.id,
                'client_id': api_response.client_id,
                'client_secret': api_response.client_secret,
                'registration_access_token': api_response.registration_access_token,
                'registration_client_uri': api_response.registration_client_uri,
                'client_id_issued_at': api_response.client_id_issued_at,
                'client_secret_expires_at': api_response.client_secret_expires_at,
                'token_endpoint_auth_method': api_response.token_endpoint_auth_method,
                'application_type': api_response.application_type,
                'subject_type': api_response.subject_type,
                'sector_identifier_uri': api_response.sector_identifier_uri,
                'id_token_encrypted_response_alg': api_response.id_token_encrypted_response_alg,
                'id_token_encrypted_response_enc': api_response.id_token_encrypted_response_enc,
                'userinfo_encrypted_response_alg': api_response.userinfo_encrypted_response_alg,
                'userinfo_encrypted_response_enc': api_response.userinfo_encrypted_response_enc
            })
