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
"""Exposes all of the resource endpoints mounted in Flask-Blueprint style.

Uses restplus namespaces to mount individual api endpoints into the service.
All services have 2 defaults sets of endpoints:
 - ops
 - meta
That are used to expose operational health information about the service, and meta information.
"""

from flask_jwt_oidc import AuthError
from flask_restplus import Api

from ..exceptions import BusinessException
from .contact_us import API as CONTACTUS_API
from .meta import API as META_API
from .oidc_config import API as OIDC_CONFIG_API
from .ops import API as OPS_API
from .project import API as PROJECT_API
from .scope_package import API as SCOPEPACKAGE_API
from .team import API as TEAM_API
from .technical_req import API as TECHNICALREQ_API
from .test_account import API as TESTACCOUNT_API
from .user import API as USER_API
from .values import API as VALUES_API


# This will add the Authorize button to the swagger docs
# oauth2 & openid may not yet be supported by restplus
AUTHORIZATIONS = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

API = Api(
    title='BC Services Card Self Service API',
    version='1.0',
    description='The API for the BC Services Card Application',
    prefix='/api/v1',
    security=['apikey'],
    authorizations=AUTHORIZATIONS)


@API.errorhandler(BusinessException)
def handle_business_exception(error: BusinessException):
    """Handle Business exception."""
    return {'message': error.error}, error.status_code


@API.errorhandler(AuthError)
def handle_auth_error(error: AuthError):
    """Handle Business exception."""
    return {'message': 'Access Denied'}, error.status_code


API.add_namespace(OPS_API, path='/ops')
API.add_namespace(META_API, path='/meta')
API.add_namespace(CONTACTUS_API, path='/contactus')
API.add_namespace(USER_API, path='/user')
API.add_namespace(PROJECT_API, path='/project/info')
API.add_namespace(TEAM_API, path='/project/<int:project_id>/team')
API.add_namespace(TECHNICALREQ_API, path='/project/<int:project_id>/technical-req')
API.add_namespace(VALUES_API, path='/values')
API.add_namespace(SCOPEPACKAGE_API, path='/scope-package')
API.add_namespace(OIDC_CONFIG_API, path='/project/<int:project_id>/oidc-config')
API.add_namespace(TESTACCOUNT_API, path='/test-account')
