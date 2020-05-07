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
"""Tests to assure the API endpoints for managing a project team is working as expected."""

import json
from http import HTTPStatus

from ..helper.api_create_data import (TEAM_API, create_team, _create_team_, _delete_team_member_,  # noqa: I001
                                    _get_team_, _get_team_member_, create_project)  # noqa: I001
from ..helper.auth import ss_admin_auth_header, ss_client_auth_header
from ..helper.request_data import factory_project_team_member

from selfservice_api.models.enums import ProjectRoles


def test_post_team(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    response = _create_team_(client, jwt, member_role=ProjectRoles.Manager)
    assert response.status_code == HTTPStatus.CREATED


def test_post_team_validation(client, jwt, session):
    """Assert that the endpoint returns the failure status."""
    headers = ss_client_auth_header(jwt)
    project = create_project(client, jwt)

    request_data = factory_project_team_member()
    response = client.post(TEAM_API.replace(':project_id', str(project['id'])),
                           data=json.dumps(request_data),
                           headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.BAD_REQUEST

    request_data = factory_project_team_member(member_role=None)
    response = client.post(TEAM_API.replace(':project_id', str(project['id'])),
                           data=json.dumps(request_data),
                           headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.BAD_REQUEST

    request_data = factory_project_team_member(member_role=ProjectRoles.Manager)
    request_data['role'] = 0
    response = client.post(TEAM_API.replace(':project_id', str(project['id'])),
                           data=json.dumps(request_data),
                           headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_put_team(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    headers = ss_admin_auth_header(jwt)
    team = create_team(client, jwt, member_role=ProjectRoles.Manager)

    get_team_response = _get_team_(client, jwt, str(team['projectId']))
    get_team = json.loads(get_team_response.data)['team'][0]
    team_put_api = TEAM_API.replace(':project_id', str(team['projectId'])) + '/' + str(get_team['id'])
    response = client.put(team_put_api, data=json.dumps(get_team),
                          headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.OK

    team_put_api = TEAM_API.replace(':project_id', str(team['projectId'])) + '/' + str(team['id'])
    response = client.put(team_put_api, data=json.dumps(team),
                          headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.OK


def test_put_team_validation(client, jwt, session):
    """Assert that the endpoint returns the failure status."""
    headers = ss_admin_auth_header(jwt)
    team = create_team(client, jwt, member_role=ProjectRoles.Manager)
    team_put_api = TEAM_API.replace(':project_id', str(team['projectId'])) + '/' + str(team['id'])

    request_data = factory_project_team_member()
    response = client.put(team_put_api,
                          data=json.dumps(request_data),
                          headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.BAD_REQUEST

    request_data = factory_project_team_member(member_role=ProjectRoles.Manager)
    request_data['role'] = 0
    response = client.put(team_put_api,
                          data=json.dumps(request_data),
                          headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_delete_team_member(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    team = create_team(client, jwt, member_role=ProjectRoles.Manager)
    _delete_team_member_(client, jwt, str(team['projectId']), '0')
    response = _delete_team_member_(client, jwt, str(team['projectId']), str(team['id']))
    assert response.status_code == HTTPStatus.OK


def test_get_team_member(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    team = create_team(client, jwt, member_role=ProjectRoles.Manager)
    response = _get_team_member_(client, jwt, str(team['projectId']), str(team['id']))
    assert response.status_code == HTTPStatus.OK


def test_get_team(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    team = create_team(client, jwt, member_role=ProjectRoles.Manager)
    response = _get_team_(client, jwt, str(team['projectId']))
    assert response.status_code == HTTPStatus.OK
