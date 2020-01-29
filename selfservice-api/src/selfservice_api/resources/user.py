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
"""API endpoints for managing an user resource."""

from http import HTTPStatus

from flask import g
from flask_restplus import Namespace, Resource, cors
from marshmallow import ValidationError

from ..models.user import User
from ..schemas.user import UserSchema
from ..utils.auth import jwt
from ..utils.util import cors_preflight


API = Namespace('User', description='User')


@cors_preflight('GET,POST,OPTIONS')
@API.route('', methods=['GET', 'POST', 'OPTIONS'])
class UserResource(Resource):
    """Resource for managing create and get user."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def get():
        """Get user details."""
        token_info = g.jwt_oidc_token_info
        user = User.find_by_oauth_id(token_info.get('sub'))

        return UserSchema().dump(user), HTTPStatus.OK

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def post():
        """Post a new user using the request body."""
        token_info = g.jwt_oidc_token_info

        try:
            user = User.find_by_oauth_id(token_info.get('sub'))

            user_schema = UserSchema()
            if not user:
                dict_data = user_schema.load({
                    # Email from token is for this Sprint. Must be changed based on the user creation.
                    'email': token_info.get('email'),
                    'phone': '',
                    'firstName': token_info.get('given_name'),
                    'lastName': token_info.get('family_name'),
                    'oauthId': token_info.get('sub')
                })
                user = User.create_from_dict(dict_data)

            response, status = user_schema.dump(user), HTTPStatus.CREATED
        except ValidationError as err:
            response, status = {'message': str(err.messages)}, \
                HTTPStatus.BAD_REQUEST
        return response, status
