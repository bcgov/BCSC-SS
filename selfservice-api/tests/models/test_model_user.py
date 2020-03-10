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
"""This tests User model."""

from ..helper.request_data import factory_user_info

from selfservice_api.models.user import User


def test_create_from_dict(session):
    """Assert user creation from the provided dictionary."""
    user = create_user(session)
    assert user.id is not None


def test_none_create_from_dict(session):
    """Assert skipping user creation by providing None."""
    user = User.create_from_dict(user_info=None)
    assert user is None


def test_update(session):
    """Assert user updation."""
    user = create_user(session)
    user.update({'phone': '123456897'})
    found = user.find_by_oauth_id(user.oauth_id)
    assert found.phone == '123456897'


def test_find_by_id(session):
    """Assert user instance that matches the provided id."""
    user = create_user(session)
    found = user.find_by_id(user.id)
    assert found is not None


def test_find_by_email(session):
    """Assert user instance that matches the email."""
    user = create_user(session)
    found = user.find_by_email(user.email)
    assert found is not None


def test_find_by_oauth_id(session):
    """Assert user instance that matches the provided oauth_id."""
    user = create_user(session)
    found = user.find_by_oauth_id(user.oauth_id)
    assert found is not None


def create_user(session):
    """Create user and return user object."""
    user_info = factory_user_info(is_model=True)
    user = User.create_from_dict(
        user_info=user_info)
    session.add(user)
    session.commit()
    return user
