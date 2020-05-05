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
"""OIDC Dynamic Client Create Request/Response Models."""


class CreateRequestModel:  # pylint: disable=too-few-public-methods
    """Client Registration Request Model."""

    """Required. Name of the Client."""  # pylint: disable=pointless-string-statement
    client_name: str

    """Required.
    URL of the home page of the Client. The
    value of this field MUST point to a valid Web
    page, and will be presented to end users in
    BCSC Account Activity, and possibly during
    authentication."""
    client_uri: str

    """Required.
    Array of Redirection URI values used by the
    Client. One of these registered Redirection
    URI values MUST exactly match the redirect
    _uri parameter value used in each
    Authorization Request.
    In non-production instances this array may
    include localhost values for developers."""
    redirect_uris: []

    """Optional.
    If no scope is provided, defaults to
    'openid profile address email'"""
    scope: str

    """Required.
    URL for the Client's JSON Web Key Set
    (JWKS) document. The JWK Set MUST
    contain the Client's encryption keys(s),
    which are used by the Server to encrypt
    responses to the Client."""
    jwks_uri: str

    """Required.
    Array of e-mail addresses of people
    responsible for this Client."""
    contacts: []

    """Optional.
    Requested Client Authentication method for
    the Token Endpoint. The options are
    client_secret_post, client_secret_basic,
    client_secret_jwt, private_key_jwt. If
    omitted, the default is client_secret_post."""
    token_endpoint_auth_method: str

    """Required.
    The assigned signature algorithm. Currently
    defaulted to RS256. Likely to be defaulted to
    RS512 in the future."""
    id_token_signed_response_alg: str

    """Required.
    The assigned signature algorithm. Currently
    defaulted to RS256. Likely to be defaulted to
    RS512 in the future."""
    userinfo_signed_response_alg: str

    """Optional.
    The algorithm used to determine the content
    encryption key for encrypting the id_token.
    Acceptable values published via OIDC
    Connect Discovery."""
    id_token_encrypted_response_alg: str

    """Optional.
    The algorithm used to encrypt the id_token.
    Acceptable values published via OIDC
    Connect Discovery."""
    id_token_encrypted_response_enc: str

    """Optional.
    The algorithm used to determine the content
    encryption key for encrypting the userinfo
    response. Acceptable values published via
    OIDC Connect Discovery."""
    userinfo_encrypted_response_alg: str

    """Optional.
    The algorithm used to encrypt the userinfo
    response. Acceptable values published via
    OIDC Connect Discovery."""
    userinfo_encrypted_response_enc: str

    """api_url and api_token are required to make dynamic api call."""
    api_url: str
    api_token: str


class CreateResponseModel:  # pylint: disable=too-few-public-methods
    """Client Registration Response Model."""

    def __init__(self, _dict: dict):
        """Initialize response."""
        self.__dict__ = _dict

    """The assigned unique client identifier."""  # pylint: disable=pointless-string-statement
    client_id: str

    """If the assigned token endpoint client authentication method requires
    a client secret this field will be populated. Not provided for
    private_key_jwt."""
    client_secret: str

    """Registration Access Token that can be used at the Client
    Configuration Endpoint to perform subsequent operations upon the
    Client registration."""
    registration_access_token: str

    """Location of the Client Configuration Endpoint where the Registration
    Access Token can be used to perform subsequent operations upon
    the resulting Client registration."""
    registration_client_uri: str

    """Time at which the Client Identifier was issued. Its value is a JSON
    number representing the number of seconds from 1970-01-01T0:0:
    0Z as measured in UTC until the date/time."""
    client_id_issued_at: str

    """The date the client secret expires."""
    client_secret_expires_at: str

    """Name of the Client that will be presented to the end user during
    authentication."""
    client_name: str

    """URL of the home page of the Client. The value of this field MUST
    point to a valid Web page, and will be presented to end users in
    BCSC Account Activity, and possibly during authentication."""
    client_uri: str

    """Array of Redirection URI values used by the Client. One of these
    registered Redirection URI values MUST exactly match
    the redirect_uri parameter value used in each Authorization Request."""
    redirect_uris: []

    """URL for the Client's JSON Web Key Set (JWKS) document. The
    JWK Set MUST contain the Client's encryption keys(s), which are
    used by the Server to encrypt responses to the Client."""
    jwks_uri: str

    """Array of e-mail addresses of people responsible for this Client."""
    contacts: []

    """Requested Client Authentication method for the Token Endpoint.
    The options are client_secret_post, client_secret_basic,
    client_secret_jwt, private_key_jwt. If omitted, the default is
    client_secret_post."""
    token_endpoint_auth_method: str

    """Example: web"""
    application_type: str

    """Example: pairwise"""
    subject_type: str

    """Example: urn:org:example:client"""
    sector_identifier_uri: str

    """The assigned signature algorithm. Currently defaulted to RS256.
    Likely to be defaulted to RS512 in the future."""
    id_token_signed_response_alg: str

    """The assigned signature algorithm. Currently defaulted to RS256.
    Likely to be defaulted to RS512 in the future."""
    userinfo_signed_response_alg: str

    """The algorithm used to determine the content encryption key for
    encrypting the id_token. Acceptable values published via OIDC
    Connect Discovery."""
    id_token_encrypted_response_alg: str

    """The algorithm used to encrypt the id_token. Acceptable values
    published via OIDC Connect Discovery."""
    id_token_encrypted_response_enc: str

    """The algorithm used to determine the content encryption key for
    encrypting the userinfo response. Acceptable values published via
    OIDC Connect Discovery."""
    userinfo_encrypted_response_alg: str

    """The algorithm used to encrypt the userinfo response. Acceptable
    values published via OIDC Connect Discovery."""
    userinfo_encrypted_response_enc: str
