from __future__ import annotations
import hmac
import hashlib
from base64 import b64encode
from typing import Any

from datetime import datetime

from dataclasses import dataclass

from adaptix import Retort

from .money_amount import MoneyAmount
from .payment_option import PaymentOption
from .enums import UpdateType, OrderStatus



@dataclass
class UpdatePayload:
    id: int
    number: str
    externalId: str
    orderAmount: MoneyAmount
    orderCompletedDateTime: datetime
    status: OrderStatus | None = None
    customData: str | None = None
    selectedPaymentOption: PaymentOption | None = None


@dataclass
class Update:
    eventDateTime: datetime 
    eventId: int
    type: UpdateType
    payload: UpdatePayload

    @classmethod
    def from_json(cls, json: dict[str, Any]) -> list["Update"]:
        retort = Retort()

        return retort.load(json, list[Update])

    @staticmethod
    def compute_signature(
        api_key: str,
        method: str,
        uri: str,
        timestamp: str,
        body: str,
    ) -> str:
        encoded64 = b64encode(body.encode()).decode()

        sign = f"{method}.{uri}.{timestamp}.{encoded64}"

        _hmac = hmac.new(
            api_key.encode(),
            sign.encode(),
            digestmod=hashlib.sha256
        )

        return b64encode(_hmac.digest()).decode()
