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

"""Tests to assure the API endpoints for managing a project technical requirements is working as expected."""
import json
from http import HTTPStatus

from ..api import API_URI_PREFIX
from ..helper.auth import ss_client_auth_header
from ..helper.request_data import factory_project_technical_req
from .test_project import create_project
from .test_user import create_user


def test_post_technical_req(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    response = _create_technical_req_(client, jwt)

    assert response.status_code == HTTPStatus.CREATED


def test_get_technical_req(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    headers = ss_client_auth_header(jwt)
    technical_req = create_technical_req(client, jwt)

    response = client.get(API_URI_PREFIX + 'technical-req/' + str(technical_req['id']),
                          headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK
    data = json.loads(response.data)
    assert data['id'] == technical_req['id']


def create_technical_req(client, jwt):
    """Create technical requirement and return technical_req object."""
    response = _create_technical_req_(client, jwt)
    technical_req = json.loads(response.data)
    return technical_req


def _create_technical_req_(client, jwt):
    """Create technical requirement and return response object."""
    headers = ss_client_auth_header(jwt)
    create_user(client, jwt)
    project = create_project(client, jwt)
    request_data = factory_project_technical_req()
    request_data['projectId'] = project['id']

    response = client.post(API_URI_PREFIX + 'technical-req',
                           data=json.dumps(request_data),
                           headers=headers, content_type='application/json')
    return response
