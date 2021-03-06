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
"""This exports all of the schemas used by the application."""

from .contact_us import ContactUsSchema
from .oidc_config import OIDCConfigSchema
from .project import ProjectSchema
from .team import TeamSchema
from .technical_req import (TechnicalReqPackageSchema, TechnicalReqRequestSchema,  # noqa: I001
                            TechnicalReqResponseSchema, TechnicalReqTestAccountSchema)  # noqa: I001
from .test_account import TestAccountSchema
from .user import UserSchema
