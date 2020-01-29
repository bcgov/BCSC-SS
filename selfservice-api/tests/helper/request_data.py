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
"""Data for testing."""

from . import camel2snake

from selfservice_api.models.enums.project import ProjectRoles


def factory_user_info(is_model=False):
    """JSON data to create user info."""
    user = {
        'email': 'developer@email.com',
        'phone': '987654321',
        'firstName': 'client',
        'lastName': 'ss',
        'oauthId': '123456'
    }
    if is_model:
        return camel2snake(user)
    else:
        return user


def factory_project_info(is_model=False, my_role=ProjectRoles.Developer):
    """JSON data to create project info."""
    project = {
        'organizationName': 'organization',
        'projectName': 'project',
        'description': 'project which i am trying to create',
        'myRole': my_role,
        'users': []
    }
    if my_role != ProjectRoles.Developer:
        project['users'].append({
            'email': 'developer@email.com',
            'phone': '1234567890',
            'firstName': 'f developer',
            'lastName': 'l developer',
            'role': ProjectRoles.Developer
        })

    if my_role != ProjectRoles.Manager:
        project['users'].append({
            'email': 'manager@email.com',
            'phone': '1234567890',
            'firstName': 'f manager',
            'lastName': 'l manager',
            'role': ProjectRoles.Manager
        })

    if my_role != ProjectRoles.Cto:
        project['users'].append({
            'email': 'cto@email.com',
            'phone': '1234567890',
            'firstName': 'f cto',
            'lastName': 'l cto',
            'role': ProjectRoles.Cto
        })

    if is_model:
        return camel2snake(project)
    else:
        return project


def factory_project_technical_req(is_model=False):
    """JSON data to create technical req."""
    technical_req = {
        'projectId': 0,
        'clientUri': 'https://someone.com',
        'redirectUris': [
            'https://someone.com/*'
        ],
        'jwksUri': 'https://someone.com/jwks',
        'idTokenSignedResponseAlg': 'RS256',
        'userinfoSignedResponseAlg': 'RS256'
    }
    if is_model:
        return camel2snake(technical_req)
    else:
        return technical_req
