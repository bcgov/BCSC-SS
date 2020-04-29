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
"""This tests TestAccount model."""

from ..helper.request_data import factory_test_account

from selfservice_api.models.test_account import TestAccount
from selfservice_api.resources.test_account import TestAccountResource


def test_create_from_list(session):
    """Assert test account creation from list."""
    test_accounts, total_count = \
        TestAccountResource._read_from_csv_data_(factory_test_account(is_model=True)['testAccounts'])
    length = TestAccount.create_from_list(test_accounts)
    assert length > 0


def test_none_create_from_list(session):
    """Assert skipping test account creation by providing None."""
    length = TestAccount.create_from_list(None)
    assert length == 0
