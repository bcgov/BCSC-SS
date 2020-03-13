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
"""Helper class for email."""

import os
import re
from enum import Enum

from jinja2 import Environment, FileSystemLoader

from ...utils.logging import log_error


class EmailType(Enum):
    """Types of email."""

    TEST_ACCOUNT = 'test_account'
    DEV_REQUEST = 'dev_request'


class EmailSubject:  # pylint: disable=too-few-public-methods
    """Email subject for each type."""

    test_account = 'Test accounts in self service application low'
    dev_request = 'Development Access Request - API Keys sent'

    @classmethod
    def get(cls, email_type: EmailType, attributes: dict):
        """Get the email subject."""
        subject = cls.__dict__.get(email_type.value)
        if subject:
            attrs = re.findall(r'{{\w+}}', subject)
            for attr in set(attrs):
                attr_name = attr.replace('{', '').replace('}', '')
                attr_value = attributes.get(attr_name)
                subject = subject.replace(attr, attr_value) if attr_value else ''
        else:
            log_error('unknown email subject')

        return subject


class EmailBody:  # pylint: disable=too-few-public-methods
    """Email body for each type."""

    @classmethod
    def get(cls, email_type: EmailType, attributes: dict):
        """Get the email body."""
        root = os.path.dirname(os.path.abspath(__file__))
        templates_dir = os.path.join(root, 'templates')
        env = Environment(loader=FileSystemLoader(templates_dir), autoescape=True)
        template = env.get_template(email_type.value + '.html')

        result = template.render(attributes)
        return result
