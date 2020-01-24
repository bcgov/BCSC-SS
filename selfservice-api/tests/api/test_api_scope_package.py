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
"""Tests API endpoints for scope package."""

import json
from http import HTTPStatus

from ..api import API_URI_PREFIX
from ..helper.auth import ss_client_auth_header


def test_scope_packages(client, jwt, session):
    """Assert that the endpoint returns the success status for scope packages."""
    response = _get_scope_packages_(client, jwt, session)
    assert response.status_code == HTTPStatus.OK


def get_scope_packages(client, jwt, session):
    """Get algorithms and return scope_package object."""
    response = _get_scope_packages_(client, jwt, session)
    return json.loads(response.data)


def _get_scope_packages_(client, jwt, session):
    """Get algorithms and return response object."""
    headers = ss_client_auth_header(jwt)
    response = client.get(API_URI_PREFIX + 'scope-package', headers=headers)
    return response
