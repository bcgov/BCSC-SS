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
"""This manages Email Queue."""

from .audit_mixin import AuditDateTimeMixin, AuditUserMixin
from .base_model import BaseModel
from .db import db


class EmailQueue(AuditDateTimeMixin, AuditUserMixin, BaseModel, db.Model):  # pylint: disable=too-few-public-methods
    """This class manages email queue."""

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column('subject', db.String(), nullable=False)
    recipients = db.Column('recipients', db.JSON(), nullable=False)
    body = db.Column('body', db.String(), nullable=False)
    sender = db.Column('sender', db.String(), nullable=False)
    cc = db.Column('cc', db.JSON(), nullable=True)  # pylint: disable=invalid-name
    bcc = db.Column('bcc', db.JSON(), nullable=True)
    email_type = db.Column('email_type', db.String(), nullable=False)
