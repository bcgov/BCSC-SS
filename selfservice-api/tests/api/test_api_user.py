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

from ..helper.api_create_data import USER_API, _create_team_, _create_user_, _get_user_
from ..helper.auth import (invalid_email_auth_header, invalid_provider_auth_header,  # noqa: I001
                           new_idir_auth_header, ss_admin_auth_header, ss_client_auth_header)  # noqa: I001

from selfservice_api.models.enums import ProjectRoles


new_email = 'new@gov.bc.ca'


def test_post_user(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    response = _create_user_(client, jwt)
    assert response.status_code == HTTPStatus.CREATED


def test_post_user_validation(client, jwt, session):
    """Assert that the endpoint returns the bad request."""
    response = _create_user_(client, jwt, invalid_email=True)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    response = _create_user_(client, jwt, email_none=True)
    assert response.status_code == HTTPStatus.BAD_REQUEST

    response = _create_user_(client, jwt, invalid_phone=True)
    assert response.status_code == HTTPStatus.BAD_REQUEST

    headers = invalid_provider_auth_header(jwt)
    req_data = {
        'email': 'developer@gov.bc.ca',
        'phone': '5689732156'
    }
    response = client.post(USER_API, data=json.dumps(req_data),
                           headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.BAD_REQUEST

    _create_new_idir_user_(client, jwt, session)
    headers = new_idir_auth_header(jwt, sub='test-validation')
    req_data = {
        'email': new_email,
        'phone': '5689732156'
    }

    response = client.post(USER_API, data=json.dumps(req_data),
                           headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.BAD_REQUEST

    _create_user_(client, jwt)
    headers = ss_client_auth_header(jwt)
    req_data = {
        'email': new_email,
        'phone': '5689732156'
    }

    response = client.post(USER_API, data=json.dumps(req_data),
                           headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.BAD_REQUEST

    req_data = {
        'email': 'new2@gov.bc.ca',
        'phone': '5689732156'
    }

    response = client.post(USER_API, data=json.dumps(req_data),
                           headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.CREATED


def test_put_user(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    response = _create_user_(client, jwt)
    headers = ss_client_auth_header(jwt)

    response = client.put(USER_API,
                          headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK


def test_get_user(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    response = _get_user_(client, jwt)
    assert response.status_code == HTTPStatus.OK

    headers = new_idir_auth_header(jwt)
    response = client.get(USER_API,
                          headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.OK

    _create_team_(client, jwt, member_role=ProjectRoles.Cto, new_email=new_email)

    headers = new_idir_auth_header(jwt)
    response = client.get(USER_API,
                          headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.OK


def test_get_user_email(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    headers = ss_client_auth_header(jwt)

    response = client.get(USER_API,
                          headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK

    headers = invalid_email_auth_header(jwt)
    response = client.get(USER_API,
                          headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.OK


def test_get_user_admin(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    headers = ss_admin_auth_header(jwt)
    response = client.get(USER_API,
                          headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.OK


def _create_new_idir_user_(client, jwt, session, email=new_email, sub='65a62-6713-4e7d-8f12-99'):
    """Assert that the endpoint returns the success status."""
    headers = new_idir_auth_header(jwt, email=email, sub=sub)
    req_data = {
        'email': email,
        'phone': '5689732156'
    }

    response = client.post(USER_API, data=json.dumps(req_data),
                           headers=headers, content_type='application/json')
    return response
