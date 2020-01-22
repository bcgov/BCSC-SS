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

from ..models.project import Project
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


@cors_preflight('GET,OPTIONS')
@API.route('/<int:project_id>', methods=['GET', 'OPTIONS'])
class ProjectResourceById(Resource):
    """Resource for managing get project by id."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def get(project_id):
        """Get project details."""
        project = Project.find_by_id(project_id)

        return ProjectSchema().dump(project), HTTPStatus.OK
