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

from marshmallow import EXCLUDE, Schema, ValidationError, fields, validate, validates_schema

from ..models.enums import Algorithms, SigningEncryptionType


class TechnicalReqRequestSchema(Schema):
    """This class manages technical requirement request schema."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Exclude unknown fields in the deserialized output."""

        unknown = EXCLUDE

    id = fields.Int()
    project_id = fields.Int(data_key='projectId')
    client_uri = fields.Str(data_key='clientUri', required=True, validate=validate.Length(min=10, max=500))
    redirect_uris = fields.List(fields.String(validate=validate.Length(min=10)),
                                data_key='redirectUris', required=True, validate=validate.Length(min=1))
    jwks_uri = fields.Str(data_key='jwksUri', required=False, validate=validate.Length(max=500), allow_none=True)

    id_token_signed_response_alg = fields.Str(load_only=True, data_key='signedResponseAlg', allow_none=True)
    userinfo_signed_response_alg = fields.Str(load_only=True, data_key='signedResponseAlg', allow_none=True)
    id_token_encrypted_response_alg = fields.Str(load_only=True, data_key='encryptedResponseAlg', allow_none=True)
    userinfo_encrypted_response_alg = fields.Str(load_only=True, data_key='encryptedResponseAlg', allow_none=True)

    signing_encryption_type = fields.Int(data_key='signingEncryptionType', required=True,
                                         validate=validate.OneOf(list(map(int, SigningEncryptionType))))

    # Since the discussion of Encryption and Signing continues dumping is changed. May change on upcoming sprint's.
    dump_signed_response_alg = fields.Str(dump_only=True, data_key='signedResponseAlg',
                                          attribute='id_token_signed_response_alg')
    dump_encrypted_response_alg = fields.Str(dump_only=True, data_key='encryptedResponseAlg',
                                             attribute='id_token_encrypted_response_alg')

    @validates_schema
    def validate_and_set_algorithm(self, data, **kwargs):  # pylint: disable=no-self-use
        """Validate fields based on signing_encryption_type."""
        if data['signing_encryption_type'] == SigningEncryptionType.SecureJWT:
            errors = {}
            if data['id_token_signed_response_alg'] not in Algorithms.list():
                errors['signedResponseAlg'] = 'signedResponseAlg is required.'
            if data['id_token_encrypted_response_alg'] not in Algorithms.list():
                errors['encryptedResponseAlg'] = 'encryptedResponseAlg is required.'
            if data['jwks_uri'] is None or len(data['jwks_uri'].strip()) <= 0:
                errors['jwksUri'] = 'jwksUri is required.'
            if errors:
                raise ValidationError(errors)
        elif data['signing_encryption_type'] == SigningEncryptionType.SignedJWT:
            errors = {}
            if data['id_token_signed_response_alg'] not in Algorithms.list():
                errors['signedResponseAlg'] = 'signedResponseAlg is required.'
            if errors:
                raise ValidationError(errors)

            data['id_token_encrypted_response_alg'] = data['userinfo_encrypted_response_alg'] = None
            data['jwks_uri'] = ''
        else:
            data['id_token_signed_response_alg'] = data['userinfo_signed_response_alg'] = None
            data['id_token_encrypted_response_alg'] = data['userinfo_encrypted_response_alg'] = None
            data['jwks_uri'] = ''


class TechnicalReqPackageSchema(Schema):
    """This class manages technical requirement request schema."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Exclude unknown fields in the deserialized output."""

        unknown = EXCLUDE

    scope_package_id = fields.Int(data_key='scopePackageId', required=True)


class TechnicalReqTestAccountSchema(Schema):
    """This class manages technical requirement request schema."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Exclude unknown fields in the deserialized output."""

        unknown = EXCLUDE

    no_of_test_account = fields.Int(data_key='noOfTestAccount', required=True, validate=validate.OneOf([1, 2, 3, 5]))
    note_test_account = fields.Str(data_key='noteTestAccount', allow_none=True)


class TechnicalReqResponseSchema(TechnicalReqRequestSchema,
                                 TechnicalReqPackageSchema,
                                 TechnicalReqTestAccountSchema
                                 ):
    """This class manages technical requirement response schema."""
