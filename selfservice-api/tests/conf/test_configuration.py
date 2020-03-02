# Copyright © 2019 Province of British Columbia.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests to assure the configuration objects.

Test-Suite to ensure that the Configuration Classes are working as expected.
"""

from importlib import reload

import pytest

from selfservice_api import config


# testdata pattern is ({str: environment}, {expected return value})
TEST_ENVIRONMENT_DATA = [
    ('valid', 'development', config.DevConfig),
    ('valid', 'testing', config.TestConfig),
    ('valid', 'default', config.ProdConfig),
    ('valid', 'production', config.ProdConfig),
    ('error', None, KeyError)
]


@pytest.mark.parametrize('test_type,environment,expected', TEST_ENVIRONMENT_DATA)
def test_get_named_config(test_type, environment, expected):
    """Assert that the named configurations can be loaded.

    Or that a KeyError is returned for missing config types.
    """
    if test_type == 'valid':
        assert isinstance(config.get_named_config(environment), expected)
    else:
        with pytest.raises(KeyError):
            config.get_named_config(environment)


def test_prod_config_secret_key(monkeypatch):
    """Assert that the ProductionConfig is correct.

    The object either uses the SECRET_KEY from the environment,
    or creates the SECRET_KEY on the fly.
    """
    key = 'SECRET_KEY'

    # Assert that secret key will default to some value
    # even if missed in the environment setup
    monkeypatch.delenv(key, raising=False)
    reload(config)
    assert config.ProdConfig().SECRET_KEY is not None

    # Assert that the secret_key is set to the assigned environment value
    monkeypatch.setenv(key, 'SECRET_KEY')
    reload(config)
    assert config.ProdConfig().SECRET_KEY == 'SECRET_KEY'


def test_prod_config_jwks_cache(monkeypatch):
    """Assert that the Config is correct.

    The object either uses the JWT_OIDC_JWKS_CACHE_TIMEOUT from the environment,
    or creates the JWT_OIDC_JWKS_CACHE_TIMEOUT defaults to 300
    """
    key = 'JWT_OIDC_JWKS_CACHE_TIMEOUT'

    # Assert that secret key will default to some value
    # even if missed in the environment setup
    monkeypatch.delenv(key)  # , raising=False)
    monkeypatch.setenv(key, None)
    reload(config)
    assert config.ProdConfig().JWT_OIDC_JWKS_CACHE_TIMEOUT is not None

    # Assert that the secret_key is set to the assigned environment value
    monkeypatch.setenv(key, 500)
    reload(config)
    assert config.ProdConfig().JWT_OIDC_JWKS_CACHE_TIMEOUT == 500

    # Assert that the secret_key is set to the assigned environment value
    monkeypatch.setenv(key, 'ack')
    reload(config)
    assert config.ProdConfig().JWT_OIDC_JWKS_CACHE_TIMEOUT == 300


def test_dynamic_api_url(monkeypatch):
    """Assert that the Config is correct.

    The object either uses the DYNAMIC_TEST_API_URL and DYNAMIC_PROD_API_URL with trailing /.
    """
    key = 'DYNAMIC_TEST_API_URL'

    monkeypatch.delenv(key)
    monkeypatch.setenv(key, 'DYNAMIC_TEST_API_URL/')
    reload(config)

    key = 'DYNAMIC_PROD_API_URL'

    monkeypatch.delenv(key)
    monkeypatch.setenv(key, 'DYNAMIC_PROD_API_URL/')
    reload(config)
