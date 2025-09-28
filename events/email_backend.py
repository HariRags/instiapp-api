import logging
import smtplib
import ssl
from django.core.mail.backends.smtp import EmailBackend as DjangoEmailBackend

logger = logging.getLogger(__name__)

class PatchedEmailBackend(DjangoEmailBackend):
    """SMTP Email backend patched for Python 3.12.

    Django <4.2 passes keyfile/certfile to smtplib.SMTP.starttls().
    Python 3.12 removed those kwargs, raising:
        TypeError: SMTP.starttls() got an unexpected keyword argument 'keyfile'

    This backend replicates Django's logic but calls starttls(context=...).
    """

    def open(self):  # noqa: D401
        if self.connection:
            return False
        try:
            timeout = self.timeout or None
            host = self.host
            port = self.port
            logger.info("[PatchedEmailBackend] Opening SMTP connection host=%s port=%s use_ssl=%s use_tls=%s", host, port, self.use_ssl, self.use_tls)

            if self.use_ssl:
                context = ssl.create_default_context()
                self.connection = smtplib.SMTP_SSL(host, port, timeout=timeout, context=context)
            else:
                self.connection = smtplib.SMTP(host, port, timeout=timeout)
                self.connection.ehlo()
                if self.use_tls:
                    context = ssl.create_default_context()
                    logger.info("[PatchedEmailBackend] Initiating STARTTLS (patched, no keyfile/certfile)")
                    self.connection.starttls(context=context)
                    self.connection.ehlo()

            if self.username and self.password:
                logger.info("[PatchedEmailBackend] Logging in as %s", self.username)
                self.connection.login(self.username, self.password)
            logger.info("[PatchedEmailBackend] SMTP connection established")
            return True
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("[PatchedEmailBackend] Failed to open SMTP connection: %s", exc, exc_info=True)
            if not self.fail_silently:
                raise
            return False
