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
"""Tests to assure the API endpoints for managing a project info resource is working as expected."""

import json
from http import HTTPStatus

from ..helper.api_create_data import (PROJECTINFO_API, _create_project_, _get_project_, _get_all_project_,  # noqa: I001
                                      create_project, create_technical_req_with_additional, create_user,  # noqa: I001
                                      get_project)  # noqa: I001
from ..helper.auth import ss_client_auth_header

from selfservice_api.models.enums import ProjectRoles


def test_post_project_as_developer(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    create_user(client, jwt, project_role='manager')
    response = _create_project_(client, jwt, ProjectRoles.Developer)

    assert response.status_code == HTTPStatus.CREATED


def test_post_project_as_manager(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    create_user(client, jwt, project_role='cto')
    response = _create_project_(client, jwt, ProjectRoles.Manager)

    assert response.status_code == HTTPStatus.CREATED


def test_post_project_as_cto(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    create_user(client, jwt, project_role='developer')
    response = _create_project_(client, jwt, ProjectRoles.Cto)

    assert response.status_code == HTTPStatus.CREATED


def test_post_project_validation(client, jwt, session):
    """Assert that the endpoint returns the failure status."""
    headers = ss_client_auth_header(jwt)
    req_data = {}

    response = client.post(PROJECTINFO_API, data=json.dumps(req_data),
                           headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_get_all_project(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    response = _get_all_project_(client, jwt)
    assert response.status_code == HTTPStatus.OK


def test_get_project(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    response = _get_project_(client, jwt)
    assert response.status_code == HTTPStatus.OK


def test_put_project_(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    headers = ss_client_auth_header(jwt)
    project = get_project(client, jwt)

    response = client.put(PROJECTINFO_API + '/' + str(project['id']),
                          data=json.dumps(project), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK


def test_put_project_validation(client, jwt, session):
    """Assert that the endpoint returns the failure status."""
    headers = ss_client_auth_header(jwt)
    project = get_project(client, jwt)
    req_data = {}

    response = client.put(PROJECTINFO_API + '/' + str(project['id']), data=json.dumps(req_data),
                          headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_patch_project_status(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    headers = ss_client_auth_header(jwt)
    technical_req = create_technical_req_with_additional(client, jwt)

    req_data = {'update': 'status', 'status': 2}
    response = client.patch(PROJECTINFO_API + '/' + str(technical_req['projectId']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK

    # check the skip condition on oidc config
    response = client.patch(PROJECTINFO_API + '/' + str(technical_req['projectId']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')


def test_patch_project_status_validation(client, jwt, session):
    """Assert that the endpoint returns the failure status."""
    headers = ss_client_auth_header(jwt)
    req_data = {}

    response = client.patch(PROJECTINFO_API + '/1234',
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST

    req_data = {'update': ''}

    technical_req = create_technical_req_with_additional(client, jwt)
    response = client.patch(PROJECTINFO_API + '/' + str(technical_req['projectId']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST

    req_data = {'update': 'status'}

    response = client.patch(PROJECTINFO_API + '/1234',
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST

    req_data = {'update': 'status'}

    technical_req = create_technical_req_with_additional(client, jwt)
    response = client.patch(PROJECTINFO_API + '/' + str(technical_req['projectId']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST

    req_data = {'update': 'status', 'status': 2}

    project = create_project(client, jwt)
    response = client.patch(PROJECTINFO_API + '/' + str(project['id']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST
