import os
from typing import Optional

import requests

from .exc import BotmakerException, InvalidAuth
from .helpers import sanitize_phone_number
from .resources import Message, Resource, TemplateMessage


class Client:
    BASE_URL = 'https://go.botmaker.com/api/v1.0'

    messages = Message
    template_messages = TemplateMessage

    def __init__(self, access_token: Optional[str] = None):
        self.session = requests.Session()
        self.access_token = access_token or os.environ['BOTMAKER_ACCESS_TOKEN']
        self.headers = {'access-token': self.access_token}
        Resource._client = self

    def get(self, endpoint: str, **kwargs) -> dict:
        return self.request('get', endpoint, {}, **kwargs)

    def post(self, endpoint: str, data: dict, **kwargs) -> dict:
        return self.request('post', endpoint, data, **kwargs)

    def request(
        self, method: str, endpoint: str, data: dict, **kwargs
    ) -> dict:
        url = self.BASE_URL + endpoint
        response = self.session.request(
            method, url, headers=self.headers, json=data, **kwargs
        )
        self._check_response(response)
        return response.json()

    @staticmethod
    def _check_response(response):
        if response.ok:
            body = response.json()
            if body.get('problems'):
                raise BotmakerException(body['problems']['message'])
        if response.status_code == 401:
            raise InvalidAuth
        else:
            response.raise_for_status()

    def check_whatsapp_contact(
        self, channel: str, phone_number: str
    ) -> Optional[str]:
        """
        Check a single phone number.
        """
        result = self.check_whatsapp_contacts(channel, [phone_number])
        try:
            checked = result[phone_number]
        except KeyError:
            checked = None
        return checked

    def check_whatsapp_contacts(
        self, channel: str, phone_numbers: list
    ) -> dict:
        """
        Check a list of phone numbers.
        Based on
        https://botmakeradmin.github.io/docs/es/#/messages-api?id=chequear-validez-de-n%C3%BAmeros-de-contactos-de-whatsapp
        """
        channel = sanitize_phone_number(channel)
        data = dict(chatChannelNumber=channel, contacts=phone_numbers)
        resp = self.post('/customer/checkWhatsAppContact', data)
        try:
            result = resp['result']
        except KeyError:
            # This should never happen
            raise BotmakerException("Expected 'result' in the response body")
        return result
