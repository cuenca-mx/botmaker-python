from typing import Optional

from requests import HTTPError


class BotmakerException(Exception):
    """Generic BotMaker API exception"""

    def __init__(self, message: Optional[str] = None):
        if message:
            self.message = message

    def __str__(self):
        return getattr(self, 'message', self.__class__.__doc__)


class InvalidAuth(BotmakerException, HTTPError):
    """Invalid API authentication credentials"""


class InvalidPhoneNumber(BotmakerException):
    """Phone number is not associated to a WhatsApp account"""
