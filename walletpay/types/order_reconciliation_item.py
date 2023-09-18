from typing import Any

from dataclasses import dataclass

from datetime import datetime

from adaptix import Retort

from .money_amount import MoneyAmount
from .payment_option import PaymentOption
from .enums import OrderStatus


@dataclass
class OrderReconciliationItem:
    id: int
    status: OrderStatus
    amount: MoneyAmount
    externalId: str
    createdDateTime: datetime
    expirationDateTime: datetime
    customerTelegramUserId: int | None = None
    paymentDateTime: datetime | None = None
    selectedPaymentOption: PaymentOption | None = None

    @classmethod
    def from_json(cls, json: dict[str, Any]) -> "OrderReconciliationItem":
        retort = Retort()

        return retort.load(json, cls)
