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
"""This manages Project Enums."""

from .base_enum import ExtendedIntEnum


class ProjectRoles(ExtendedIntEnum):
    """This enum provides the list of Project Roles."""

    Developer = 1, 'Developer'
    Manager = 2, 'Manager'
    Cto = 3, 'Executive Sponsor'


class ProjectStatus(ExtendedIntEnum):
    """This enum provides the list of Project Status."""

    Draft = 1, 'Draft'
    Development = 2, 'Development'
    DevelopmentComplete = 3, 'Development Complete'
    ComplianceChecks = 4, 'Compliance Checks'
    AwaitingApproval = 5, 'Awaiting Approval'
    PrepareProdTechConfig = 6, 'Prepare Prod Tech Config'
    RequireIDIMEDApproval = 7, 'Require IDIM ED Approval'
    ApprovalGranted = 8, 'Approval Granted'
