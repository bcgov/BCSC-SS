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
from .enums.project import ProjectRoles, ProjectStatus
from .user import User


class Project(AuditDateTimeMixin, AuditUserMixin, BaseModel, db.Model):
    """This class manages project information."""

    id = db.Column(db.Integer, primary_key=True)
    organization_name = db.Column(db.String(100), nullable=False)
    project_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    my_role = db.Column(db.Integer(), nullable=False)

    developer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    manager_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    cto_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    developer = db.relationship('User', foreign_keys='Project.developer_id',
                                backref='Project', lazy=True)
    manager = db.relationship('User', foreign_keys='Project.manager_id',
                              backref='Project', lazy=True)
    cto = db.relationship('User', foreign_keys='Project.cto_id',
                          backref='Project', lazy=True)

    status = db.Column(db.Integer(), nullable=False)

    @classmethod
    def create_from_dict(cls, project_info: dict) -> Project:
        """Create a new project from the provided dictionary."""
        if project_info:
            project = Project()
            project.organization_name = project_info['organization_name']
            project.project_name = project_info['project_name']
            project.description = project_info['description']
            project.my_role = project_info['my_role']

            project.created_by = project.__create_or_map_users__(project_info)
            project.status = ProjectStatus.DevInProgress

            project.save()

            return project
        return None

    def __create_or_map_users__(self, project_info: dict):
        """Create or map the users of project.

        :return : current user id
        """
        current_user = User.find_by_oauth_id(project_info['oauth_id'])

        if project_info['my_role'] != ProjectRoles.Developer:
            developer_user = User.find_by_email(project_info['developer_details']['email'])
            if developer_user is None:
                developer_user = User.create_from_dict(project_info['developer_details'])
            self.developer_id = developer_user.id
        else:
            self.developer_id = current_user.id

        if project_info['my_role'] != ProjectRoles.Manager:
            manager_user = User.find_by_email(project_info['manager_details']['email'])
            if manager_user is None:
                manager_user = User.create_from_dict(project_info['manager_details'])
            self.manager_id = manager_user.id
        else:
            self.manager_id = current_user.id

        if project_info['my_role'] != ProjectRoles.Cto:
            cto_user = User.find_by_email(project_info['cto_details']['email'])
            if cto_user is None:
                cto_user = User.create_from_dict(project_info['cto_details'])
            self.cto_id = cto_user.id
        else:
            self.cto_id = current_user.id

        return current_user.id

    @classmethod
    def find_by_id(cls, id) -> Project:
        """Find project that matches the provided id."""
        return cls.query.filter_by(id=id).first()
