from botmaker.exc import BotmakerException, InvalidPhoneNumber
from botmaker.helpers import sanitize_phone_number

from .base import Resource


class TemplateMessage(Resource):
    _endpoint = '/intent/v2'

    def __init__(
            self,
            id: str,
            from_: str,
            to: str,
            template: str,
            params: dict,
            **kwargs
    ):
        self.id = id
        self.from_ = from_
        self.to = to
        self.template = template
        self.params = params
        super().__init__(**kwargs)

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
            check_dict = cls._client.check_whatsapp_contacts(from_, [to])
            if to not in check_dict:
                raise InvalidPhoneNumber(
                    f"'{to} is not from valid WhatsApp contact")
            else:
                to = check_dict[to]
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
