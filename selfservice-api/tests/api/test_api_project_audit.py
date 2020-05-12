# Copyright © 2020 Province of British Columbia
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
"""Tests API endpoints for project audit."""

from http import HTTPStatus

from ..helper.api_create_data import _get_project_audit_


def test_project_audit(client, jwt, session):
    """Assert that the endpoint returns the success status for project audit."""
    response = _get_project_audit_(client, jwt)
    assert response.status_code == HTTPStatus.OK
