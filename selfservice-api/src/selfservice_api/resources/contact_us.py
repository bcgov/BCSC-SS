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
"""API endpoints for exposing contact us."""

from http import HTTPStatus

from flask import escape, request
from flask_restplus import Namespace, Resource, cors
from marshmallow import ValidationError

from ..schemas import ContactUsSchema
from ..services.notification import EmailService, EmailType
from ..utils.util import cors_preflight


API = Namespace('ContactUs', description='ContactUs')


@cors_preflight('POST,OPTIONS')
@API.route('', methods=['POST', 'OPTIONS'])
class ContactUsResource(Resource):
    """Resource for managing contact us."""

    @staticmethod
    @cors.crossdomain(origin='*')
    def post():
        """Send contact us email."""
        contactus_json = request.get_json()

        try:
            dict_data = ContactUsSchema().load(contactus_json)
            dict_data['description'] = escape(dict_data['description'])
            EmailService.save_and_send(EmailType.CONTACT_US, dict_data)
            response, status = 'Received successfully', HTTPStatus.OK
        except ValidationError as project_err:
            response, status = {'systemErrors': project_err.messages}, \
                HTTPStatus.BAD_REQUEST
        return response, status
