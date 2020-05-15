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
from ..services.notification import EmailService, EmailType
from ..utils.auth import auth
from ..utils.roles import Role
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
        user = g.user
        for team_member in data:
            team_member['isCurrentUser'] = team_member['userId'] == user.id
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
            EmailService.save_and_send(EmailType.TEAM_MEMBER, {}, to=team.user.email)

            response, status = team_schema.dump(team), HTTPStatus.CREATED
        except ValidationError as team_err:
            response, status = {'systemErrors': team_err.messages}, HTTPStatus.BAD_REQUEST
        except BusinessException as team_be_err:
            response, status = {'errors': team_be_err.error}, HTTPStatus.BAD_REQUEST
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
        data = TeamSchema().dump(team_member)
        user = g.user
        data['isCurrentUser'] = data['userId'] == user.id
        return data, HTTPStatus.OK

    @staticmethod
    @cors.crossdomain(origin='*')
    @auth.has_one_of_roles([Role.ss_admin])
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
            user = g.user
            team_schema = TeamSchema()
            association = ProjectUsersAssociation.find_by_id(member_id)

            can_i_update = True  # can update if user is admin
            if auth.is_client_role():  # can update own details if user is client
                can_i_update = association.user_id == user.id

            if can_i_update:
                if association.user_id == user.id:
                    dict_data = team_schema.load(team_json, partial=('role',))
                    validate_before_save(project_id, dict_data, member_id, True)
                    association.update(dict_data, only_role=True)
                else:
                    dict_data = team_schema.load(team_json)
                    validate_before_save(project_id, dict_data, member_id)
                    association.update(dict_data)
                response, status = 'Updated successfully', HTTPStatus.OK
            else:
                response, status = 'Access Denied', HTTPStatus.UNAUTHORIZED
        except ValidationError as team_err:
            response, status = {'systemErrors': team_err.messages}, HTTPStatus.BAD_REQUEST
        except BusinessException as team_be_err:
            response, status = {'errors': team_be_err.error}, HTTPStatus.BAD_REQUEST
        return response, status


def validate_before_save(project_id, dict_data, association_id: str = None, is_current_user: bool = False):
    """Validate team member before save."""
    errors = {}

    role = dict_data['role']
    role_exist = ProjectUsersAssociation.check_role_existence(project_id, role, association_id)
    if role_exist:
        errors['role'] = 'roleAlreadyAssigned'

    if not is_current_user:
        # Skip validation if the user association is for the logged in user.
        email = dict_data['email']
        email_exist = ProjectUsersAssociation.check_user_existence(project_id, email, association_id)
        if email_exist:
            errors['email'] = 'emailAlreadyAssigned'

        domain = email.strip().split('@').pop() if email and '@' in email else None
        if not OrgWhitelist.validate_domain(domain):
            errors['email'] = 'invalidDomain'

    if errors:
        raise BusinessException(errors, HTTPStatus.BAD_REQUEST)
