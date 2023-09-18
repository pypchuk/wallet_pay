from decimal import Decimal

from datetime import datetime, timezone

from walletpay.types import OrderList, OrderStatus, CurrencyCode
from walletpay.types.order_list import GetOrderListStatus


def test_method_compilation():
    create_response_json = {
        "status": "SUCCESS",
        "message": "",
        "data":
        {
            "items": [
                {
                    "id": 2703383946854401,
                    "status": "ACTIVE",
                    "amount": {
                        "currencyCode": "USD",
                        "amount": "1.00"
                    },
                    "externalId": "ORD-5023-4E89",
                    "customerTelegramUserId": 0,
                    "createdDateTime": "2019-08-24T14:15:22Z",
                    "expirationDateTime": "2019-08-24T14:15:22Z",
                    "paymentDateTime": "2019-08-24T14:15:22Z",
                    "selectedPaymentOption": {
                        "amount": {
                            "currencyCode": "USD",
                            "amount": "1.00"
                        },
                        "amountFee": {
                            "currencyCode": "USD",
                            "amount": "1.00"
                        },
                        "amountNet": {
                            "currencyCode": "USD",
                            "amount": "1.00"
                        },
                        "exchangeRate": "0.44"
                    }
                }
            ]
        }
    }

    response = OrderList.from_json(create_response_json)

    assert response.status == GetOrderListStatus.SUCCESS

    assert response.message == ""

    assert response.data is not None

    assert len(response.data.items) == 1

    assert response.data.items[0].id == 2703383946854401

    assert response.data.items[0].externalId == "ORD-5023-4E89"

    assert response.data.items[0].customerTelegramUserId == 0

    assert response.data.items[0].status == OrderStatus.ACTIVE

    assert response.data.items[0].amount.currencyCode == CurrencyCode.USD

    assert response.data.items[0].amount.amount == Decimal("1.00")

    assert response.data.items[0].createdDateTime == datetime(2019, 8, 24, 14, 15, 22, tzinfo=timezone.utc)

    assert response.data.items[0].expirationDateTime == datetime(2019, 8, 24, 14, 15, 22, tzinfo=timezone.utc)

    assert response.data.items[0].paymentDateTime == datetime(2019, 8, 24, 14, 15, 22, tzinfo=timezone.utc)

    assert response.data.items[0].selectedPaymentOption.exchangeRate == Decimal("0.44")
