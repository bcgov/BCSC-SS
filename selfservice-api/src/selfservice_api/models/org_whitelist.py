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
"""This manages Orginasition Whitelist."""

from .audit_mixin import AuditDateTimeMixin
from .db import db


class OrgWhitelist(AuditDateTimeMixin, db.Model):  # pylint: disable=too-few-public-methods
    """This class manages whitelisted Orginasition."""

    __tablename__ = 'org_whitelist'
    id = db.Column(db.Integer, primary_key=True)
    org_name = db.Column('org_name', db.String(250), nullable=False)
    head_of_org = db.Column('head_of_org', db.String(250), nullable=False)
    domain = db.Column('domain', db.String(50), nullable=False)
