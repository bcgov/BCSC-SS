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
"""This manages Project Req/Res Schema."""

from marshmallow import EXCLUDE, Schema, fields, validate

from ..models.enums.project import ProjectRoles
from .user import UserSchema


class ProjectUserSchema(Schema):
    """This class manages project users(developer,manager,cto) request and response schema."""

    id = fields.Int(load_only=True)
    email = fields.Email(load_only=True, validate=validate.Length(max=250))
    phone = fields.Str(load_only=True, validate=validate.Length(max=15))
    first_name = fields.Str(load_only=True, data_key='firstName', validate=validate.Length(max=250))
    last_name = fields.Str(load_only=True, data_key='lastName', validate=validate.Length(max=250))
    role = fields.Int(data_key='role', required=True, validate=validate.OneOf(list(map(int, ProjectRoles))))

    dump_id = fields.Pluck(UserSchema, field_name='id', dump_only=True, data_key='id', attribute='user')
    dump_email = fields.Pluck(UserSchema, field_name='email', dump_only=True, data_key='email', attribute='user')
    dump_phone = fields.Pluck(UserSchema, field_name='phone', dump_only=True, data_key='phone', attribute='user')
    dump_first_name = fields.Pluck(UserSchema, field_name='first_name', dump_only=True,
                                   data_key='firstName', attribute='user')
    dump_last_name = fields.Pluck(UserSchema, field_name='last_name', dump_only=True,
                                  data_key='lastName', attribute='user')


class ProjectSchema(Schema):
    """This class manages project request and response schema."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Exclude unknown fields in the deserialized output."""

        unknown = EXCLUDE

    id = fields.Int()
    organization_name = fields.Str(data_key='organizationName', required=True)
    project_name = fields.Str(data_key='projectName', required=True)
    description = fields.Str(required=True)
    my_role = fields.Int(data_key='myRole', required=True, validate=validate.OneOf(list(map(int, ProjectRoles))))

    users = fields.List(fields.Nested(ProjectUserSchema), data_key='users', required=True)
