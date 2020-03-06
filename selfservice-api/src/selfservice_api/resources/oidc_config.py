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
"""API endpoints for managing an oidc config."""

from http import HTTPStatus

from flask import jsonify
from flask_restplus import Namespace, Resource, cors

from ..models import OIDCConfig, TestAccount
from ..schemas import OIDCConfigSchema, TestAccountSchema
from ..utils.auth import jwt
from ..utils.util import cors_preflight


API = Namespace('OIDCConfig', description='OIDC Config')


@cors_preflight('GET,OPTIONS')
@API.route('', methods=['GET', 'OPTIONS'])
class OIDCConfigResource(Resource):
    """Resource for managing get oidc config by project id."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def get(project_id):
        """Get oidc config and test account details."""
        oidc_config = OIDCConfig.find_by_project_id(project_id)
        test_accounts = TestAccount.find_all_by_project_id(project_id)

        return jsonify({
            'oidcConfig': OIDCConfigSchema().dump(oidc_config),
            'testAccount': TestAccountSchema().dump(test_accounts, many=True)
        }), HTTPStatus.OK
