from dataclasses import dataclass

from decimal import Decimal

from .enums import CurrencyCode


@dataclass
class MoneyAmount:
    currencyCode: CurrencyCode
    amount: Decimal
