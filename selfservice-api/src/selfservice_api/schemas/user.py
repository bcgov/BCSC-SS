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
"""This manages User Req/Res Schema."""

from marshmallow import EXCLUDE, Schema, fields, validate


class UserSchema(Schema):
    """This class manages user request and response schema."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Exclude unknown fields in the deserialized output."""

        unknown = EXCLUDE

    id = fields.Int()
    email = fields.Email(required=True, validate=validate.Length(min=5, max=250))
    phone = fields.Str(required=True, validate=validate.Length(max=15))
    first_name = fields.Str(data_key='firstName', required=True, validate=validate.Length(min=2, max=250))
    last_name = fields.Str(data_key='lastName', required=True, validate=validate.Length(min=2, max=250))
    oauth_id = fields.Str(data_key='oauthId', required=True, validate=validate.Length(min=3, max=100))
