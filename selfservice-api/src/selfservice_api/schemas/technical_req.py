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
"""This manages Technical Requirement Req/Res Schema."""

from marshmallow import EXCLUDE, Schema, fields, validate


class TechnicalReqRequestSchema(Schema):
    """This class manages technical requirement request schema."""

    unknown = EXCLUDE

    id = fields.Int()
    client_name = fields.Str(data_key='clientName', validate=validate.Length(max=100))
    client_uri = fields.Str(data_key='clientUri', validate=validate.Length(max=500))
    redirect_uris = fields.Dict(data_key='redirectUris')
    jwks_uri = fields.Str(data_key='jwksUri', validate=validate.Length(max=500))
    id_token_signed_response_alg = fields.Str(data_key='idTokenSignedResponseAlg', validate=validate.Length(max=10))
    userinfo_signed_response_alg = fields.Str(data_key='userinfoSignedResponseAlg', validate=validate.Length(max=10))
