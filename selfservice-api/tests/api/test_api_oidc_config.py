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
"""Tests API endpoints for oidc config."""

from http import HTTPStatus

from ..helper.api_create_data import _get_oidc_config_


def test_oidc_config(client, jwt, session):
    """Assert that the endpoint returns the success status for oidc config."""
    response = _get_oidc_config_(client, jwt)
    assert response.status_code == HTTPStatus.OK
