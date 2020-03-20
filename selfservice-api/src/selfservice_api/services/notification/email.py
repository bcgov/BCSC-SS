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
from .email_helper import EmailBody, EmailSubject, EmailType


mail = Mail()  # pylint: disable=invalid-name


class EmailService():
    """Email service."""

    @classmethod
    def send(cls, email_queue: EmailQueue):
        """Send Email."""
        message = Message(subject=email_queue.subject, html=email_queue.body,
                          recipients=email_queue.recipients, sender=email_queue.sender,
                          cc=email_queue.cc, bcc=email_queue.bcc)
        mail.send(message)

    @classmethod
    def save_and_send(cls, email_type: EmailType, attributes: dict):
        """Save and Send Email."""
        email_queue = EmailService._prepare_email_queue_(email_type, attributes=attributes)
        email_queue.email_type = email_type.value
        if g.user:
            email_queue.created_by = g.user.id
        email_queue.save()
        cls.send(email_queue)

    @staticmethod
    def _prepare_email_queue_(email_type: EmailType, attributes: dict):
        """Prepare email queue object."""
        from_email = current_app.config.get('EMAIL_ID_FROM')
        attributes['EMAIL_ID_FROM'] = from_email

        analyst_email = current_app.config.get('EMAIL_ID_ANALYST')
        attributes['EMAIL_ID_ANALYST'] = analyst_email

        cc_email = current_app.config.get('EMAIL_ID_CC')
        cc_email = cc_email.split(',') if cc_email else None
        attributes['EMAIL_ID_CC'] = cc_email

        debug_email = current_app.config.get('EMAIL_ID_DEBUG')
        attributes['EMAIL_ID_DEBUG'] = debug_email

        if g.user:
            attributes['user'] = g.user

        email_queue = EmailQueue()
        email_queue.sender = from_email
        email_queue.recipients = [analyst_email]
        email_queue.cc = cc_email
        email_queue.bcc = [debug_email] if debug_email else None

        email_queue.subject = EmailSubject.get(email_type, attributes)
        email_queue.body = EmailBody.get(email_type, attributes)

        return email_queue
