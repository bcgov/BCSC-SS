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
"""This tests Project model."""

from ..helper.request_data import factory_project_info
from .test_model_user import create_user

from selfservice_api.models.project import Project


def test_create_from_dict(session):
    """Assert project creation from the provided dictionary."""
    project = create_project(session)
    assert project.id is not None


def test_none_create_from_dict(session):
    """Assert skipping project creation by providing None."""
    project = Project.create_from_dict(project_info=None, oauth_id=None)
    assert project is None


def test_find_by_id(session):
    """Assert project instance that matches the provided id."""
    project = create_project(session)
    found = project.find_by_id(project.id)
    assert found is not None


def create_project(session):
    """Create project and return project object."""
    user = create_user(session)
    project_info = factory_project_info(is_model=True)

    project = Project.create_from_dict(
        project_info=project_info, oauth_id=user.oauth_id)
    session.add(project)
    session.commit()
    return project
