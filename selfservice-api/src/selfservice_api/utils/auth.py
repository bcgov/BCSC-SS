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
"""Bring in the common JWT Manager and helper functions."""

from functools import wraps
from http import HTTPStatus

from flask import g
from flask_jwt_oidc import JwtManager

from ..exceptions import BusinessException
from ..models import User
from ..models.project import ProjectUsersAssociation
from .roles import Role


jwt = JwtManager()  # pylint: disable=invalid-name; lower case name as used by convention in most Flask apps


def can_access_project(project_roles):
    """User should have one of the roles on the project.

    Args:
        roles [str,]: Comma separated list of valid roles
    """
    def decorated(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if is_client_role():
                token_info = g.jwt_oidc_token_info
                user = User.find_by_oauth_id(token_info.get('sub'))

                if user is not None:
                    project_id = kwargs.get('project_id')
                    associations = ProjectUsersAssociation.find_all(project_id, user.id)
                    if associations is not None:
                        roles = [association.role for association in associations]
                        if all(elem in project_roles for elem in roles):
                            return f(*args, **kwargs)
                raise BusinessException('Access Denied', HTTPStatus.UNAUTHORIZED)

            return f(*args, **kwargs)
        return wrapper
    return decorated


def is_client_role():
    """Return True if the JWT relam roles contains ss_client and doesn't contain ss_admin."""
    token_info = g.jwt_oidc_token_info

    realm_access = token_info.get('realm_access')
    if Role.ss_admin not in realm_access.get('roles') and Role.ss_client in realm_access.get('roles'):
        return True

    return False
