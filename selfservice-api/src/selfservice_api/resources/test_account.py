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
"""API endpoints for managing test account resource."""

import csv
from http import HTTPStatus

from flask import current_app, jsonify, request
from flask_restplus import Namespace, Resource, cors

from ..models.test_account import TestAccount
from ..utils.auth import auth
from ..utils.util import cors_preflight


API = Namespace('TestAccount', description='Test Account')


@cors_preflight('GET,OPTIONS')
@API.route('/availability', methods=['GET', 'OPTIONS'])
class TestAccountCountResource(Resource):
    """Resource to get availability of test account."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @auth.has_one_of_roles(['ss_admin'])
    def get():
        """Get availability of test account."""
        warning_count = current_app.config.get('LIMITED_TEST_ACCOUNT_TRIGGER_COUNT')
        available_count = TestAccount.get_availability_count()
        total_count = TestAccount.get_total_count()
        return jsonify({
            'available': available_count,
            'total': total_count,
            'warning': available_count <= warning_count
        }), HTTPStatus.OK


@cors_preflight('POST,OPTIONS')
@API.route('', methods=['POST', 'OPTIONS'])
class TestAccountResource(Resource):
    """Resource for managing create test account."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @auth.has_one_of_roles(['ss_admin'])
    def post():
        """Bulk insert of test account in csv format."""
        test_account_json = request.get_json()
        data = test_account_json.get('testAccounts') if test_account_json else None
        if not data:
            return 'Unknown data', HTTPStatus.BAD_REQUEST
        test_accounts, total_count = TestAccountResource._read_from_csv_data_(data)

        no_of_created = TestAccount.create_from_list(test_accounts)
        response, status = {
            'created': no_of_created,
            'skipped': total_count - no_of_created
        }, HTTPStatus.CREATED

        return response, status

    @staticmethod
    def _read_from_csv_data_(data: str):
        test_accounts_data = data.split('\n')
        fieldnames = ['card_number', 'passcode', 'surname', 'givenname',
                      'gender', 'address1', 'address2', 'postcode', 'dob']
        test_accounts = []
        for row in csv.DictReader(test_accounts_data, fieldnames=fieldnames):
            if row['card_number'] and row['passcode']:
                attributes = {}
                attributes['surname'] = row.pop('surname')
                attributes['givenname'] = row.pop('givenname')
                attributes['gender'] = row.pop('gender')
                attributes['address1'] = row.pop('address1')
                attributes['address2'] = row.pop('address2')
                attributes['postcode'] = row.pop('postcode')
                attributes['dob'] = row.pop('dob')
                row['attributes'] = attributes
                test_accounts.append(row)

        return test_accounts, len(test_accounts_data)
