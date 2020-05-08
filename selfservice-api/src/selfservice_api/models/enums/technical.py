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
"""This manages Technical Enums."""

from .base_enum import ExtendedEnum, ExtendedIntEnum


class SignedAlgorithm(ExtendedEnum):
    """This enum provides the list of Signed Algorithm supported by Dynamic API."""

    HS256 = 'HS256'
    HS384 = 'HS384'
    HS512 = 'HS512'
    RS256 = 'RS256'
    RS384 = 'RS384'
    RS512 = 'RS512'
    ES256 = 'ES256'
    ES384 = 'ES384'
    ES512 = 'ES512'
    PS256 = 'PS256'
    PS384 = 'PS384'
    PS512 = 'PS512'


class EncryptedAlgorithm(ExtendedEnum):
    """This enum provides the list of Encrypted Algorithm supported by Dynamic API."""

    RSA1_5 = 'RSA1_5'
    RSA_OAEP = 'RSA-OAEP'


class EncryptedEncoding(ExtendedEnum):
    """This enum provides the list of Encrypted Encoding supported by Dynamic API."""

    A256GCM = 'A256GCM'
    A256CBC_PLUS_HS512 = 'A256CBC+HS512'
    A192GCM = 'A192GCM'
    A128GCM = 'A128GCM'
    A128CBC_HS256 = 'A128CBC-HS256'
    A192CBC_HS384 = 'A192CBC-HS384'
    A256CBC_HS512 = 'A256CBC-HS512'
    A128CBC_PLUS_HS256 = 'A128CBC+HS256'


class SigningEncryptionType(ExtendedIntEnum):
    """This enum provides the list of Signing and Encryption type."""

    SignedJWT = 1, 'Signed JWT'
    SecureJWT = 2, 'Secure JWT'
