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

from ..helper.api_create_data import (PROJECTINFO_API,  # noqa: I001
                                    _create_admin_user_, _create_project_, _get_project_,  # noqa: I001
                                    _get_all_project_, _update_technical_req_with_test_account_,  # noqa: I001
                                    create_project, create_technical_req_with_additional, create_user,  # noqa: I001
                                    get_project)  # noqa: I001
from ..helper.auth import ss_admin_auth_header, ss_client_auth_header

from selfservice_api.models.enums import ProjectRoles, ProjectStatus


def test_post_project_as_analyst(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    response = _create_project_(client, jwt, None, is_analyst=True)
    assert response.status_code == HTTPStatus.CREATED


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
    create_user(client, jwt)
    headers = ss_client_auth_header(jwt)
    req_data = {}

    response = client.post(PROJECTINFO_API, data=json.dumps(req_data),
                           headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_get_all_project(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    response = _get_all_project_(client, jwt)
    assert response.status_code == HTTPStatus.OK


def test_get_all_project_analyst(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    _create_admin_user_(client, jwt)
    response = _get_all_project_(client, jwt, True)
    assert response.status_code == HTTPStatus.OK


def test_get_project(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    response = _get_project_(client, jwt)
    assert response.status_code == HTTPStatus.OK

    response = _get_project_(client, jwt, is_analyst=True)
    assert response.status_code == HTTPStatus.OK


def test_delete_project(client, jwt, session):
    """Assert that the endpoint returns the success status."""
    # Delete as admin
    headers = ss_admin_auth_header(jwt)
    project = get_project(client, jwt)
    response = client.delete(PROJECTINFO_API + '/' + str(project['id']),
                             headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.OK

    # Delete as client
    project = get_project(client, jwt)
    response = client.delete(PROJECTINFO_API + '/' + str(project['id']),
                             headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.OK

    headers = ss_client_auth_header(jwt)
    technical_req = create_technical_req_with_additional(client, jwt)

    req_data = {'update': 'status', 'status': ProjectStatus.Dev}
    project_id = str(technical_req['projectId'])
    response = client.patch(PROJECTINFO_API + '/' + project_id,
                            data=json.dumps(req_data), headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.OK

    req_data = {'update': 'status', 'status': ProjectStatus.DevComplete}
    response = client.patch(PROJECTINFO_API + '/' + project_id,
                            data=json.dumps(req_data), headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.OK

    response = client.delete(PROJECTINFO_API + '/' + project_id,
                             headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_put_project(client, jwt, session):
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

    req_data = {'update': 'status', 'status': ProjectStatus.Dev}
    response = client.patch(PROJECTINFO_API + '/' + str(technical_req['projectId']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK

    # check the update condition on test account
    _update_technical_req_with_test_account_(client, jwt, str(technical_req['projectId']), 2)
    response = client.patch(PROJECTINFO_API + '/' + str(technical_req['projectId']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.OK

    _update_technical_req_with_test_account_(client, jwt, str(technical_req['projectId']), 5)
    response = client.patch(PROJECTINFO_API + '/' + str(technical_req['projectId']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.OK

    _update_technical_req_with_test_account_(client, jwt, str(technical_req['projectId']), 0)
    response = client.patch(PROJECTINFO_API + '/' + str(technical_req['projectId']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')
    assert response.status_code == HTTPStatus.OK

    req_data = {'update': 'status', 'status': ProjectStatus.DevComplete}
    response = client.patch(PROJECTINFO_API + '/' + str(technical_req['projectId']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK


def test_patch_project_status_validation(client, jwt, session):
    """Assert that the endpoint returns the failure status."""
    headers = ss_client_auth_header(jwt)
    create_user(client, jwt)

    req_data = {}

    technical_req = create_technical_req_with_additional(client, jwt)
    response = client.patch(PROJECTINFO_API + '/' + str(technical_req['projectId']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST

    req_data = {'update': ''}

    technical_req = create_technical_req_with_additional(client, jwt)
    response = client.patch(PROJECTINFO_API + '/' + str(technical_req['projectId']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST

    req_data = {'update': 'status'}

    technical_req = create_technical_req_with_additional(client, jwt)
    response = client.patch(PROJECTINFO_API + '/' + str(technical_req['projectId']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST

    req_data = {'update': 'status', 'status': ProjectStatus.Dev}

    project = create_project(client, jwt)
    response = client.patch(PROJECTINFO_API + '/' + str(project['id']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_patch_project_status_oidc_and_test_account(client, jwt, session, config):
    """Assert that the endpoint returns the failure status."""
    headers = ss_client_auth_header(jwt)
    technical_req = create_technical_req_with_additional(client, jwt)

    # Dynamic OIDC None response: Start
    config['dynamic_api_return_none'] = True
    req_data = {'update': 'status', 'status': ProjectStatus.Dev}
    response = client.patch(PROJECTINFO_API + '/' + str(technical_req['projectId']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR

    # call again to cover update api call
    config.pop('dynamic_api_return_none')

    response = client.patch(PROJECTINFO_API + '/' + str(technical_req['projectId']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK

    config['dynamic_api_return_none'] = True
    response = client.patch(PROJECTINFO_API + '/' + str(technical_req['projectId']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    config.pop('dynamic_api_return_none')

    # Dynamic OIDC None response: End

    config['LIMITED_TEST_ACCOUNT_TRIGGER_COUNT'] = 200
    req_data = {'update': 'status', 'status': ProjectStatus.Dev}
    response = client.patch(PROJECTINFO_API + '/' + str(technical_req['projectId']),
                            data=json.dumps(req_data), headers=headers, content_type='application/json')

    assert response.status_code == HTTPStatus.OK
