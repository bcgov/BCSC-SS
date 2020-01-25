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
"""Tests to assure the API endpoints for managing a project info resource is working as expected."""

import json
from http import HTTPStatus

from ..api import API_URI_PREFIX
from ..helper.auth import ss_client_auth_header
from ..helper.request_data import factory_project_info
from .test_api_user import create_user

from selfservice_api.models.enums import ProjectRoles


PROJECTINFO_API = API_URI_PREFIX + 'project/info'


def test_post_project_as_developer(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    create_user(client, jwt, project_role='manager')

    response = _create_project_(client, jwt, ProjectRoles.Developer)

    assert response.status_code == HTTPStatus.CREATED


def test_post_project_as_manager(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    create_user(client, jwt, project_role='cto')
    response = _create_project_(client, jwt, ProjectRoles.Manager)

    assert response.status_code == HTTPStatus.CREATED


def test_post_project_as_cto(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    create_user(client, jwt, project_role='developer')
    response = _create_project_(client, jwt, ProjectRoles.Cto)

    assert response.status_code == HTTPStatus.CREATED


def test_post_project_validation(client, jwt, session):
    """Assert that the endpoint returns the failure status."""
    headers = ss_client_auth_header(jwt)
    req_data = {}

    response = client.post(PROJECTINFO_API, data=json.dumps(req_data),
                           headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_get_project(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    headers = ss_client_auth_header(jwt)
    project = create_project(client, jwt)

    response = client.get(PROJECTINFO_API + '/' + str(project['id']),
                          headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK
    data = json.loads(response.data)
    assert data['id'] == project['id']


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
