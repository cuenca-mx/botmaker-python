import os
from typing import Optional

import requests

from .exc import InvalidAuth
from .resources import Resource, TemplateMessage


class Client:
    BASE_URL = 'https://go.botmaker.com/api/v1.0'

    template_messages = TemplateMessage

    def __init__(self, access_token: Optional[str] = None):
        self.access_token = access_token or os.environ['BOTMAKER_ACCESS_TOKEN']
        self.headers = {'access-token': self.access_token}
        Resource._client = self

    def get(self, endpoint: str, **kwargs) -> dict:
        return self.request('get', endpoint, {}, **kwargs)

    def post(self, endpoint: str, data: dict, **kwargs) -> dict:
        return self.request('post', endpoint, data, **kwargs)

    def request(self,
                method: str,
                endpoint: str,
                data: dict,
                **kwargs) -> dict:
        url = self.BASE_URL + endpoint
        response = requests.request(
            method, url, headers=self.headers, json=data, **kwargs)
        self._check_response(response)
        return response.json()

    @staticmethod
    def _check_response(response):
        if response.ok:
            return
        if response.status_code == 401:
            raise InvalidAuth
        else:
            response.raise_for_status()
