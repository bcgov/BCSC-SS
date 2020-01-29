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

from .auth import ss_client_auth_header
from .request_data import factory_project_info, factory_project_technical_req

from selfservice_api.models.enums import ProjectRoles


API_URI_PREFIX = '/api/v1/'
USER_API = API_URI_PREFIX + 'user'
PROJECTINFO_API = API_URI_PREFIX + 'project/info'
TECHNICALREQ_API = API_URI_PREFIX + 'project/:project_id/technical-req'
SCOPEPACKAGE_API = API_URI_PREFIX + 'scope-package'
# User: Start


def create_user(client, jwt, project_role='developer'):
    """Create user and return user object.

    project_role allowed values: developer, manager, cto
    """
    response = _create_user_(client, jwt, project_role=project_role)
    user = json.loads(response.data)
    return user


def _create_user_(client, jwt, project_role='developer'):
    """Create user and return response object."""
    headers = ss_client_auth_header(jwt, project_role=project_role)
    response = client.post(USER_API,
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

    response = client.post(PROJECTINFO_API, data=json.dumps(factory_project_info(my_role=my_role)),
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


def _update_technical_req_with_test_account_(client, jwt, project_id):
    """Update technical requirement with test account and return response."""
    headers = ss_client_auth_header(jwt)
    req_data = {
        'update': 'test-account',
        'noOfTestAccount': 5,
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


def _create_technical_req_(client, jwt):
    """Create technical requirement and return response object."""
    headers = ss_client_auth_header(jwt)
    project = create_project(client, jwt)
    request_data = factory_project_technical_req()
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
    """Get algorithms and return scope_package object."""
    response = _get_scope_packages_(client, jwt)
    return json.loads(response.data)


def _get_scope_packages_(client, jwt):
    """Get algorithms and return response object."""
    headers = ss_client_auth_header(jwt)
    response = client.get(SCOPEPACKAGE_API, headers=headers)
    return response


# Scope Package: End
