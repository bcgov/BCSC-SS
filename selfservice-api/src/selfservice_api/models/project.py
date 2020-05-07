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
"""This manages Project Info Data."""

from __future__ import annotations

from sqlalchemy import and_

from .audit_mixin import AuditDateTimeMixin, AuditUserMixin
from .base_model import BaseModel
from .db import db
from .enums.project import ProjectRoles, ProjectStatus
from .user import User


class Project(AuditDateTimeMixin, AuditUserMixin, BaseModel, db.Model):
    """This class manages project information."""

    id = db.Column(db.Integer, primary_key=True)
    organization_name = db.Column(db.String(100), nullable=False)
    project_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    ref_no = db.Column(db.String(20), nullable=True)

    status = db.Column(db.Integer(), nullable=False)
    oidc_dev_date = db.Column(db.DateTime, nullable=True)
    oidc_prod_date = db.Column(db.DateTime, nullable=True)

    is_deleted = db.Column(db.Boolean(), default=False, nullable=False)

    technical_req = db.relationship('TechnicalReq', backref='project', lazy=True)

    @classmethod
    def create_from_dict(cls, project_info: dict, user: User) -> Project:
        """Create a new project from the provided dictionary and current user oauth id."""
        if project_info:
            project = Project()
            project.organization_name = project_info['organization_name']
            project.project_name = project_info['project_name']
            project.description = project_info['description']
            project.created_by = user.id
            project.status = ProjectStatus.Draft
            project.save()
            return project
        return None

    def update(self, project_info: dict, user: User):
        """Update project."""
        project_info['modified_by'] = user.id
        self.update_from_dict(['modified_by', 'organization_name', 'project_name', 'description', 'is_deleted'],
                              project_info)
        self.commit()

    def update_status(self, project_status: int, user: User):
        """Update project status."""
        project_info = {'modified_by': user.id, 'status': project_status}
        self.update_from_dict(['modified_by', 'status'], project_info)
        self.commit()

    @classmethod
    def find_by_id(cls, project_id, is_deleted=False) -> Project:
        """Find project that matches the provided id."""
        return cls.query.filter(and_(Project.id == project_id, Project.is_deleted == is_deleted)).first()

    @classmethod
    def find_all_or_by_user(cls, user: User = None):
        """Fetch all projects or by user."""
        if user is not None:
            result_proxy = db.session.execute("""SELECT
                    TO_CHAR(project.created, 'Mon dd yyyy') as created,
                    project.id,
                    project.project_name as name,
                    project.status,
                    project.ref_no as reference,
                    project_users_association.role
                FROM project
                    JOIN project_users_association ON project.id = project_users_association.project_id
                WHERE
                    project.is_deleted = false AND
                    project_users_association.user_id = """ + str(user.id) + ' ORDER BY project.created DESC')
        else:
            result_proxy = db.session.execute("""SELECT
                    TO_CHAR(project.created, 'Mon dd yyyy') as created,
                    project.id,
                    project.project_name as name,
                    project.status,
                    project.ref_no as reference
                FROM project
                WHERE
                    project.is_deleted = false
                ORDER BY project.created DESC""")

        result = []
        for row in result_proxy:
            info = dict(row)

            info['statusId'] = info['status']
            info['status'] = ProjectStatus.get_phrase(info['status'])
            if user is not None:
                info['role'] = ProjectRoles.get_phrase(info['role'])

            result.append(info)

        return result
