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
"""This manages OIDC Config Data."""

from __future__ import annotations

from .base_model import BaseModel
from .db import db


class OIDCConfig(BaseModel, db.Model):
    """This class manages oidc config information."""

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

    client_id = db.Column(db.String(100))
    client_secret = db.Column(db.String(500))

    registration_access_token = db.Column(db.String(5000))
    registration_client_uri = db.Column(db.String(500))

    client_id_issued_at = db.Column(db.String(100))
    client_secret_expires_at = db.Column(db.String(100))

    token_endpoint_auth_method = db.Column(db.String(100))

    application_type = db.Column(db.String(100))
    subject_type = db.Column(db.String(100))

    is_prod = db.Column(db.Boolean(), default=False)

    @classmethod
    def create_from_dict(cls, oidc_config_info: dict) -> OIDCConfig:
        """Create a new oidc config from the provided dictionary."""
        if oidc_config_info:
            oidc_config = OIDCConfig()
            oidc_config.project_id = oidc_config_info['project_id']
            oidc_config.client_id = oidc_config_info['client_id']
            oidc_config.client_secret = oidc_config_info['client_secret']
            oidc_config.registration_access_token = oidc_config_info['registration_access_token']
            oidc_config.registration_client_uri = oidc_config_info['registration_client_uri']
            oidc_config.client_id_issued_at = oidc_config_info['client_id_issued_at']
            oidc_config.client_secret_expires_at = oidc_config_info['client_secret_expires_at']
            oidc_config.token_endpoint_auth_method = oidc_config_info['token_endpoint_auth_method']
            oidc_config.application_type = oidc_config_info['application_type']
            oidc_config.subject_type = oidc_config_info['subject_type']
            oidc_config.is_prod = oidc_config_info['is_prod']
            oidc_config.save()

            return oidc_config
        return None

    @classmethod
    def find_by_project_id(cls, project_id, is_prod: bool) -> OIDCConfig:
        """Find oidc config that matches the provided id."""
        return cls.query.filter(OIDCConfig.project_id == project_id and
                                OIDCConfig.is_prod == is_prod).first()

    def update(self, oidc_config_info: dict):
        """Update oidc config."""
        self.update_from_dict(['project_id', 'client_id', 'client_secret', 'registration_access_token',
                               'registration_client_uri', 'client_id_issued_at', 'client_secret_expires_at',
                               'token_endpoint_auth_method', 'application_type', 'subject_type'],
                              oidc_config_info)
        self.commit()

    @classmethod
    def delete_by_project_id(cls, project_id):
        """Delete oidc config that matches the provided id."""
        return cls.query.filter(OIDCConfig.project_id == project_id).delete()
