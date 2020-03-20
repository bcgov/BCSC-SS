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
"""This manages Project Enums."""

from .base_enum import ExtendedEnum, ExtendedIntEnum


class ProjectRoles(ExtendedIntEnum):
    """This enum provides the list of Project Roles."""

    Developer = 1, 'Developer'
    Manager = 2, 'Manager'
    Cto = 3, 'Executive Sponsor'


class ProjectStatus(ExtendedIntEnum):
    """This enum provides the list of Project Status."""

    Draft = 1, 'Draft'
    Development = 2, 'Development'


class Algorithms(ExtendedEnum):
    """This enum provides the list of Algorithms supported by Dynamic API."""

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


class SigningEncryptionType(ExtendedIntEnum):
    """This enum provides the list of Signing and Encryption type."""

    SimpleJSON = 1, 'Simple JSON'
    SignedJWT = 2, 'Signed JWT'
    SecureJWT = 3, 'Secure JWT'
