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
"""This manages Scope Package Data."""

from .db import db


class ScopePackage(db.Model):  # pylint: disable=too-few-public-methods
    """This class manages scope and packages information."""

    id = db.Column(db.Integer, primary_key=True)
    package_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    claim_names = db.Column(db.JSON, nullable=False)
    scope = db.Column(db.String(100), nullable=False)

    technical_req = db.relationship('TechnicalReq', backref='scope_package', lazy=True)

    @classmethod
    def find_all(cls):
        """Fetch all scope packages."""
        return cls.query.all()
