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
"""This manages LoginHistory."""

import datetime

from .base_model import BaseModel
from .db import db


class LoginHistory(BaseModel, db.Model):  # pylint: disable=too-few-public-methods
    """This class manages LoginHistory."""

    __tablename__ = 'login_history'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(), nullable=False)
    logged_in = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)

    @classmethod
    def log(cls, user_id):
        """Create login history."""
        if user_id:
            history = LoginHistory()
            history.user_id = user_id
            history.save()
