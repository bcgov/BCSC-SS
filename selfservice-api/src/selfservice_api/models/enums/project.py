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

from enum import Enum, IntEnum


class ProjectRoles(IntEnum):
    """This Enum provides the list of Project Roles."""

    def __new__(cls, value, phrase=''):
        """Customize the value to include phrase."""
        obj = int.__new__(cls, value)
        obj._value_ = value

        obj.phrase = phrase
        return obj

    Developer = 1, 'Developer'
    Manager = 2, 'Manager'
    Cto = 3, 'Executive Sponsor'

    @staticmethod
    def get_phrase(value):
        """Get phrase by value."""
        return ProjectRoles(value).phrase


class ProjectStatus(IntEnum):
    """This Enum provides the list of Project Status."""

    def __new__(cls, value, phrase=''):
        """Customize the value to include phrase."""
        obj = int.__new__(cls, value)
        obj._value_ = value

        obj.phrase = phrase
        return obj

    Draft = 1, 'Draft'
    Development = 2, 'Development'

    @staticmethod
    def get_phrase(value):
        """Get phrase by value."""
        return ProjectStatus(value).phrase


class Algorithms(Enum):
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
