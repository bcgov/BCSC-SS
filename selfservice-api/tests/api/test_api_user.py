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

from http import HTTPStatus

from ..helper.api_create_data import USER_API, _create_user_, _get_user_
from ..helper.auth import ss_admin_auth_header, ss_client_auth_header


def test_post_user(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    response = _create_user_(client, jwt)
    assert response.status_code == HTTPStatus.CREATED


def test_post_user_validation(client, jwt, session):
    """Assert that the endpoint returns the bad request."""
    response = _create_user_(client, jwt, invalid_data=True)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_get_user(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    response = _get_user_(client, jwt)

    assert response.status_code == HTTPStatus.OK


def test_get_user_email(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    headers = ss_client_auth_header(jwt)

    response = client.get(USER_API,
                          headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK


def test_get_user_admin(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    headers = ss_admin_auth_header(jwt)

    response = client.get(USER_API,
                          headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK
