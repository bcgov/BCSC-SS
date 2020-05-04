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
"""This manages Audit."""

from .base_enum import ExtendedEnum, ExtendedIntEnum


class AuditType(ExtendedEnum):
    """This enum provides the list of Audit Type."""

    Project = 'project'
    TechnicalReq = 'technical_req'
    ProjectUsersAssociation = 'project_users_association'
    TestAccount = 'test_account'
    OIDCConfig = 'oidc_config'


class ProjectSubType(ExtendedIntEnum):
    """This enum provides the list of Project Sub Type."""

    User = 1, 'User'
    Technical = 2, 'Technical Requirement'
    Package = 3, 'Data Package'
    TestAccount = 4, 'Test Account'
    DevOidc = 5, 'Development OIDC'
