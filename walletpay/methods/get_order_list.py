from typing import Any

from dataclasses import dataclass

from ..types.order_list import OrderList

from .base import Method


@dataclass
class GetOrderList(Method[OrderList]):
    __returning__ = OrderList
    __api_method__ = "reconciliation/order-list"
    __http_method__ = "get"

    offset: int
    count: int

    def query_params(self) -> dict[str, Any]:
        return {
            "offset": self.offset,
            "count": self.count
        }

    def to_json(self) -> dict[str, Any] | None:
        return None
