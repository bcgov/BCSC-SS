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

from .models.dynamic_client_create import CreateRequestModel, CreateResponseModel
from .models.dynamic_client_get import GetResponseModel
from .models.dynamic_client_update import UpdateRequestModel, UpdateResponseModel


class DynamicClientRegistrationService():
    """Service to manage OIDC Dynamic Client Registration."""

    @staticmethod
    def create(request: CreateRequestModel):
        """Client Registration Request for a new client at the BCSC OpenID Provider."""
        response = CreateResponseModel()

        return response

    @staticmethod
    def get(registration_access_token: str):
        """Get Registration Request for an existing client at the BCSC OpenID Provider."""
        return GetResponseModel()

    @staticmethod
    def update(registration_access_token: str, request: UpdateRequestModel):
        """Update Registration Request for an existing client at the BCSC OpenID Provider."""
        return UpdateResponseModel()

    @staticmethod
    def delete():
        """Delete Registration Request for a new client at the BCSC OpenID Provider."""
        return True
