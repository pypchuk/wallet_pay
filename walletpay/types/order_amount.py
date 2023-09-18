from typing import Any

from dataclasses import dataclass

from adaptix import Retort, loader, P

from .order_preview import OrderPreview

from .enums import GetOrderAmountStatus


@dataclass
class OrderAmount:
    totalAmount: int

@dataclass
class GetOrderAmount:
    status: GetOrderAmountStatus
    message: str | None = None
    data: OrderAmount | None = None

    @classmethod
    def from_json(cls, json: dict[str, Any]) -> "GetOrderAmount":
        retort = Retort(
            recipe=[
                loader(P[OrderPreview], lambda x: OrderPreview.from_json(x) if x is not None else None),
            ],
        )

        return retort.load(json, cls)
