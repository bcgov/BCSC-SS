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

from .audit_mixin import AuditDateTimeMixin, AuditUserMixin
from .base_model import BaseModel
from .db import db
from .enums.project import ProjectStatus
from .user import User


class ProjectUsersAssociation(BaseModel, db.Model):
    """This class manages project and user association."""

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', lazy=True, backref=db.backref('projects', lazy=True))
    project = db.relationship('Project', lazy=True, backref=db.backref('users', lazy='subquery'))


class Project(AuditDateTimeMixin, AuditUserMixin, BaseModel, db.Model):
    """This class manages project information."""

    id = db.Column(db.Integer, primary_key=True)
    organization_name = db.Column(db.String(100), nullable=False)
    project_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(), nullable=False)

    status = db.Column(db.Integer(), nullable=False)

    technical_req = db.relationship('TechnicalReq', backref='project', lazy=True)

    @classmethod
    def create_from_dict(cls, project_info: dict, oauth_id: str) -> Project:
        """Create a new project from the provided dictionary and current user oauth id."""
        if project_info:
            current_user = User.find_by_oauth_id(oauth_id)

            project = Project()
            project.organization_name = project_info['organization_name']
            project.project_name = project_info['project_name']
            project.description = project_info['description']
            project.created_by = current_user.id
            project.status = ProjectStatus.Draft
            project.save()

            project.__create_or_map_users__(project_info)
            project.__create_association__(current_user.id, project_info['my_role'])

            return project
        return None

    def __create_or_map_users__(self, project_info: dict):
        """Create or map the users of project."""
        for project_user in project_info['users']:
            user = User.find_by_email(project_user['email'])
            if user is None:
                user = User.create_from_dict(project_user)
            self.__create_association__(user.id, project_user['role'])

    def __create_association__(self, user_id, role):
        """Create an association between user and project."""
        association = ProjectUsersAssociation()
        association.user_id = user_id
        association.project_id = self.id
        association.role = role
        association.save()

    @classmethod
    def find_by_id(cls, project_id) -> Project:
        """Find project that matches the provided id."""
        return cls.query.filter_by(id=project_id).first()

    def update_status(self, oauth_id: str, project_status: int):
        """Update project status."""
        current_user = User.find_by_oauth_id(oauth_id)
        project_info = {'modified_by': current_user.id, 'status': project_status}
        self.update_from_dict(['modified_by', 'status'], project_info)
        self.commit()
