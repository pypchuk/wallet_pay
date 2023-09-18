from typing import Any

from dataclasses import dataclass

from adaptix import Retort

from .order_reconciliation_item import OrderReconciliationItem
from .enums import GetOrderListStatus


@dataclass
class Data:
    items: list[OrderReconciliationItem]


@dataclass
class OrderList:
    status: GetOrderListStatus
    message: str | None = None
    data: Data | None = None

    @classmethod
    def from_json(cls, json: dict[str, Any]) -> "OrderList":
        retort = Retort()

        return retort.load(json, cls)
