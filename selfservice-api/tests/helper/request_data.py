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
"""Data for API testing."""


def factory_project_info():
    """JSON data to create project info."""
    return {
        'organizationName': 'organization',
        'projectName': 'project',
        'description': 'project which i am trying to create',
        'myRole': 1,
        'developerDetails': {},
        'managerDetails': {
            'email': 'manager@email.com',
            'phone': '1234567890',
            'firstName': 'f manager',
            'lastName': 'l manager'
        },
        'ctoDetails': {
            'email': 'cto@email.com',
            'phone': '1234567890',
            'firstName': 'f cto',
            'lastName': 'l cto'
        }
    }


def factory_project_technical_req():
    """JSON data to create technical req."""
    return {
        'projectId': 0,
        'clientUri': 'https://someone.com',
        'redirectUris': [
            'https://someone.com/*'
        ],
        'jwksUri': 'https://someone.com/jwks',
        'idTokenSignedResponseAlg': 'RS256',
        'userinfoSignedResponseAlg': 'RS256'
    }
