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
"""This manages Audit Mixin for models."""

import datetime

from .db import db


class AuditDateTimeMixin():  # pylint: disable=too-few-public-methods
    """Inherit this class to extend the model with created and modified column."""

    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    modified = db.Column(db.DateTime, onupdate=datetime.datetime.now)


class AuditUserMixin():  # pylint: disable=too-few-public-methods
    """Inherit this class to extend the model with created_by and modified_by column."""

    created_by = db.Column(db.String(), nullable=False)
    modified_by = db.Column(db.String(), nullable=True)
