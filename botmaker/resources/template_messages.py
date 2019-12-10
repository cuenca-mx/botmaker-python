from dataclasses import dataclass, field

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
        check_phone: bool = True,
        **params,
    ):
        """
        Based on
        https://botmakeradmin.github.io/docs/es/#/messages-api?id=templates-messages
        """
        return cls.commonCreate(
            from_,
            to,
            chat_platform,
            check_phone,
            template=template,
            params=params,
        )
