from abc import abstractmethod
from typing import Optional

from typing_extensions import Protocol


class BaseClient(Protocol):
    @abstractmethod
    def check_whatsapp_contact(
        self, channel: str, phone_number: str
    ) -> Optional[str]:
        ...

    @abstractmethod
    def post(self, endpoint: str, data: dict, **kwargs) -> dict:
        ...
