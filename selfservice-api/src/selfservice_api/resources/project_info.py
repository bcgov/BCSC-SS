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
"""API endpoints for managing an project info resource."""

from http import HTTPStatus

from flask import g, request
from flask_restplus import Namespace, Resource, cors
from marshmallow import ValidationError

from ..models.project_info import ProjectInfo
from ..schemas.project_info import ProjectInfoRequestSchema
from ..utils.auth import jwt
from ..utils.util import cors_preflight


API = Namespace('ProjectInfo', description='ProjectInfo')


@cors_preflight('GET,POST,OPTIONS')
@API.route('', methods=['GET', 'POST', 'OPTIONS'])
class ProjectInfoResource(Resource):
    """Resource for managing create and get project information."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def post():
        """Post a new project information using the request body."""
        project_info_json = request.get_json()

        try:
            token_info = g.jwt_oidc_token_info
            dict_data = ProjectInfoRequestSchema().load(project_info_json)
            dict_data['oauth_id'] = token_info.get('sub')
            ProjectInfo.create_from_dict(dict_data)
            response, status = 'success', HTTPStatus.CREATED.value
        except ValidationError as err:
            response, status = {'message': str(err.messages)}, \
                HTTPStatus.BAD_REQUEST.value
        return response, status
