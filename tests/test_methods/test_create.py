from decimal import Decimal

from walletpay.methods.create import Create
from walletpay.types import MoneyAmount, CurrencyCode


def test_method_compilation():
    method = Create(
        MoneyAmount(
            CurrencyCode.USD,
            Decimal("1.00")
        ),
        description="VPN for 1 month",
        returnUrl="https://t.me/wallet",
        failReturnUrl="https://t.me/wallet",
        customData="client_ref=4E89",
        externalId="ORD-5023-4E89",
        timeoutSeconds=10800,
        customerTelegramUserId=0,
    )

    json_structure = method.to_json()

    expected_structure = {
          "amount": {
            "currencyCode": "USD",
            "amount": "1.00"
          },
          "description": "VPN for 1 month",
          "returnUrl": "https://t.me/wallet",
          "failReturnUrl": "https://t.me/wallet",
          "customData": "client_ref=4E89",
          "externalId": "ORD-5023-4E89",
          "timeoutSeconds": 10800,
          "customerTelegramUserId": 0
    }

    assert json_structure == expected_structure

    assert method.query_params() is None
