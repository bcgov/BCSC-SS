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
"""This manages Technical Requirement Data."""

from __future__ import annotations

from .audit_mixin import AuditDateTimeMixin, AuditUserMixin
from .base_model import BaseModel
from .db import db
from .user import User


class TechnicalReq(AuditDateTimeMixin, AuditUserMixin, BaseModel, db.Model):  # pylint: disable=too-few-public-methods
    """This class manages technical requirement information."""

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

    client_uri = db.Column(db.String(500), nullable=True)
    redirect_uris = db.Column(db.JSON(), nullable=True)
    jwks_uri = db.Column(db.String(500), nullable=True)
    id_token_signed_response_alg = db.Column(db.String(10), nullable=True)
    userinfo_signed_response_alg = db.Column(db.String(10), nullable=True)

    scope_package_id = db.Column(db.Integer, db.ForeignKey('scope_package.id'), nullable=True)

    @classmethod
    def create_from_dict(cls, technical_req_info: dict, oauth_id: str) -> TechnicalReq:
        """Create a new technical requirement from the provided dictionary."""
        if technical_req_info:
            technical_req = TechnicalReq()
            technical_req.project_id = technical_req_info['project_id']
            technical_req.client_uri = technical_req_info['client_uri']
            technical_req.redirect_uris = technical_req_info['redirect_uris']
            technical_req.jwks_uri = technical_req_info['jwks_uri']
            technical_req.id_token_signed_response_alg = technical_req_info['id_token_signed_response_alg']
            technical_req.userinfo_signed_response_alg = technical_req_info['userinfo_signed_response_alg']

            current_user = User.find_by_oauth_id(oauth_id)
            technical_req.created_by = current_user.id

            technical_req.save()

            return technical_req
        return None

    @classmethod
    def find_by_id(cls, id) -> TechnicalReq:
        """Find technical requirement that matches the provided id."""
        return cls.query.filter_by(id=id).first()