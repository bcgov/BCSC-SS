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
"""This manages Audit."""

import datetime

from .base_model import BaseModel
from .db import db


class Audit(BaseModel, db.Model):  # pylint: disable=too-few-public-methods
    """This class manages audit."""

    __tablename__ = 'audit'
    id = db.Column(db.Integer, primary_key=True)
    audit_type = db.Column('audit_type', db.String(), nullable=False)
    audit_type_id = db.Column('audit_type_id', db.String(), nullable=True)
    sub_type = db.Column('sub_type', db.String(), nullable=True)
    sub_type_id = db.Column('sub_type_id', db.String(), nullable=True)
    field = db.Column('field', db.String(), nullable=False)
    old_value = db.Column('old_value', db.String(), nullable=True)
    new_value = db.Column('new_value', db.String(), nullable=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    created_by = db.Column(db.String(), nullable=False)

    @classmethod
    def create_from_dict(cls, audit_info: dict):
        """Create audit from the dict."""
        if audit_info:
            audit = Audit()
            audit.audit_type = audit_info['audit_type']
            audit.audit_type_id = audit_info.get('audit_type_id')
            audit.sub_type = audit_info.get('sub_type')
            audit.sub_type_id = audit_info.get('sub_type_id')
            audit.field = audit_info['field']
            audit.old_value = audit_info.get('old_value')
            audit.new_value = audit_info['new_value']
            audit.created_by = audit_info['created_by']
            audit.save()

    @classmethod
    def create_from_list(cls, audit_list: list):
        """Create audit from the list."""
        if audit_list:
            for info in audit_list:
                cls.create_from_dict(info)

    @classmethod
    def find_project_status(cls, project_id):
        """Find project audit status."""
        result_proxy = db.session.execute("""
            SELECT
                audit.new_value as "status",
                TO_CHAR(audit.created, 'Mon dd yyyy') as "created",
                "user".first_name || ' ' || "user".last_name as "name",
                project_users_association.role
            FROM audit
                INNER JOIN "user" on "user".id = audit.created_by::integer
                INNER JOIN project_users_association on project_users_association.user_id = "user".id and
                            project_users_association.project_id = '""" + str(project_id) + """'
            WHERE
                audit.field = 'status' and
                audit.audit_type = 'project' and
                audit.audit_type_id = '""" + str(project_id) + """'
            ORDER BY audit.created""")

        result = []
        for row in result_proxy:
            info = dict(row)

            info['status'] = int(info['status'])
            info['role'] = int(info['role'])

            result.append(info)

        return result
