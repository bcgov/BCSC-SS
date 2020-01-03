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

import datetime

from sqlalchemy import Column, DateTime, Integer, String

from .db import db


class OrgWhitelist(db.Model):
    """This class manages whitelisted Orginasition."""

    __tablename__ = 'org_whitelist'
    id = Column(Integer, primary_key=True)
    org_name = Column('org_name', String(250), nullable=False)
    head_of_org = Column('head_of_org', String(250), nullable=False)
    domain = Column('domain', String(50), nullable=False)
    created = Column(DateTime, default=datetime.datetime.now)
    modified = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
