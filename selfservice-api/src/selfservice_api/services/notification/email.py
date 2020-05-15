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
"""Send Email service."""

from flask import current_app, g
from flask_mail import Mail, Message

from ...models import EmailQueue
from ...utils.logging import log_error
from .email_helper import EmailBody, EmailSubject, EmailType


mail = Mail()  # pylint: disable=invalid-name


class EmailService():
    """Email service."""

    @classmethod
    def send(cls, email_queue: EmailQueue):
        """Send Email."""
        try:
            message = Message(subject=email_queue.subject, html=email_queue.body,
                              recipients=email_queue.recipients, sender=email_queue.sender,
                              cc=email_queue.cc, bcc=email_queue.bcc)

            mail.send(message)
        except Exception as err:  # pylint: disable=broad-except
            log_error(err)

    @classmethod
    def save_and_send(cls, etype: EmailType, attributes: dict, to=None, cc=None):  # pylint: disable=invalid-name
        """Save and Send Email.

        :param etype: EmailType
        :param attributes: dict

        Optional parameters. Not required for any email type meant for an analyst.
        :param to: list or str
        :param cc: list or str
        """
        email_queue = EmailService._prepare_email_queue_(etype, attributes, to, cc)
        email_queue.email_type = etype.value
        if 'user' in g:
            email_queue.created_by = g.user.id
        else:
            email_queue.created_by = 'system'
        email_queue.save()
        cls.send(email_queue)

    @staticmethod
    def _prepare_email_queue_(etype: EmailType, attributes: dict, to, cc):  # pylint: disable=invalid-name
        """Prepare email queue object."""
        app_url = current_app.config.get('APP_URL')
        attributes['url'] = app_url.rstrip('/')

        from_email = current_app.config.get('EMAIL_ID_FROM')
        attributes['EMAIL_ID_FROM'] = from_email

        analyst_email = current_app.config.get('EMAIL_ID_ANALYST')
        attributes['EMAIL_ID_ANALYST'] = analyst_email

        email_id_cc = current_app.config.get('EMAIL_ID_CC')
        attributes['EMAIL_ID_CC'] = email_id_cc.split(',') if email_id_cc else None

        if isinstance(to, list):
            recipients = to
        elif isinstance(to, str):
            recipients = to.split(',')
        else:
            recipients = [analyst_email]

        if isinstance(cc, list):
            cc_email = cc
        elif isinstance(cc, str):
            cc_email = cc.split(',')
        else:
            cc_email = attributes['EMAIL_ID_CC']

        debug_email = current_app.config.get('EMAIL_ID_DEBUG')
        attributes['EMAIL_ID_DEBUG'] = debug_email

        if 'user' in g:
            attributes['user'] = g.user

        email_queue = EmailQueue()
        email_queue.sender = from_email
        email_queue.recipients = recipients
        email_queue.cc = cc_email
        email_queue.bcc = [debug_email] if debug_email else None

        email_queue.subject = EmailSubject.get(etype, attributes)
        email_queue.body = EmailBody.get(etype, attributes)

        return email_queue
