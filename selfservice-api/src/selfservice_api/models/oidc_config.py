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
    client_secret = db.Column(db.String(100), nullable=True)

    registration_access_token = db.Column(db.String(100))
    registration_client_uri = db.Column(db.String(500))

    client_id_issued_at = db.Column(db.String(100))
    client_secret_expires_at = db.Column(db.Integer)

    token_endpoint_auth_method = db.Column(db.String(100))

    application_type = db.Column(db.String(100))
    subject_type = db.Column(db.String(100))

    sector_identifier_uri = db.Column(db.String(500))

    id_token_encrypted_response_alg = db.Column(db.String(100))
    id_token_encrypted_response_enc = db.Column(db.String(100))

    userinfo_encrypted_response_alg = db.Column(db.String(100))
    userinfo_encrypted_response_enc = db.Column(db.String(100))

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
            oidc_config.sector_identifier_uri = oidc_config_info['sector_identifier_uri']
            oidc_config.id_token_encrypted_response_alg = \
                oidc_config_info['id_token_encrypted_response_alg']
            oidc_config.id_token_encrypted_response_enc = \
                oidc_config_info['id_token_encrypted_response_enc']
            oidc_config.userinfo_encrypted_response_alg = \
                oidc_config_info['userinfo_encrypted_response_alg']
            oidc_config.userinfo_encrypted_response_enc = \
                oidc_config_info['userinfo_encrypted_response_enc']

            oidc_config.save()

            return oidc_config
        return None

    @classmethod
    def find_by_project_id(cls, project_id) -> OIDCConfig:
        """Find oidc config that matches the provided id."""
        return cls.query.filter(OIDCConfig.project_id == project_id).first()

    def update(self, oidc_config_info: dict):
        """Update oidc config."""
        self.update_from_dict(['project_id', 'client_id', 'client_secret', 'registration_access_token',
                               'registration_client_uri', 'client_id_issued_at', 'client_secret_expires_at',
                               'token_endpoint_auth_method', 'application_type', 'subject_type',
                               'sector_identifier_uri', 'id_token_encrypted_response_alg',
                               'id_token_encrypted_response_enc', 'userinfo_encrypted_response_alg',
                               'userinfo_encrypted_response_enc'],
                              oidc_config_info)
        self.commit()
