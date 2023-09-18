from os import environ

from aiohttp.web import run_app
from aiohttp.web_app import Application

from aiohttp.web_request import Request
from aiohttp.web_response import Response

from walletpay.types.update import Update

app = Application()


async def webhook(request: Request) -> Response:
    headers = request.headers

    text = await request.text()

    sign = Update.compute_signature(
        environ.get("WP_TEST_KEY"),
        request.method,
        request.path,
        timestamp=headers["WalletPay-Timestamp"],
        body=text,
    )

    wp_sign = headers["WalletPay-Signature"]

    print(sign, wp_sign, wp_sign == sign)

    return Response()

app.router.add_post("/", webhook)

run_app(app, host="localhost", port=80)
