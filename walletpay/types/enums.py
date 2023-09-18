from enum import Enum


class CreateStatus(Enum):
    SUCCESS = "SUCCESS"
    ALREADY = "ALREADY"
    CONFLICT = "CONFLICT"
    ACCESS_DENIED = "ACCESS_DENIED"
    INVALID_REQUEST = "INVALID_REQUEST"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class GetPreviewStatus(Enum):
    SUCCESS = "SUCCESS"
    INVALID_REQUEST = "INVALID_REQUEST"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class CurrencyCode(Enum):
    TON = "TON"
    BTC = "BTC"
    USDT = "USDT"
    EUR = "EUR"
    USD = "USD"
    RUB = "RUB"


class OrderStatus(Enum):
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    PAID = "PAID"
    CANCELLED = "CANCELLED"


class GetOrderListStatus(Enum):
    SUCCESS = "SUCCESS"
    INVALID_REQUEST = "INVALID_REQUEST"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class GetOrderAmountStatus(Enum):
    SUCCESS = "SUCCESS"
    INVALID_REQUEST = "INVALID_REQUEST"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class UpdateType(Enum):
    ORDER_FAILED = "ORDER_FAILED"
    ORDER_PAID = "ORDER_PAID"
