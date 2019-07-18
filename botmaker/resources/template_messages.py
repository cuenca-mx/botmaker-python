from dataclasses import dataclass, field

from botmaker.exc import InvalidPhoneNumber
from botmaker.helpers import sanitize_phone_number

from .base import Resource


@dataclass
class TemplateMessage(Resource):
    _endpoint = '/intent/v2'

    id: str
    from_: str
    to: str
    template: str
    params: dict = field(default_factory=dict)

    @classmethod
    def create(
            cls,
            from_: str,
            to: str,
            template: str,
            chat_platform: str = 'whatsapp',
            **params
    ):
        """
        Based on
        https://botmakeradmin.github.io/docs/es/#/messages-api?id=templates-messages
        """
        from_ = sanitize_phone_number(from_)
        if chat_platform == 'whatsapp':
            checked = cls._client.check_whatsapp_contact(from_, to)
            if not checked:
                raise InvalidPhoneNumber(
                    f"'{to} is not from valid WhatsApp contact")
            else:
                to = checked
        else:
            to = sanitize_phone_number(to)
        data = dict(
            chatPlatform=chat_platform,
            chatChannelNumber=from_,
            platformContactId=to,
            ruleNameOrId=template,
            params=params
        )
        resp = cls._client.post(cls._endpoint, data)
        return cls(resp['id'], from_, to, template, params)
