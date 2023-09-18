from walletpay.methods import GetOrderList


def test_method_compilation():
    method = GetOrderList(
        offset=10,
        count=5,
    )

    params = method.query_params()

    assert params["offset"] == 10

    assert params["count"] == 5

    assert method.to_json() is None
