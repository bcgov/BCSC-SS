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
"""This tests Audit model."""

from selfservice_api.models import Audit
from selfservice_api.models.enums import AuditType


def test_create_from_dict(session):
    """Assert audit creation from dict."""
    Audit.create_from_dict({
        'audit_type': AuditType.Project,
        'field': 'test_field',
        'new_value': '123456',
        'created_by': '1'
    })


def test_none_create_from_dict(session):
    """Assert skipping audit creation by providing None."""
    Audit.create_from_dict(None)


def test_create_from_list(session):
    """Assert audit creation from list."""
    Audit.create_from_list([{
        'audit_type': AuditType.Project,
        'field': 'test_field',
        'new_value': '123456',
        'created_by': '1'
    }])


def test_none_create_from_list(session):
    """Assert skipping audit creation by providing None."""
    Audit.create_from_list(None)
