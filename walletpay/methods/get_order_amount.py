from typing import Any

from dataclasses import dataclass

from ..types.order_amount import GetOrderAmount as Response

from .base import Method


@dataclass
class GetOrderAmount(Method[Response]):
    __returning__ = Response
    __api_method__ = "reconciliation/order-amount"
    __http_method__ = "get"

    def query_params(self) -> dict[str, Any] | None:
        return None

    def to_json(self) -> dict[str, Any] | None:
        return None
