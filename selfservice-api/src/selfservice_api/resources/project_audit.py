# Copyright © 2020 Province of British Columbia
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
"""API endpoints for managing project audit."""

from http import HTTPStatus

from flask import jsonify
from flask_restplus import Namespace, Resource, cors

from ..models import Audit
from ..models.enums import ProjectRoles, ProjectStatus
from ..utils.auth import auth
from ..utils.util import cors_preflight


API = Namespace('ProjectAudit', description='Project Audit')


@cors_preflight('GET,OPTIONS')
@API.route('', methods=['GET', 'OPTIONS'])
class ProjectAuditResource(Resource):
    """Resource for managing get project audit by project id."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @auth.can_access_project([ProjectRoles.Developer, ProjectRoles.Manager, ProjectRoles.Cto])
    def get(project_id):
        """Get project audit status."""
        status_list = Audit.find_project_status(project_id)
        last_status = status_list[-1]['status'] if len(status_list) > 0 else 0
        for project_status in ProjectStatus:
            if last_status < project_status:
                status_list.append({
                    'status': project_status,
                    'created': '',
                    'name': '',
                    'role': ''
                })
        return jsonify({
            'history': status_list
        }), HTTPStatus.OK
