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
"""Auth Test Utility for API testing."""

import os
from enum import Enum


JWT_HEADER = {
    'alg': os.getenv('JWT_OIDC_ALGORITHMS'),
    'typ': 'JWT',
    'kid': os.getenv('JWT_OIDC_AUDIENCE')
}


class TestJwtClaims(dict, Enum):
    """Test scenarios of jwt claims."""

    invalid = {
        'sub': 'barfoo',
        'given_name': 'Trouble',
        'family_name': 'Maker',
        'preferred_username': 'troublemaker'
    }

    ss_client = {
        'iss': os.getenv('JWT_OIDC_ISSUER'),
        'sub': '79ae27e8-4f87-4b7d-8075-46aa4be72e02',
        'given_name': 'client',
        'family_name': 'ss',
        'email': 'developer@email.com',
        'preferred_username': 'ssclient',
        'realm_access': {
            'roles': [
                'ss_client'
            ]
        }
    }

    ss_admin = {
        'iss': os.getenv('JWT_OIDC_ISSUER'),
        'sub': '79ae27e8-4f87-4b7d-8075-46aa4be72e02',
        'given_name': 'admin',
        'family_name': 'ss',
        'preferred_username': 'ssadmin',
        'realm_access': {
            'roles': [
                'ss_admin'
            ]
        }
    }


def ss_client_auth_header(jwt):
    """Produce ss_client JWT tokens for use in tests."""
    return {'Authorization': 'Bearer ' + jwt.create_jwt(claims=TestJwtClaims.ss_client, header=JWT_HEADER)}


def ss_admin_auth_header(jwt):
    """Produce ss_admin JWT tokens for use in tests."""
    return {'Authorization': 'Bearer ' + jwt.create_jwt(claims=TestJwtClaims.ss_admin, header=JWT_HEADER)}


def invalid_auth_header(jwt):
    """Produce invalid JWT tokens for use in tests."""
    return {'Authorization': 'Bearer ' + jwt.create_jwt(claims=TestJwtClaims.invalid, header=JWT_HEADER)}
