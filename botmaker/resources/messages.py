from dataclasses import dataclass

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
        check_phone: bool = False,
        chat_platform: str = 'whatsapp',
    ):
        """
        Based on
        https://botmakeradmin.github.io/docs/es/#/messages-api?id=enviando-mensajes-a-los-usuarios
        """
        return cls.commonCreate(
            from_, to, chat_platform, check_phone, message_text=message_text
        )
