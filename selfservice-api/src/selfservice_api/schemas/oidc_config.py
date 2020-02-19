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
"""This manages OIDC Config Req/Res Schema."""

from marshmallow import EXCLUDE, Schema, fields


class OIDCConfigSchema(Schema):
    """This class manages oidc config request and response schema."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Exclude unknown fields in the deserialized output."""

        unknown = EXCLUDE

    client_id = fields.Str(data_key='clientId')
    client_secret = fields.Str(data_key='clientSecret')

    registration_access_token = fields.Str(data_key='registrationAccessToken')
    registration_client_uri = fields.Str(data_key='registrationClientUri')

    client_id_issued_at = fields.Str(data_key='clientIdIssuedAt')
    client_secret_expires_at = fields.Int(data_key='clientSecretExpiresAt')

    token_endpoint_auth_method = fields.Str(data_key='tokenEndpointAuthMethod')

    application_type = fields.Str(data_key='applicationType')
    subject_type = fields.Str(data_key='subjectType')

    sector_identifier_uri = fields.Str(data_key='sectorIdentifierUri')

    id_token_encrypted_response_alg = fields.Str(data_key='idTokenEncryptedResponseAlg')
    id_token_encrypted_response_enc = fields.Str(data_key='idTokenEncryptedResponseEnc')

    userinfo_encrypted_response_alg = fields.Str(data_key='userinfoEncryptedResponseAlg')
    userinfo_encrypted_response_enc = fields.Str(data_key='userinfoEncryptedResponseEnc')
