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
"""Tests API endpoints for test account."""

import json
from http import HTTPStatus

from ..helper.api_create_data import TESTACCOUNT_API, _create_admin_user_, _create_test_account_
from ..helper.auth import ss_admin_auth_header


def test_test_account_availability(client, jwt, session):
    """Assert that the endpoint returns the success status for test account."""
    headers = ss_admin_auth_header(jwt)

    response = client.get(TESTACCOUNT_API + '/availability',
                          headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.OK


def test_test_account(client, jwt, session):
    """Assert that the endpoint returns the success status for test account."""
    response = _create_test_account_(client, jwt)
    assert response.status_code == HTTPStatus.CREATED


def test_test_account_validation(client, jwt, session):
    """Assert that the endpoint returns the success status for test account."""
    _create_admin_user_(client, jwt)

    headers = ss_admin_auth_header(jwt)

    response = client.post(TESTACCOUNT_API, data=json.dumps({}),
                           headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.BAD_REQUEST
