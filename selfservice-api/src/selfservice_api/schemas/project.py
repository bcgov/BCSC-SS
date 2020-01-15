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


class ProjectUserSchema(Schema):
    """This class manages project users(developer,manager,cto) request schema."""

    id = fields.Int()
    email = fields.Email(validate=validate.Length(max=250))
    phone = fields.Str(validate=validate.Length(max=15))
    first_name = fields.Str(data_key='firstName', validate=validate.Length(max=250))
    last_name = fields.Str(data_key='lastName', validate=validate.Length(max=250))


class ProjectRequestSchema(Schema):
    """This class manages project request schema."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Exclude unknown fields in the deserialized output."""

        unknown = EXCLUDE

    id = fields.Int()
    organization_name = fields.Str(data_key='organizationName', required=True)
    project_name = fields.Str(data_key='projectName', required=True)
    description = fields.Str(required=True)
    my_role = fields.Int(data_key='myRole', required=True, validate=validate.OneOf(list(map(int, ProjectRoles))))

    developer = fields.Nested(ProjectUserSchema, data_key='developerDetails')
    manager = fields.Nested(ProjectUserSchema, data_key='managerDetails')
    cto = fields.Nested(ProjectUserSchema, data_key='ctoDetails')
