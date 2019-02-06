from requests import HTTPError


class BotmakerException(Exception):
    """Generic BotMaker API exception"""


class InvalidAuth(BotmakerException, HTTPError):
    """Invalid API authentication credentials"""
