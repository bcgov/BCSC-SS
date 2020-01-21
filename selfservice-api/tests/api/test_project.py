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
from .test_user import create_user


def test_post_project(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    response = _create_project_(client, jwt)

    assert response.status_code == HTTPStatus.CREATED


def test_get_project(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    headers = ss_client_auth_header(jwt)
    project = create_project(client, jwt)

    response = client.get(API_URI_PREFIX + 'project/' + str(project['id']),
                          headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK
    data = json.loads(response.data)
    assert data['id'] == project['id']


def create_project(client, jwt):
    """Create project and return project object."""
    response = _create_project_(client, jwt)
    project = json.loads(response.data)
    return project


def _create_project_(client, jwt):
    """Create project and return response object."""
    headers = ss_client_auth_header(jwt)
    create_user(client, jwt)

    response = client.post(API_URI_PREFIX + 'project', data=json.dumps(factory_project_info()),
                           headers=headers, content_type='application/json')
    return response
