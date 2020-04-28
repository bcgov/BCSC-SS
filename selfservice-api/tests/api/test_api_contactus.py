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
"""Tests API endpoints for exposing contactus."""

import json
from http import HTTPStatus

from ..api import API_URI_PREFIX


def test_contactus_request(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    req_data = {
        'firstName': 'my',
        'lastName': 'self',
        'email': 'my.self@mail.com',
        'description': 'i have some questions <script type="text/javascript">alert("abcd");</script>'
    }
    rv = client.post(API_URI_PREFIX + 'contactus', data=json.dumps(req_data), content_type='application/json')

    assert rv.status_code == HTTPStatus.OK


def test_contactus_invalid(client, jwt, session):
    """Assert that the endpoint returns the failure status."""
    req_data = {
        'firstName': 'my',
        'lastName': 'self',
        'email': '',
        'description': ''
    }
    rv = client.post(API_URI_PREFIX + 'contactus', data=json.dumps(req_data), content_type='application/json')

    assert rv.status_code == HTTPStatus.BAD_REQUEST
