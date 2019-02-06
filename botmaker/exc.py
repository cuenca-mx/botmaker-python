from requests import HTTPError


class BotmakerException(Exception):
    """Generic BotMaker API exception"""

    def __str__(self):
        return getattr(self, 'message', self.__class__.__doc__)


class InvalidAuth(BotmakerException, HTTPError):
    """Invalid API authentication credentials"""
