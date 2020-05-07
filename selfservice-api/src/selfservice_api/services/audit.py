# Copyright © 2020 Province of British Columbia
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
"""This manages Audit Service."""

from ..models import Audit, Project, User, db
from ..models.enums import AuditType, ProjectStatus


class AuditService():
    """Service to manage Audit log."""

    @classmethod
    def log_project_status_change(cls, project: Project, user: User):
        """Log project status change after save."""
        audit = Audit()
        audit.audit_type = AuditType.Project.value  # pylint: disable=E1101
        audit.audit_type_id = project.id
        audit.sub_type = None
        audit.sub_type_id = None
        audit.field = 'status'
        audit.old_value = None if project.status == ProjectStatus.Draft else project.status - 1
        audit.new_value = project.status
        audit.created_by = user.id
        audit.save()

    @classmethod
    def log(cls, audit_type: AuditType, old_model, model, user: User):
        """Compare and log changes from model."""
        for field in cls.__get_valid_fields__(model):
            old_value = getattr(old_model, field, None)
            value = getattr(model, field, None)
            if old_value != value:
                audit = Audit()
                audit.audit_type = audit_type.value
                audit.audit_type_id = model.id
                audit.sub_type = None
                audit.sub_type_id = None
                audit.field = field
                audit.old_value = old_value
                audit.new_value = value
                audit.created_by = user.id
                db.session.add(audit)

        db.session.commit()

    @staticmethod
    def __get_valid_fields__(model):
        """Get list of valid fields for the specific Audit Type."""
        fields = model.__table__.columns.keys()
        if 'created' in fields:
            fields.remove('created')
        if 'modified' in fields:
            fields.remove('modified')
        if 'created_by' in fields:
            fields.remove('created_by')
        if 'modified_by' in fields:
            fields.remove('modified_by')

        return fields
