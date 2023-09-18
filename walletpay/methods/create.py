from dataclasses import dataclass

from .base import Method

from ..types.money_amount import MoneyAmount

from ..types.create_response import CreateResponse


@dataclass
class Create(Method[CreateResponse]):
    __returning__ = CreateResponse
    __api_method__ = "order"
    __http_method__ = "post"

    amount: MoneyAmount
    externalId: str
    timeoutSeconds: int
    customerTelegramUserId: int
    description: str
    customData: str | None = None
    returnUrl: str | None = None
    failReturnUrl: str | None = None
