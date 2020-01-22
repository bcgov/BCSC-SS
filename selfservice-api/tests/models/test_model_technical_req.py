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
"""This tests Technical Requirement model."""

from ..helper.request_data import factory_project_technical_req
from .test_model_project import create_project

from selfservice_api.models.technical_req import TechnicalReq


def test_create_from_dict(session):
    """Assert technical_req creation from the provided dictionary."""
    technical_req = create_technical_req(session)
    assert technical_req.id is not None


def test_none_create_from_dict(session):
    """Assert skipping technical_req creation by providing None."""
    technical_req = TechnicalReq.create_from_dict(technical_req_info=None, oauth_id=None)
    assert technical_req is None


def test_find_by_id(session):
    """Assert technical_req instance that matches the provided id."""
    technical_req = create_technical_req(session)
    found = technical_req.find_by_id(technical_req.id)
    assert found is not None


def create_technical_req(session):
    """Create technical_req and return technical_req object."""
    project = create_project(session)
    technical_req_info = factory_project_technical_req(is_model=True)
    technical_req_info['project_id'] = project.id

    technical_req = TechnicalReq.create_from_dict(
        technical_req_info=technical_req_info, oauth_id=None)
    session.add(technical_req)
    session.commit()
    return technical_req
