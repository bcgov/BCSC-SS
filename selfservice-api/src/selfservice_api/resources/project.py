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
"""API endpoints for managing an project resource."""

from http import HTTPStatus

from flask import g, request
from flask_restplus import Namespace, Resource, cors
from marshmallow import ValidationError

from ..models import Project, TechnicalReq
from ..models.enums.project import ProjectStatus
from ..schemas.project import ProjectSchema
from ..utils.auth import jwt
from ..utils.util import cors_preflight


API = Namespace('Project', description='Project')


@cors_preflight('POST,OPTIONS')
@API.route('', methods=['POST', 'OPTIONS'])
class ProjectResource(Resource):
    """Resource for managing create project."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def post():
        """Post a new project using the request body."""
        project_json = request.get_json()

        try:
            token_info = g.jwt_oidc_token_info
            project_schema = ProjectSchema()
            dict_data = project_schema.load(project_json)
            project = Project.create_from_dict(dict_data, token_info.get('sub'))
            response, status = project_schema.dump(project), HTTPStatus.CREATED
        except ValidationError as project_err:
            response, status = {'message': str(project_err.messages)}, \
                HTTPStatus.BAD_REQUEST
        return response, status


@cors_preflight('GET,PATCH,OPTIONS')
@API.route('/<int:project_id>', methods=['GET', 'PATCH', 'OPTIONS'])
class ProjectResourceById(Resource):
    """Resource for managing get project by id."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def get(project_id):
        """Get project details."""
        project = Project.find_by_id(project_id)

        return ProjectSchema().dump(project), HTTPStatus.OK

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def patch(project_id):
        """Update project status."""
        project_patch_json = request.get_json()

        project = Project.find_by_id(project_id)
        token_info = g.jwt_oidc_token_info
        if 'update' in project_patch_json:
            if project_patch_json['update'] == 'status' and \
                    ProjectResourceById._validate_before_status_update_(project, project_patch_json.get('status')):

                project.update_status(token_info.get('sub'), project_patch_json['status'])
                return 'Updated successfully', HTTPStatus.OK

        return 'Update failed', HTTPStatus.BAD_REQUEST

    @staticmethod
    def _validate_before_status_update_(project: Project, status):
        """Validate the project details before updating status."""
        if project is not None:
            if status == ProjectStatus.DevSubmitted:
                technical_req = TechnicalReq.find_by_project_id(project.id)
                if technical_req is not None and \
                    technical_req.scope_package_id is not None and \
                        technical_req.no_of_test_account is not None:
                    return True

        return False
