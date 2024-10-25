from typing import Any, ClassVar, Dict

from botmaker.exc import InvalidPhoneNumber
from botmaker.helpers import sanitize_phone_number


class Resource:
    _client: ClassVar['botmaker.Client']  # type: ignore # noqa: F821
    _endpoint: str

    def __init__(self, *_, **__):
        ...

    @classmethod
    def commonCreate(
        cls, from_: str, to: str, chat_platform: str, check_phone: bool, **data
    ):
        from_ = sanitize_phone_number(from_)
        if chat_platform == 'whatsapp' and check_phone:
            checked = cls._client.check_whatsapp_contact(from_, to)
            if not checked:
                raise InvalidPhoneNumber(
                    f"'{to} is not from valid WhatsApp contact"
                )
            else:
                to = checked
        else:
            to = sanitize_phone_number(to)
        body: Dict[str, Any] = dict(
            chatPlatform=chat_platform,
            chatChannelNumber=from_,
            platformContactId=to,
        )

        if cls._endpoint == '/message/v3':
            body['messageText'] = data['message_text']
            resp = cls._client.post(cls._endpoint, body)
            return cls(resp['id'], from_, to, data['message_text'])
        if cls._endpoint == '/intent/v2':
            body['ruleNameOrId'] = data['template']
            body['params'] = data['params'] or {}
            resp = cls._client.post(cls._endpoint, body)
            return cls(resp['id'], from_, to, data['template'], data['params'])
