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
"""API endpoints for managing an technical requirement resource."""

from http import HTTPStatus

from flask import g, request
from flask_restplus import Namespace, Resource, cors
from marshmallow import ValidationError

from ..models.technical_req import TechnicalReq
from ..schemas.technical_req import (TechnicalReqPackageSchema, TechnicalReqRequestSchema,  # noqa: I001
                                     TechnicalReqResponseSchema, TechnicalReqTestAccountSchema)  # noqa: I001
from ..utils.auth import jwt
from ..utils.util import cors_preflight


API = Namespace('TechnicalReq', description='Technical Requirement')


@cors_preflight('GET,POST,PUT,PATCH,OPTIONS')
@API.route('', methods=['GET', 'POST', 'PUT', 'PATCH', 'OPTIONS'])
class TechnicalReqResource(Resource):
    """Resource for managing create technical requirement."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def post(project_id):
        """Post a new technical requirement using the request body."""
        technical_req_json = request.get_json()

        try:
            token_info = g.jwt_oidc_token_info
            technical_req_schema = TechnicalReqRequestSchema()
            dict_data = technical_req_schema.load(technical_req_json)
            dict_data['project_id'] = project_id
            technical_req = TechnicalReq.create_from_dict(dict_data, token_info.get('sub'))
            response, status = technical_req_schema.dump(technical_req), HTTPStatus.CREATED
        except ValidationError as technical_req_err:
            response, status = {'message': str(technical_req_err.messages)}, \
                HTTPStatus.BAD_REQUEST
        return response, status

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def get(project_id):
        """Get technical requirement details."""
        technical_req = TechnicalReq.find_by_project_id(project_id)

        return TechnicalReqResponseSchema().dump(technical_req), HTTPStatus.OK

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def put(project_id):
        """Update technical requirement using the request body."""
        technical_req_json = request.get_json()

        try:
            token_info = g.jwt_oidc_token_info
            technical_req_schema = TechnicalReqRequestSchema()
            dict_data = technical_req_schema.load(technical_req_json)
            dict_data['project_id'] = project_id
            technical_req = TechnicalReq.find_by_project_id(project_id)
            technical_req.update(token_info.get('sub'), dict_data)
            response, status = 'Updated successfully', HTTPStatus.OK
        except ValidationError as technical_req_err:
            response, status = {'message': str(technical_req_err.messages)}, HTTPStatus.BAD_REQUEST
        return response, status

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def patch(project_id):
        """Update scope package or test account in technical requirement."""
        tr_patch_json = request.get_json()

        token_info = g.jwt_oidc_token_info
        technical_req_info = None
        if 'update' in tr_patch_json:
            if tr_patch_json['update'] == 'package':
                technical_req_info = TechnicalReqPackageSchema().load(tr_patch_json)
            if tr_patch_json['update'] == 'test-account':
                technical_req_info = TechnicalReqTestAccountSchema().load(tr_patch_json)

        if technical_req_info is not None:
            technical_req = TechnicalReq.find_by_project_id(project_id)
            technical_req.update(token_info.get('sub'), technical_req_info)
            response, status = 'Updated successfully', HTTPStatus.OK
        else:
            response, status = 'Update failed', HTTPStatus.BAD_REQUEST

        return response, status
