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

from ..api import API_URI_PREFIX
from ..helper.auth import ss_client_auth_header
from ..helper.request_data import factory_project_technical_req
from .test_api_project import create_project
from .test_api_scope_package import get_scope_packages


TECHNICALREQ_API = API_URI_PREFIX + 'project/:project_id/technical-req'


def test_post_technical_req(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    response = _create_technical_req_(client, jwt)

    assert response.status_code == HTTPStatus.CREATED


def test_post_technical_req_validation(client, jwt, session):
    """Assert that the endpoint returns the failure status."""
    headers = ss_client_auth_header(jwt)
    project = create_project(client, jwt)
    req_data = {}

    response = client.post(TECHNICALREQ_API.replace(':project_id', str(project['id'])), data=json.dumps(req_data),
                           headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_patch_technical_req_package(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    headers = ss_client_auth_header(jwt)
    technical_req = create_technical_req(client, jwt)
    scope_packages = get_scope_packages(client, jwt, session)
    req_data = {
        'update': 'package',
        'scopePackageId': scope_packages['scopePackages'][0]['id']
    }

    response = client.patch(TECHNICALREQ_API.replace(':project_id', str(technical_req['projectId'])),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK


def test_patch_technical_req_test_account(client, jwt, session): 
    """Assert that the endpoint returns the success status."""
    headers = ss_client_auth_header(jwt)
    technical_req = create_technical_req(client, jwt)
    req_data = {
        'update': 'test-account',
        'noOfTestAccount': 5,
        'noteTestAccount': 'renmarks'
    }

    response = client.patch(TECHNICALREQ_API.replace(':project_id', str(technical_req['projectId'])),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK


def test_patch_technical_req_validation(client, jwt, session):
    """Assert that the endpoint returns the failure status."""
    headers = ss_client_auth_header(jwt)
    technical_req = create_technical_req(client, jwt)
    scope_packages = get_scope_packages(client, jwt, session)
    req_data = {
        'scopePackageId': scope_packages['scopePackages'][0]['id']
    }

    response = client.patch(TECHNICALREQ_API.replace(':project_id', str(technical_req['projectId'])),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_get_technical_req(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    headers = ss_client_auth_header(jwt)
    technical_req = create_technical_req(client, jwt)

    response = client.get(TECHNICALREQ_API.replace(':project_id', str(technical_req['projectId'])),
                          headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK


def create_technical_req(client, jwt):
    """Create technical requirement and return technical_req object."""
    response = _create_technical_req_(client, jwt)
    technical_req = json.loads(response.data)
    return technical_req


def _create_technical_req_(client, jwt):
    """Create technical requirement and return response object."""
    headers = ss_client_auth_header(jwt)
    project = create_project(client, jwt)
    request_data = factory_project_technical_req()
    request_data['projectId'] = project['id']

    response = client.post(TECHNICALREQ_API.replace(':project_id', str(project['id'])),
                           data=json.dumps(request_data),
                           headers=headers, content_type='application/json')
    return response
