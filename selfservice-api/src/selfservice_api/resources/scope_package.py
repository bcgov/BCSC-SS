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
"""API endpoints for scope package."""

from http import HTTPStatus

from flask import jsonify
from flask_restplus import Namespace, Resource, cors

from ..models.scope_package import ScopePackage
from ..schemas.scope_package import ScopePackageSchema
from ..utils.auth import jwt
from ..utils.util import cors_preflight


API = Namespace('ScopePackage', description='ScopePackage')


@cors_preflight('GET,OPTIONS')
@API.route('', methods=['GET', 'OPTIONS'])
class ScopePackageResource(Resource):
    """Resource for managing get scope packages."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def get():
        """Get all scope package."""
        scope_packages = ScopePackage.find_all()

        return jsonify({
            'scopePackages': ScopePackageSchema().dump(scope_packages, many=True)
        }), HTTPStatus.OK
