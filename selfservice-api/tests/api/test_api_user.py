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
"""Tests to assure the API endpoints for managing user is working as expected."""

import json
from http import HTTPStatus

from ..api import API_URI_PREFIX
from ..helper.auth import ss_client_auth_header


def test_post_user(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    response = _create_user_(client, jwt)

    assert response.status_code == HTTPStatus.CREATED


def test_get_user(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    headers = ss_client_auth_header(jwt)
    user = create_user(client, jwt)

    response = client.get(API_URI_PREFIX + 'user',
                          headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK
    data = json.loads(response.data)
    assert data['id'] == user['id']


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
    response = client.post(API_URI_PREFIX + 'user',
                           headers=headers, content_type='application/json')
    return response
