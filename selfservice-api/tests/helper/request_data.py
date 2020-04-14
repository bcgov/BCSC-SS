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
"""Data for testing."""

from . import camel2snake

from selfservice_api.models.enums.project import ProjectRoles, SigningEncryptionType


def factory_user_info(is_model=False):
    """JSON data to create user info."""
    user = {
        'email': 'developer@gov.bc.ca',
        'phone': '987654321',
        'firstName': 'client',
        'lastName': 'ss',
        'oauthId': '123456'
    }
    if is_model:
        return camel2snake(user)
    else:
        return user


def factory_project_info(is_model=False):
    """JSON data to create project info."""
    project = {
        'organizationName': 'organization',
        'projectName': 'project',
        'description': 'project which i am trying to create'
    }

    if is_model:
        return camel2snake(project)
    else:
        return project


def factory_project_team_member(is_model=False, member_role=ProjectRoles.Developer):
    """JSON data to create project info."""
    team_member = {}
    if member_role == ProjectRoles.Developer:
        team_member = {
            'email': 'developer@gov.bc.ca',
            'phone': '1234567890',
            'firstName': 'f developer',
            'lastName': 'l developer',
            'role': ProjectRoles.Developer
        }
    elif member_role == ProjectRoles.Manager:
        team_member = {
            'email': 'manager@gov.bc.ca',
            'phone': '1234567890',
            'firstName': 'f manager',
            'lastName': 'l manager',
            'role': ProjectRoles.Manager
        }
    elif member_role == ProjectRoles.Cto:
        team_member = {
            'email': 'cto@gov.bc.ca',
            'phone': '1234567890',
            'firstName': 'f cto',
            'lastName': 'l cto',
            'role': ProjectRoles.Cto
        }
    else:
        team_member = {
            'email': 'invalid@domain.com',
            'phone': '1234567890',
            'firstName': 'f invalid',
            'lastName': 'l invalid',
            'role': ProjectRoles.Developer
        }

    if is_model:
        return camel2snake(team_member)
    else:
        return team_member


def factory_project_technical_req(is_model=False, signing_encryption_type=SigningEncryptionType.SecureJWT):
    """JSON data to create technical req."""
    technical_req = {
        'projectId': 0,
        'clientUri': 'https://someone.com',
        'redirectUris': [
            'https://someone.com/*'
        ],
        'signingEncryptionType': signing_encryption_type,
        'jwksUri': 'https://someone.com/jwks',
        'signedResponseAlg': 'RS256',
        'encryptedResponseAlg': 'RS256'
    }
    if is_model:
        del technical_req['signedResponseAlg']
        del technical_req['encryptedResponseAlg']
        technical_req = camel2snake(technical_req)
        technical_req['id_token_signed_response_alg'] = 'RS256'
        technical_req['userinfo_signed_response_alg'] = 'RS256'
        technical_req['id_token_encrypted_response_alg'] = 'RS256'
        technical_req['userinfo_encrypted_response_alg'] = 'RS256'
        return technical_req
    else:
        return technical_req


def factory_project_oidc_config():
    """JSON data to create oidc config."""
    oidc_config = {
        'project_id': 0,
        'client_id': 'ee72e9abab',
        'client_secret': '6DjuDS_w7cbFfkotp1l0AumgjJ5Ng8j8lpUCezuC',
        'registration_access_token': '633537303539616631306330306235663',
        'registration_client_uri': 'https://idtest.gov.bc.ca/oauth2/register/ee72e9abab',
        'client_id_issued_at': '2020-02-13T15:52:52Z',
        'client_secret_expires_at': 658464,
        'token_endpoint_auth_method': 'client_secret_post',
        'application_type': 'web',
        'subject_type': 'pairwise',
        'sector_identifier_uri': 'urn:org:example:client',
        'id_token_encrypted_response_alg': 'RS256',
        'id_token_encrypted_response_enc': 'RS256',
        'userinfo_encrypted_response_alg': 'RS256',
        'userinfo_encrypted_response_enc': 'RS256'
    }
    return oidc_config


def factory_test_account():
    """JSON data to create TestAccount."""
    test_accounts = {
        'testAccounts': 'SS4BPS201,98901,ONE,SS4BPS Felecia,F,4732 Easy Street,,V9B 3V9,1998-04-30\n \
            SS4BPS202,,TWO,SS4BPS Benjamin ,M,308-2464 Crimson Vale,Penticton BC V2A 5N1,V2A 5N1,2000-11-18'
    }
    return test_accounts
