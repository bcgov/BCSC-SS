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
"""API endpoints for exposing static list of values."""

from http import HTTPStatus

from flask import jsonify
from flask_restplus import Namespace, Resource, cors

from ..models.enums.project import Algorithms
from ..utils.auth import jwt
from ..utils.util import cors_preflight


API = Namespace('Values', description='Values')


@cors_preflight('GET,OPTIONS')
@API.route('/algorithms/', methods=['GET', 'OPTIONS'])
class AlgorithmValuesResource(Resource):
    """Resource for managing get algorithm values."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @jwt.requires_auth
    def get():
        """Get algorithms."""
        algorithms = [e.value for e in Algorithms]

        return jsonify(algorithms), HTTPStatus.OK
