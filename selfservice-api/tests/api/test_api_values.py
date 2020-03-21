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
"""Tests API endpoints for exposing static list of values."""

from http import HTTPStatus

from ..api import API_URI_PREFIX
from ..helper.api_create_data import _create_user_
from ..helper.auth import ss_client_auth_header


def test_values_algorithms(client, jwt, session):
    """Assert that the endpoint returns the success status for algorithms."""
    _create_user_(client, jwt)
    headers = ss_client_auth_header(jwt)
    rv = client.get(API_URI_PREFIX + 'values/algorithms', headers=headers)

    assert rv.status_code == HTTPStatus.OK
