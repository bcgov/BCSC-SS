# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""BCSC Profile for OIDC Dynamic Client Registration.

The BCSC Profile for OIDC Dynamic Client Registration
describes the required fields, assumptions and constraints for
creating, updating, deleting and viewing a client configuration.
"""

import copy
import json

import requests

from ...utils.logging import log_error, log_info
from .models.dynamic_client_create import CreateRequestModel, CreateResponseModel
from .models.dynamic_client_get import GetResponseModel
from .models.dynamic_client_update import UpdateRequestModel, UpdateResponseModel


class DynamicClientRegistrationService():
    """Service to manage OIDC Dynamic Client Registration."""

    @staticmethod
    def create(request: CreateRequestModel):
        """Client Registration Request for a new client at the BCSC OpenID Provider."""
        url = request.api_url + '/oauth2/register'
        headers = DynamicClientRegistrationService._get_header_(request.api_token)

        del request.api_url
        del request.api_token

        request_json_data = json.dumps(request.__dict__)

        log_info('Create: ' + url + ', request_data: ' + request_json_data)

        response = requests.post(url, headers=headers, data=request_json_data)
        data = None
        if response.ok:
            data = CreateResponseModel(response.json())
            log_info(DynamicClientRegistrationService._get_sanitized_data_(data))
        else:
            log_error('ERROR:Create - status_code: ' + response.status_code + ', ' + response.text)
        return data

    @staticmethod
    def get(client_id: str, registration_access_token: str, api_url: str):
        """Get Registration Request for an existing client at the BCSC OpenID Provider."""
        url = api_url + '/oauth2/register/' + client_id
        headers = DynamicClientRegistrationService._get_header_(registration_access_token)

        log_info('Get: ' + url)

        response = requests.get(url, headers=headers)
        data = None
        if response.ok:
            data = GetResponseModel(response.json())
            log_info(DynamicClientRegistrationService._get_sanitized_data_(data))
        else:
            log_error('ERROR:Get - status_code: ' + response.status_code + ', ' + response.text)

        return data

    @staticmethod
    def update(registration_access_token: str, request: UpdateRequestModel):
        """Update Registration Request for an existing client at the BCSC OpenID Provider."""
        url = request.api_url + '/oauth2/register/' + request.client_id
        headers = DynamicClientRegistrationService._get_header_(registration_access_token)

        del request.api_url
        del request.api_token

        request_json_data = json.dumps(request.__dict__)
        log_info('Update: ' + url + ', request_data: ' + request_json_data)

        response = requests.put(url, headers=headers, data=request_json_data)
        data = None
        if response.ok:
            data = UpdateResponseModel(response.json())
            log_info(DynamicClientRegistrationService._get_sanitized_data_(data))
        else:
            log_error('ERROR:Update - status_code: ' + response.status_code + ', ' + response.text)

        return data

    @staticmethod
    def delete(client_id: str, registration_access_token: str, api_url: str):
        """Delete Registration Request for a new client at the BCSC OpenID Provider."""
        url = api_url + '/oauth2/register/' + client_id
        headers = DynamicClientRegistrationService._get_header_(registration_access_token)

        log_info('Delete: ' + url)

        response = requests.delete(url, headers=headers)
        return response.ok

    @staticmethod
    def _get_header_(token):
        """Generate header."""
        return {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }

    @staticmethod
    def _get_sanitized_data_(data):
        """Remove sensitive data before logging."""
        dc_data = copy.deepcopy(data)
        dc_data.client_secret = None
        dc_data.registration_access_token = None
