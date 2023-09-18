import asyncio
from os import environ
from uuid import uuid4

from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.command import Command

from walletpay import Client
from walletpay.exceptions import ServerError


router = Router()


@router.message((Command("start")))
async def _(m: Message) -> None:
    await m.answer("Pay Bot")


@router.message((Command("pay")))
async def _(m: Message) -> None:
    api = Client(environ.get("WP_TEST_KEY"))

    try:
        r = await api.create_order(
            "0.001",
            external_id=str(uuid4()),
            customer_telegram_user_id=m.from_user.id,
            description="Support me",
            timeout_seconds=60,
        )
    except ServerError as e:
        await m.answer(f"Server responded with {e.status_code}, reason: {e.content}")
        await api.session.close()
        return

    await m.answer(
        "Pay",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="👛 Pay via Wallet",
                            url=r.data.payLink,
                        )
                    ]
                ]
            )
    )

    await api.session.close()


async def main() -> None:
    bot = Bot(
        token=environ.get("WP_BOT_TOKEN"),
        parse_mode="html"
    )
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)

asyncio.run(main())
