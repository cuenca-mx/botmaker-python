from dataclasses import dataclass

from botmaker.exc import InvalidPhoneNumber
from botmaker.helpers import sanitize_phone_number

from .base import Resource


@dataclass
class Message(Resource):
    _endpoint = '/message/v3'

    id: str
    from_: str
    to: str
    message_text: str

    @classmethod
    def create(
            cls,
            from_: str,
            to: str,
            message_text: str,
            chat_platform: str = 'whatsapp'
    ):
        """
        Based on
        https://botmakeradmin.github.io/docs/es/#/messages-api?id=enviando-mensajes-a-los-usuarios
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
            messageText=message_text
        )
        resp = cls._client.post(cls._endpoint, data)
        return cls(resp['id'], from_, to, message_text)
