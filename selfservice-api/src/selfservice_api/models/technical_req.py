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
"""This manages Technical Req Data."""

from .audit_mixin import AuditDateTimeMixin, AuditUserMixin
from .db import db


class TechnicalReq(AuditDateTimeMixin, AuditUserMixin, db.Model):  # pylint: disable=too-few-public-methods
    """This class manages technical requirement information."""

    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=True)
    client_uri = db.Column(db.String(500), nullable=True)
    redirect_uris = db.Column(db.JSON(), nullable=True)
    jwks_uri = db.Column(db.String(500), nullable=True)
    id_token_signed_response_alg = db.Column(db.String(10), nullable=True)
    userinfo_signed_response_alg = db.Column(db.String(10), nullable=True)
    scope_package_id = db.Column(db.Integer, db.ForeignKey('scope_package.id'), nullable=True)
