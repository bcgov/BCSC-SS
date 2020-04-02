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
"""Creating data before testing."""

import json

from .auth import TestJwtClaims, ss_admin_auth_header, ss_client_auth_header
from .request_data import factory_project_info, factory_project_technical_req, factory_test_account

from selfservice_api.models.enums import ProjectRoles, SigningEncryptionType


API_URI_PREFIX = '/api/v1/'
USER_API = API_URI_PREFIX + 'user'
PROJECTINFO_API = API_URI_PREFIX + 'project/info'
TEAM_API = API_URI_PREFIX + 'project/:project_id/team'
TECHNICALREQ_API = API_URI_PREFIX + 'project/:project_id/technical-req'
OIDCCONFIG_API = API_URI_PREFIX + 'project/:project_id/oidc-config'
SCOPEPACKAGE_API = API_URI_PREFIX + 'scope-package'
TESTACCOUNT_API = API_URI_PREFIX + 'test-account'

# User: Start


def create_user(client, jwt, project_role='developer'):
    """Create user and return user object.

    project_role allowed values: developer, manager, cto
    """
    response = _create_user_(client, jwt, project_role=project_role)
    user = json.loads(response.data)
    return user


def _create_user_(client, jwt, project_role='developer', invalid_email=False, email_none=False, invalid_phone=False):
    """Create user and return response object."""
    headers = ss_client_auth_header(jwt, project_role=project_role)
    claims = TestJwtClaims['ss_client_' + project_role]
    req_data = {
        'email': claims['email'],
        'phone': '5689732156'
    }
    if invalid_email:
        req_data['email'] = 'mail@email.com'
    if email_none:
        req_data['email'] = None
    if invalid_phone:
        req_data['phone'] = None

    response = client.post(USER_API, data=json.dumps(req_data),
                           headers=headers, content_type='application/json')
    return response


def _create_admin_user_(client, jwt):
    """Create admin user and return response object."""
    headers = ss_admin_auth_header(jwt)
    claims = TestJwtClaims['ss_admin']
    req_data = {
        'email': claims['email'],
        'phone': '5689732156'
    }

    response = client.post(USER_API, data=json.dumps(req_data),
                           headers=headers, content_type='application/json')
    return response


def get_user(client, jwt):
    """Get user and return user object."""
    response = _get_user_(client, jwt)
    user = json.loads(response.data)
    return user


def _get_user_(client, jwt):
    """Get user and return response object."""
    headers = ss_client_auth_header(jwt)
    create_user(client, jwt)

    response = client.get(USER_API,
                          headers=headers, content_type='application/json')

    return response

# User: End
# Project Info: Start


def create_project(client, jwt):
    """Create project and return project object."""
    response = _create_project_(client, jwt, ProjectRoles.Developer)
    project = json.loads(response.data)
    return project


def _create_project_(client, jwt, my_role):
    """Create project and return response object."""
    project_role = 'developer' if my_role == 1 else 'manager' if my_role == 2 else 'cto'
    headers = ss_client_auth_header(jwt, project_role=project_role)
    create_user(client, jwt, project_role=project_role)

    response = client.post(PROJECTINFO_API, data=json.dumps(factory_project_info()),
                           headers=headers, content_type='application/json')
    return response


def get_project(client, jwt):
    """Get project and return project object."""
    response = _get_project_(client, jwt)
    project = json.loads(response.data)
    return project


def _get_project_(client, jwt):
    """Get project and return response object."""
    headers = ss_client_auth_header(jwt)
    project = create_project(client, jwt)

    response = client.get(PROJECTINFO_API + '/' + str(project['id']),
                          headers=headers, content_type='application/json')

    return response


def _get_all_project_(client, jwt, is_analyst=False):
    """Get all projects and return response object."""
    headers = ss_admin_auth_header(jwt) if is_analyst else ss_client_auth_header(jwt)
    create_project(client, jwt)

    response = client.get(PROJECTINFO_API, headers=headers, content_type='application/json')

    return response

# Project Info: End
# Technical Req: Start


def create_technical_req_with_additional(client, jwt, include=['package', 'test-account']):
    """Create technical requirement with additional details and return technical_req object."""
    technical_req = create_technical_req(client, jwt)
    _update_technical_req_with_package_(client, jwt, str(technical_req['projectId']))
    _update_technical_req_with_test_account_(client, jwt, str(technical_req['projectId']))
    response = _get_technical_req_(client, jwt, str(technical_req['projectId']))
    technical_req = json.loads(response.data)
    return technical_req


def _update_technical_req_with_package_(client, jwt, project_id):
    """Update technical requirement with package and return response."""
    headers = ss_client_auth_header(jwt)
    scope_packages = get_scope_packages(client, jwt)
    req_data = {
        'update': 'package',
        'scopePackageId': scope_packages['scopePackages'][0]['id']
    }

    response = client.patch(TECHNICALREQ_API.replace(':project_id', project_id),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    return response


def _update_technical_req_with_test_account_(client, jwt, project_id, no_of_test_account=5):
    """Update technical requirement with test account and return response."""
    headers = ss_client_auth_header(jwt)
    req_data = {
        'update': 'test-account',
        'noOfTestAccount': no_of_test_account,
        'noteTestAccount': 'renmarks'
    }

    response = client.patch(TECHNICALREQ_API.replace(':project_id', project_id),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    return response


def create_technical_req(client, jwt):
    """Create technical requirement and return technical_req object."""
    response = _create_technical_req_(client, jwt)
    technical_req = json.loads(response.data)
    return technical_req


def _create_technical_req_(client, jwt, signing_encryption_type=SigningEncryptionType.SecureJWT):
    """Create technical requirement and return response object."""
    headers = ss_client_auth_header(jwt)
    project = create_project(client, jwt)
    request_data = factory_project_technical_req(signing_encryption_type=signing_encryption_type)
    request_data['projectId'] = project['id']

    response = client.post(TECHNICALREQ_API.replace(':project_id', str(project['id'])),
                           data=json.dumps(request_data),
                           headers=headers, content_type='application/json')
    return response


def _get_technical_req_(client, jwt, project_id):
    """Get technical requirement and return response."""
    headers = ss_client_auth_header(jwt)

    response = client.get(TECHNICALREQ_API.replace(':project_id', project_id),
                          headers=headers, content_type='application/json')

    return response

# Technical Req: End
# Scope Package: Start


def get_scope_packages(client, jwt):
    """Get scope package and return object."""
    response = _get_scope_packages_(client, jwt)
    return json.loads(response.data)


def _get_scope_packages_(client, jwt):
    """Get scope package and return response object."""
    headers = ss_client_auth_header(jwt)
    response = client.get(SCOPEPACKAGE_API, headers=headers)
    return response

# Scope Package: End
# OIDC Config: Start


def get_oidc_config(client, jwt):
    """Get oidc config and return object."""
    response = _get_oidc_config_(client, jwt)
    return json.loads(response.data)


def _get_oidc_config_(client, jwt):
    """Get oidc config and return response object."""
    headers = ss_client_auth_header(jwt)
    technical_req = create_technical_req(client, jwt)

    response = client.get(OIDCCONFIG_API.replace(':project_id', str(technical_req['projectId'])), headers=headers)
    return response

# OIDC Config: End
# Test Account: Start


def _create_test_account_(client, jwt):
    """Create test account and return response object."""
    _create_admin_user_(client, jwt)

    headers = ss_admin_auth_header(jwt)
    request_data = factory_test_account()

    response = client.post(TESTACCOUNT_API, data=json.dumps(request_data),
                           headers=headers, content_type='application/json')
    return response

# Test Account: End
