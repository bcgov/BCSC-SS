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
"""***Temperory***: API mock for BCSC OIDC Dynamic Client Registration."""

import binascii
import json
import os
import secrets
from datetime import datetime

from flask import current_app

from .models.dynamic_client_create import CreateRequestModel, CreateResponseModel
from .models.dynamic_client_get import GetResponseModel
from .models.dynamic_client_update import UpdateRequestModel, UpdateResponseModel


class DynamicClientRegistrationApiMock():
    """Api mock to manage OIDC Dynamic Client Registration."""

    @staticmethod
    def create(request: CreateRequestModel):
        """Client Registration Request for a new client at the BCSC OpenID Provider."""
        if current_app.config.get('dynamic_api_return_none'):
            return None

        response = CreateResponseModel({})
        response.client_id = secrets.token_hex(5)
        response.client_secret = secrets.token_urlsafe(30)
        response.registration_access_token = binascii.hexlify(os.urandom(24))
        response.registration_client_uri = request.api_url + '/oauth2/register/' + response.client_id
        response.client_id_issued_at = json.dumps(datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'))
        response.client_secret_expires_at = '0'
        response.client_name = request.client_name
        response.client_uri = request.client_uri
        response.redirect_uris = request.redirect_uris
        response.jwks_uri = request.jwks_uri
        response.contacts = request.contacts
        response.token_endpoint_auth_method = request.token_endpoint_auth_method \
            if request.token_endpoint_auth_method is not None else 'client_secret_post'
        response.application_type = 'web'
        response.subject_type = 'pairwise'
        response.sector_identifier_uri = 'urn:org:example:client'
        response.id_token_signed_response_alg = request.id_token_signed_response_alg
        response.userinfo_signed_response_alg = request.userinfo_signed_response_alg
        response.id_token_encrypted_response_alg = request.id_token_encrypted_response_alg \
            if request.id_token_encrypted_response_alg is not None else 'RSA1_5'
        response.id_token_encrypted_response_enc = request.id_token_encrypted_response_enc \
            if request.id_token_encrypted_response_enc is not None else 'A256GCM'
        response.userinfo_encrypted_response_alg = request.userinfo_encrypted_response_alg \
            if request.userinfo_encrypted_response_alg is not None else 'RSA1_5'
        response.userinfo_encrypted_response_enc = request.userinfo_encrypted_response_enc \
            if request.userinfo_encrypted_response_enc is not None else 'A256GCM'

        return response

    @staticmethod
    def get(client_id: str, registration_access_token: str, api_url: str):
        """Get Registration Request for an existing client at the BCSC OpenID Provider."""
        if current_app.config.get('dynamic_api_return_none'):
            return None

        response = GetResponseModel({})
        response.client_id = client_id
        response.client_secret = secrets.token_urlsafe(30)
        response.registration_access_token = registration_access_token
        response.registration_client_uri = api_url + '/oauth2/register/' + response.client_id
        response.client_id_issued_at = json.dumps(datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'))
        response.client_secret_expires_at = '0'
        response.client_name = 'client 1'
        response.client_uri = 'client uri 1'
        response.redirect_uris = []
        response.jwks_uri = 'jwks uri 1'
        response.contacts = []
        response.token_endpoint_auth_method = 'client_secret_post'
        response.application_type = 'web'
        response.subject_type = 'pairwise'
        response.sector_identifier_uri = 'urn:org:example:client'
        response.id_token_signed_response_alg = 'RS256'
        response.userinfo_signed_response_alg = 'RS256'
        response.id_token_encrypted_response_alg = 'RSA1_5'
        response.id_token_encrypted_response_enc = 'A256GCM'
        response.userinfo_encrypted_response_alg = 'RSA1_5'
        response.userinfo_encrypted_response_enc = 'A256GCM'

        return response

    @staticmethod
    def update(registration_access_token: str, request: UpdateRequestModel):
        """Update Registration Request for an existing client at the BCSC OpenID Provider."""
        if current_app.config.get('dynamic_api_return_none'):
            return None

        response = UpdateResponseModel({})
        response.client_id = request.client_id
        response.client_secret = secrets.token_urlsafe(30)
        response.registration_access_token = registration_access_token
        response.registration_client_uri = request.api_url + '/oauth2/register/' + response.client_id
        response.client_id_issued_at = json.dumps(datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'))
        response.client_secret_expires_at = '0'
        response.client_name = request.client_name
        response.client_uri = request.client_uri
        response.redirect_uris = request.redirect_uris
        response.jwks_uri = request.jwks_uri
        response.contacts = request.contacts
        response.token_endpoint_auth_method = request.token_endpoint_auth_method \
            if request.token_endpoint_auth_method is not None else 'client_secret_post'
        response.application_type = 'web'
        response.subject_type = 'pairwise'
        response.sector_identifier_uri = 'urn:org:example:client'
        response.id_token_signed_response_alg = request.id_token_signed_response_alg
        response.userinfo_signed_response_alg = request.userinfo_signed_response_alg
        response.id_token_encrypted_response_alg = request.id_token_encrypted_response_alg \
            if request.id_token_encrypted_response_alg is not None else 'RSA1_5'
        response.id_token_encrypted_response_enc = request.id_token_encrypted_response_enc \
            if request.id_token_encrypted_response_enc is not None else 'A256GCM'
        response.userinfo_encrypted_response_alg = request.userinfo_encrypted_response_alg \
            if request.userinfo_encrypted_response_alg is not None else 'RSA1_5'
        response.userinfo_encrypted_response_enc = request.userinfo_encrypted_response_enc \
            if request.userinfo_encrypted_response_enc is not None else 'A256GCM'

        return response

    @staticmethod
    def delete(client_id: str, registration_access_token: str, api_url: str):  # pylint: disable=unused-argument
        """Delete Registration Request for a new client at the BCSC OpenID Provider."""
        return True
