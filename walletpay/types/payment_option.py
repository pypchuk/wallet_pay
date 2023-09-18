from decimal import Decimal

from dataclasses import dataclass

from .money_amount import MoneyAmount


@dataclass
class PaymentOption:
    amount: MoneyAmount
    amountFee: MoneyAmount
    amountNet: MoneyAmount
    exchangeRate: Decimal
