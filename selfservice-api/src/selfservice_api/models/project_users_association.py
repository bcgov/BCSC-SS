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
"""This manages Project User Association Data."""

from __future__ import annotations

from sqlalchemy import and_

from .base_model import BaseModel
from .db import db
from .enums.project import ProjectRoles
from .user import User


class ProjectUsersAssociation(BaseModel, db.Model):
    """This class manages project and user association."""

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', lazy=True, backref=db.backref('projects', lazy=True))
    project = db.relationship('Project', lazy=True, backref=db.backref('users', lazy='subquery'))

    @classmethod
    def create_from_dict(cls, user_info: dict, project_id) -> ProjectUsersAssociation:
        """Create an association between user and project from dict."""
        user = cls.__create_or_update_user__(user_info)
        return cls.create(user.id, project_id, user_info['role'])

    @classmethod
    def create(cls, user_id, project_id, role: ProjectRoles) -> ProjectUsersAssociation:
        """Create an association between user and project."""
        association = ProjectUsersAssociation()
        association.user_id = user_id
        association.project_id = project_id
        association.role = role
        association.save()
        return association

    def update(self, user_info: dict, only_role=False):
        """Update an association between user and project.

        `only_role`: if `True` only role will be updated in association.
        """
        if not only_role:
            user = self.__create_or_update_user__(user_info)
            self.user_id = user.id
        self.role = user_info['role']
        self.commit()

    @staticmethod
    def __create_or_update_user__(user_info: dict):
        """Create or update a user."""
        user = User.find_by_email(user_info['email'])
        if user is None:
            user = User.create_from_dict(user_info)
        elif user.oauth_id is None:
            user.update(user_info)

        return user

    @classmethod
    def check_user_existence(cls, project_id: str, email: str, association_id: str = None):
        """Check existence of user in a project."""
        user = User.find_by_email(email)
        if user:
            association = cls.query.filter(and_(ProjectUsersAssociation.project_id == project_id,
                                                ProjectUsersAssociation.user_id == user.id)).first()
            is_exist = association is not None

            if association_id and association and association_id == association.id:
                is_exist = False

            return is_exist
        return False

    @classmethod
    def check_role_existence(cls, project_id: str, role: str, association_id: str = None):
        """Check existence of role in a project."""
        association = cls.query.filter(and_(ProjectUsersAssociation.project_id == project_id,
                                            ProjectUsersAssociation.role == role)).first()
        is_exist = association is not None

        if association_id and association and association_id == association.id:
            is_exist = False

        return is_exist

    @classmethod
    def delete_by_id(cls, association_id: str):
        """Delete association by id."""
        association: ProjectUsersAssociation = cls.query.filter_by(id=association_id).first()
        if association:
            association.delete()

    @classmethod
    def find_by_id(cls, association_id: str) -> ProjectUsersAssociation:
        """Find by id."""
        return cls.query.filter_by(id=association_id).first()

    @classmethod
    def find_all_by_project_id(cls, project_id: str):
        """Find all by project id."""
        return cls.query.filter(ProjectUsersAssociation.project_id == project_id).all()

    @classmethod
    def find_all_by_project_and_user_id(cls, project_id: str, user_id: str) -> ProjectUsersAssociation:
        """Find all association by project id and user id."""
        return cls.query.filter(and_(ProjectUsersAssociation.project_id == project_id,
                                     ProjectUsersAssociation.user_id == user_id)).all()

    @classmethod
    def delete_all_by_project_id(cls, project_id: str):
        """Delete all by project id."""
        return cls.query.filter(ProjectUsersAssociation.project_id == project_id).delete()
