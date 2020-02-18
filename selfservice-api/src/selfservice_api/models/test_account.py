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
    def create_from_dict(cls, test_account_info: dict) -> TestAccount:
        """Create a new test account from the provided dictionary."""
        if test_account_info:
            test_account = TestAccount()
            test_account.project_id = test_account_info['project_id']
            test_account.card_number = test_account_info['card_number']
            test_account.passcode = test_account_info['passcode']
            test_account.attributes = test_account_info['attributes']

            test_account.save()

            return test_account
        return None

    @classmethod
    def find_by_project_id(cls, project_id) -> TestAccount:
        """Find test account that matches the provided id."""
        return cls.query.filter(TestAccount.project_id == project_id).first()

    def update(self, test_account_info: dict):
        """Update test account."""
        self.update_from_dict(['project_id', 'card_number', 'passcode', 'attributes'],
                              test_account_info)
        self.commit()
