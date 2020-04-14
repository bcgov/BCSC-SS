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
"""This exports all of the models used by the application."""

from .db import db, ma
from .email_queue import EmailQueue
from .org_whitelist import OrgWhitelist
from .user import User
from .project_users_association import ProjectUsersAssociation
from .project import Project
from .scope_package import ScopePackage
from .technical_req import TechnicalReq
from .oidc_config import OIDCConfig
from .test_account import TestAccount
