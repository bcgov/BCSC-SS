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
"""This tests OidcConfig model."""

from ..helper.request_data import factory_project_oidc_config
from .test_model_technical_req import create_technical_req

from selfservice_api.models.oidc_config import OIDCConfig


def test_create_from_dict(session):
    """Assert oidc config creation from the provided dictionary."""
    oidc_config = create_oidc_config(session)
    assert oidc_config.id is not None


def test_none_create_from_dict(session):
    """Assert skipping oidc config creation by providing None."""
    oidc_config = OIDCConfig.create_from_dict(oidc_config_info=None)
    assert oidc_config is None


def test_update(session):
    """Assert oidc config update from the provided dictionary."""
    oidc_config = create_oidc_config(session)
    oidc_config_info = factory_project_oidc_config()
    oidc_config_info['project_id'] = oidc_config.project_id
    oidc_config.update(oidc_config_info)
    assert oidc_config.id is not None


def test_find_by_project_id(session):
    """Assert oidc config instance that matches the provided id."""
    oidc_config = create_oidc_config(session)
    found = OIDCConfig.find_by_project_id(oidc_config.project_id, False)
    assert found is not None


def create_oidc_config(session):
    """Create oidc config and return project object."""
    technical_req = create_technical_req(session)
    oidc_config_info = factory_project_oidc_config()
    oidc_config_info['project_id'] = technical_req.project_id
    oidc_config = OIDCConfig.create_from_dict(oidc_config_info)
    session.add(oidc_config)
    session.commit()
    return oidc_config
