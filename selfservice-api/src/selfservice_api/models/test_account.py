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
"""This manages Test Account Data."""

from __future__ import annotations

from .base_model import BaseModel
from .db import db


class TestAccount(BaseModel, db.Model):
    """This class manages test account information."""

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=True)

    card_number = db.Column(db.String(50), nullable=False)
    passcode = db.Column(db.String(20), nullable=False)

    attributes = db.Column(db.JSON(), nullable=True)

    @classmethod
    def create_from_dict(cls, test_accounts):
        """Create test account's from list of dictionary."""
        for test_account_info in test_accounts:
            test_account = TestAccount()
            test_account.card_number = test_account_info['card_number']
            test_account.passcode = test_account_info['passcode']
            test_account.attributes = test_account_info['attributes']
            test_account.save()

    @classmethod
    def map_test_accounts(cls, project_id: int, no_of_accounts: int):
        """Find available test accounts and map to a project."""
        project_test_accounts = TestAccount.find_all_by_project_id(project_id)
        if len(project_test_accounts) == 0:
            TestAccount._update_project_id_(project_id, no_of_accounts)
        else:
            if len(project_test_accounts) < no_of_accounts:
                required_account = no_of_accounts - len(project_test_accounts)
                TestAccount._update_project_id_(project_id, required_account)
            elif len(project_test_accounts) > no_of_accounts:
                no_of_accounts_to_reomve = len(project_test_accounts) - no_of_accounts
                for test_account in project_test_accounts:
                    if no_of_accounts_to_reomve == 0:
                        break
                    test_account.update({'project_id': None})
                    no_of_accounts_to_reomve = no_of_accounts_to_reomve - 1

    @classmethod
    def _update_project_id_(cls, project_id, no_of_accounts):
        available_accounts = cls.query.filter(TestAccount.project_id.is_(None)).limit(no_of_accounts).all()
        for test_account in available_accounts:
            test_account.project_id = project_id

        db.session.commit()

    @classmethod
    def get_availability_count(cls):
        """Get availability count of test account."""
        return cls.query.filter(TestAccount.project_id.is_(None)).count()

    @classmethod
    def find_all_by_project_id(cls, project_id):
        """Find test account that matches the provided id."""
        return cls.query.filter(TestAccount.project_id == project_id).all()

    def update(self, test_account_info: dict):
        """Update test account."""
        self.update_from_dict(['project_id'],
                              test_account_info)
        self.commit()
