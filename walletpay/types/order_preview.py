from typing import Any

from dataclasses import dataclass

from datetime import datetime

from adaptix import Retort, loader, P

from .money_amount import MoneyAmount

from .enums import OrderStatus


@dataclass
class OrderPreview:
    id: str
    status: OrderStatus
    number: str
    amount: MoneyAmount
    createdDateTime: datetime
    expirationDateTime: datetime
    payLink: str
    directPayLink: str
    completedDateTime: datetime | None = None

    @classmethod
    def from_json(cls, json: dict[str, Any]) -> "OrderPreview":
        retort = Retort(
            recipe=[
                loader(P[OrderPreview].id, lambda x: str(x)),
            ],
        )

        return retort.load(json, cls)
