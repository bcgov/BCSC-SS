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
"""This manages User Data."""

from __future__ import annotations

from .audit_mixin import AuditDateTimeMixin
from .base_model import BaseModel
from .db import db


class User(AuditDateTimeMixin, BaseModel, db.Model):
    """This class manages user information."""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    oauth_id = db.Column(db.String(100), nullable=True)

    developer_projects = db.relationship('ProjectInfo', foreign_keys='ProjectInfo.developer_id',
                                         backref='developer', lazy=True)
    manager_projects = db.relationship('ProjectInfo', foreign_keys='ProjectInfo.manager_id',
                                       backref='manager', lazy=True)
    cto_projects = db.relationship('ProjectInfo', foreign_keys='ProjectInfo.cto_id',
                                   backref='cto', lazy=True)

    @classmethod
    def create_from_dict(cls, user_info: dict) -> User:
        """Create a new user from the provided dictionary."""
        if user_info:
            user = User()
            user.email = user_info['email']
            user.phone = user_info['phone']
            user.first_name = user_info['first_name']
            user.last_name = user_info['last_name']
            user.oauth_id = user_info.get('oauth_id')

            user.save()

            return user
        return None

    @classmethod
    def find_by_email(cls, email) -> User:
        """Find user instance that matches the email."""
        return cls.query.filter(User.email == email).first()

    @classmethod
    def find_by_oauth_id(cls, oauth_id) -> User:
        """Find user instance that matches the provided id."""
        return cls.query.filter_by(oauth_id=oauth_id).first()

    @classmethod
    def find_by_id(cls, user_id) -> User:
        """Find user instance that matches the provided id."""
        return cls.query.filter_by(id=user_id).first()
