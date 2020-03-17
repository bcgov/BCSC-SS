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

from flask import request
from flask_restplus import Namespace, Resource, cors

from ..models.test_account import TestAccount
from ..utils.auth import auth
from ..utils.util import cors_preflight


API = Namespace('TestAccount', description='Test Account')


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
        test_accounts = TestAccountResource._read_from_csv_data_(data)

        TestAccount.create_from_dict(test_accounts)
        response, status = str(len(test_accounts)) + ' test account created', HTTPStatus.CREATED

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

        return test_accounts
