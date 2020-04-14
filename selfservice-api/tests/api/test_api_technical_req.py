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
"""Tests to assure the API endpoints for managing a project technical requirements is working as expected."""

import json
from http import HTTPStatus

from ..helper.api_create_data import (TECHNICALREQ_API, _create_technical_req_, _get_technical_req_,  # noqa: I001
                                      _update_technical_req_with_package_,  # noqa: I001
                                      _update_technical_req_with_test_account_,  # noqa: I001
                                      create_project, create_technical_req, get_scope_packages)  # noqa: I001
from ..helper.auth import ss_client_auth_header
from ..helper.request_data import factory_project_technical_req

from selfservice_api.models.enums import SigningEncryptionType


def test_post_technical_req(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    response = _create_technical_req_(client, jwt)
    assert response.status_code == HTTPStatus.CREATED

    response = _create_technical_req_(client, jwt, signing_encryption_type=SigningEncryptionType.SignedJWT)
    assert response.status_code == HTTPStatus.CREATED


def test_post_technical_req_validation(client, jwt, session):
    """Assert that the endpoint returns the failure status."""
    headers = ss_client_auth_header(jwt)
    project = create_project(client, jwt)

    req_data = {}
    response = client.post(TECHNICALREQ_API.replace(':project_id', str(project['id'])), data=json.dumps(req_data),
                           headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.BAD_REQUEST

    req_data = factory_project_technical_req(signing_encryption_type=SigningEncryptionType.SignedJWT)
    req_data['signedResponseAlg'] = None
    req_data['encryptedResponseAlg'] = None
    req_data['jwksUri'] = None
    response = client.post(TECHNICALREQ_API.replace(':project_id', str(project['id'])), data=json.dumps(req_data),
                           headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.BAD_REQUEST

    req_data = factory_project_technical_req(signing_encryption_type=SigningEncryptionType.SecureJWT)
    req_data['signedResponseAlg'] = None
    req_data['encryptedResponseAlg'] = None
    req_data['jwksUri'] = None
    response = client.post(TECHNICALREQ_API.replace(':project_id', str(project['id'])), data=json.dumps(req_data),
                           headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_put_technical_req(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    headers = ss_client_auth_header(jwt)
    technical_req = create_technical_req(client, jwt)

    response = client.put(TECHNICALREQ_API.replace(':project_id', str(technical_req['projectId'])),
                          data=json.dumps(technical_req), headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.OK


def test_put_technical_req_validation(client, jwt, session):
    """Assert that the endpoint returns the failure status."""
    headers = ss_client_auth_header(jwt)
    technical_req = create_technical_req(client, jwt)
    req_data = {}

    response = client.put(TECHNICALREQ_API.replace(':project_id', str(technical_req['projectId'])),
                          data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_patch_technical_req_package(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    technical_req = create_technical_req(client, jwt)
    response = _update_technical_req_with_package_(client, jwt, str(technical_req['projectId']))
    assert response.status_code == HTTPStatus.OK


def test_patch_technical_req_test_account(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    technical_req = create_technical_req(client, jwt)
    response = _update_technical_req_with_test_account_(client, jwt, str(technical_req['projectId']))
    assert response.status_code == HTTPStatus.OK


def test_patch_technical_req_validation(client, jwt, session):
    """Assert that the endpoint returns the failure status."""
    headers = ss_client_auth_header(jwt)
    technical_req = create_technical_req(client, jwt)
    scope_packages = get_scope_packages(client, jwt)
    req_data = {
        'scopePackageId': scope_packages['scopePackages'][0]['id']
    }

    response = client.patch(TECHNICALREQ_API.replace(':project_id', str(technical_req['projectId'])),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_get_technical_req(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    technical_req = create_technical_req(client, jwt)

    response = _get_technical_req_(client, jwt, str(technical_req['projectId']))

    assert response.status_code == HTTPStatus.OK
