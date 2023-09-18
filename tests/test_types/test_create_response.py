from decimal import Decimal

from datetime import datetime, timezone

from walletpay.types import CreateResponse, CreateStatus, OrderStatus, CurrencyCode


def test_method_compilation():
    create_response_json = {
        "status": "SUCCESS",
        "message": "",
        "data": {
            "id": 2703383946854401,
            "status": "ACTIVE",
            "number": "9aeb581c",
            "amount": {
                "currencyCode": "USD",
                "amount": "1.00"
            },
            "createdDateTime": "2019-08-24T14:15:22Z",
            "expirationDateTime": "2019-08-24T14:15:22Z",
            "completedDateTime": "2019-08-24T14:15:22Z",
            "payLink": "https://t.me/wallet?startattach=wpay_order_2703383946854401",
            "directPayLink": "https://t.me/wallet/start?startapp=wpay_order-orderId__2703383946854401"
        }
    }

    response = CreateResponse.from_json(create_response_json)

    assert response.status == CreateStatus.SUCCESS

    assert response.message == ""

    assert response.data is not None

    assert response.data.id == "2703383946854401"

    assert response.data.status == OrderStatus.ACTIVE

    assert response.data.number == "9aeb581c"

    assert response.data.amount.currencyCode == CurrencyCode.USD

    assert response.data.amount.amount == Decimal("1.00")

    assert response.data.createdDateTime == datetime(2019, 8, 24, 14, 15, 22, tzinfo=timezone.utc)

    assert response.data.expirationDateTime == datetime(2019, 8, 24, 14, 15, 22, tzinfo=timezone.utc)

    assert response.data.completedDateTime == datetime(2019, 8, 24, 14, 15, 22, tzinfo=timezone.utc)

    assert response.data.payLink == "https://t.me/wallet?startattach=wpay_order_2703383946854401"

    assert response.data.directPayLink == "https://t.me/wallet/start?startapp=wpay_order-orderId__2703383946854401"
