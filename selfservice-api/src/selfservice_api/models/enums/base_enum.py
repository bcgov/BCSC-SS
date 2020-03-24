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
"""This exports all of the base enums used by the application."""

from enum import Enum, IntEnum


class ExtendedEnum(Enum):
    """Extended Enum."""

    @classmethod
    def list(cls):
        """Get list of values."""
        return list(map(lambda c: c.value, cls))


class ExtendedIntEnum(IntEnum):
    """Extended Int Enum."""

    def __new__(cls, value, phrase=''):
        """Customize the value to include phrase."""
        obj = int.__new__(cls, value)
        obj._value_ = value

        obj.phrase = phrase
        return obj

    @classmethod
    def get_phrase(cls, value):
        """Get phrase by value."""
        return cls(value).phrase
