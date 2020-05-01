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
"""API endpoints for managing project resource."""

from http import HTTPStatus

from flask import g, jsonify, request
from flask_restplus import Namespace, Resource, cors
from marshmallow import ValidationError

from ..models import OIDCConfig, Project, ProjectUsersAssociation, TechnicalReq, TestAccount
from ..models.enums import ProjectRoles, ProjectStatus
from ..schemas import ProjectSchema
from ..services import AuditService, ProjectService
from ..utils.auth import auth
from ..utils.roles import Role
from ..utils.util import cors_preflight


API = Namespace('Project', description='Project')


@cors_preflight('GET,POST,OPTIONS')
@API.route('', methods=['GET', 'POST', 'OPTIONS'])
class ProjectResource(Resource):
    """Resource for managing create project."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @auth.has_one_of_roles([Role.ss_client, Role.ss_admin])
    def get():
        """Get all project."""
        user = None
        if auth.is_client_role():
            user = g.user
        projects = Project.find_all_or_by_user(user)
        return jsonify({'projects': projects}), HTTPStatus.OK

    @staticmethod
    @cors.crossdomain(origin='*')
    @auth.require
    def post():
        """Post a new project using the request body."""
        project_json = request.get_json()

        try:
            user = g.user
            project_schema = ProjectSchema()
            dict_data = project_schema.load(project_json)
            project = Project.create_from_dict(dict_data, user)

            if auth.is_client_role():
                ProjectUsersAssociation.create(user.id, project.id, ProjectRoles.Developer)

            response, status = project_schema.dump(project), HTTPStatus.CREATED
        except ValidationError as project_err:
            response, status = {'systemErrors': project_err.messages}, \
                HTTPStatus.BAD_REQUEST
        return response, status


@cors_preflight('GET,PUT,PATCH,DELETE,OPTIONS')
@API.route('/<int:project_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])
class ProjectResourceById(Resource):
    """Resource for managing get project by id."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @auth.can_access_project([ProjectRoles.Developer, ProjectRoles.Manager, ProjectRoles.Cto])
    def get(project_id):
        """Get project details."""
        user = g.user
        project = Project.find_by_id(project_id)
        project_dump = ProjectSchema().dump(project)
        for project_users in project.users:
            if project_users.user_id == user.id:
                project_dump['myRole'] = project_users.role
        return project_dump, HTTPStatus.OK

    @staticmethod
    @cors.crossdomain(origin='*')
    @auth.require
    def delete(project_id):
        """Delete project."""
        project = Project.find_by_id(project_id)
        can_delete = bool(project)
        including_prod = not auth.is_client_role()

        if auth.is_client_role() and can_delete:
            can_delete = project.status < ProjectStatus.DevelopmentComplete

        if can_delete:
            TestAccount.map_test_accounts(project.id, 0)
            TechnicalReq.delete_by_project_id(project.id)
            ProjectUsersAssociation.delete_all_by_project_id(project.id)
            ProjectService.dynamic_api_delete(project, including_prod)
            OIDCConfig.delete_by_project_id(project.id)
            project.delete()
            return 'Deleted successfully', HTTPStatus.OK

        return 'Delete failed', HTTPStatus.BAD_REQUEST

    @staticmethod
    @cors.crossdomain(origin='*')
    @auth.can_access_project([ProjectRoles.Developer, ProjectRoles.Manager, ProjectRoles.Cto])
    def put(project_id):
        """Update project details."""
        project_json = request.get_json()

        try:
            project_schema = ProjectSchema()
            dict_data = project_schema.load(project_json)

            user = g.user
            project = Project.find_by_id(project_id)
            project.update(dict_data, user)

            return 'Updated successfully', HTTPStatus.OK
        except ValidationError as project_err:
            return {'systemErrors': project_err.messages}, HTTPStatus.BAD_REQUEST

    @staticmethod
    @cors.crossdomain(origin='*')
    @auth.can_access_project([ProjectRoles.Developer, ProjectRoles.Manager, ProjectRoles.Cto])
    def patch(project_id):
        """Update project status."""
        user = g.user
        project_patch_json = request.get_json()

        project = Project.find_by_id(project_id)
        if ProjectService.validate_before_status_update(project, project_patch_json):
            response = {'message': 'Updated successfully'}
            project_status = project_patch_json['status']
            is_success = True

            # Decide when and which api to call
            if project_status == ProjectStatus.Development:
                is_success = ProjectService.dynamic_api_save(project, False)
                if is_success:
                    response_additional = ProjectService.on_development_status(project)
                    response.update(response_additional)

            # Make sure we are not downgrading the project status
            if project.status < project_status:
                project.update_status(project_status, user)
                AuditService.log_project_status_change(project, user)
                response.update({'isCreated': True})
            else:
                response.update({'isUpdated': True})

            if is_success:
                status = HTTPStatus.OK
            else:
                response, status = 'OIDC Failed', HTTPStatus.INTERNAL_SERVER_ERROR
            return response, status

        return 'Update failed', HTTPStatus.BAD_REQUEST
