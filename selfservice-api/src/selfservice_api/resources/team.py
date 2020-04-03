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
"""API endpoints for managing team resource."""

from http import HTTPStatus

from flask import g, jsonify, request
from flask_restplus import Namespace, Resource, cors
from marshmallow import ValidationError

from ..exceptions import BusinessException
from ..models import OrgWhitelist, ProjectUsersAssociation
from ..models.enums import ProjectRoles
from ..schemas import TeamSchema
from ..utils.auth import auth
from ..utils.util import cors_preflight


API = Namespace('Team', description='Team')


@cors_preflight('GET,POST,OPTIONS')
@API.route('', methods=['GET', 'POST', 'OPTIONS'])
class TeamResource(Resource):
    """Resource for managing team."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @auth.can_access_project([ProjectRoles.Developer, ProjectRoles.Manager, ProjectRoles.Cto])
    def get(project_id):
        """Get team."""
        team = ProjectUsersAssociation.find_all_by_project_id(project_id)
        data = TeamSchema().dump(team, many=True)
        return jsonify({'team': data}), HTTPStatus.OK

    @staticmethod
    @cors.crossdomain(origin='*')
    @auth.can_access_project([ProjectRoles.Developer, ProjectRoles.Manager, ProjectRoles.Cto])
    def post(project_id):
        """Post a new team using the request body."""
        team_json = request.get_json()

        try:
            team_schema = TeamSchema()
            dict_data = team_schema.load(team_json)
            validate_before_save(project_id, dict_data)
            team = ProjectUsersAssociation.create_from_dict(dict_data, project_id)
            response, status = team_schema.dump(team), HTTPStatus.CREATED
        except ValidationError as team_err:
            response, status = {'message': str(team_err.messages)}, HTTPStatus.BAD_REQUEST
        except BusinessException as team_be_err:
            response, status = {'errors': str(team_be_err.error)}, HTTPStatus.BAD_REQUEST
        return response, status


@cors_preflight('GET,DELETE,PUT,OPTIONS')
@API.route('/<int:member_id>', methods=['GET', 'DELETE', 'PUT', 'OPTIONS'])
class TeamResourceById(Resource):
    """Resource for managing team member by id."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @auth.can_access_project([ProjectRoles.Developer, ProjectRoles.Manager, ProjectRoles.Cto])
    def get(project_id, member_id):  # pylint: disable=unused-argument
        """Get team member."""
        team_member = ProjectUsersAssociation.find_by_id(member_id)
        return TeamSchema().dump(team_member), HTTPStatus.OK

    @staticmethod
    @cors.crossdomain(origin='*')
    @auth.can_access_project([ProjectRoles.Developer, ProjectRoles.Manager, ProjectRoles.Cto])
    def delete(project_id, member_id):  # pylint: disable=unused-argument
        """Delete member from team."""
        ProjectUsersAssociation.delete_by_id(member_id)
        return 'Deleted', HTTPStatus.OK

    @staticmethod
    @cors.crossdomain(origin='*')
    @auth.can_access_project([ProjectRoles.Developer, ProjectRoles.Manager, ProjectRoles.Cto])
    def put(project_id, member_id):
        """Update team member details."""
        team_json = request.get_json()

        try:
            team_schema = TeamSchema()
            user = g.user

            association = ProjectUsersAssociation.find_by_id(member_id)
            if association.user_id == user.id:
                dict_data = team_schema.load(team_json, partial=('role',))
                validate_before_save(project_id, dict_data, member_id)
                association.update(dict_data, only_role=True)
            else:
                dict_data = team_schema.load(team_json)
                validate_before_save(project_id, dict_data, member_id)
                association.update(dict_data)
            response, status = 'Updated successfully', HTTPStatus.OK
        except ValidationError as team_err:
            response, status = {'message': str(team_err.messages)}, HTTPStatus.BAD_REQUEST
        except BusinessException as team_be_err:
            response, status = {'errors': str(team_be_err.error)}, HTTPStatus.BAD_REQUEST
        return response, status


def validate_before_save(project_id, dict_data, association_id: str = None):
    """Validate team member before save."""
    email = dict_data['email']
    role = dict_data['role']
    email_exist = ProjectUsersAssociation.check_user_existence(project_id, email, association_id)
    role_exist = ProjectUsersAssociation.check_role_existence(project_id, role, association_id)
    errors = {}
    if email_exist:
        errors['email'] = f'{email} already assigned to a different role. \
                    Remove other role and try again.'
    if role_exist:
        errors['role'] = f'{role} already assigned to a different user. \
                    Remove other user and try again.'

    domain = email.strip().split('@').pop() if email and '@' in email else None
    if not OrgWhitelist.validate_domain(domain):
        errors['email'] = f'Invalid domain.'

    if errors:
        raise BusinessException(errors, HTTPStatus.BAD_REQUEST)
