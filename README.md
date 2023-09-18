# Wallet Pay Python API
https://docs.wallet.tg/pay/

## Installation
```commandline
pip install walletpay-sdk
```

## Example
```python
import asyncio

from uuid import uuid4

from aiogram import Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from walletpay import Client


CUSTOMER_TELEGRAM_ID = 133777888


async def main():
    api = Client("YoUrApIKey")
    bot = Bot("1294789:YourBoTKey")

    # Create order
    order = await api.create_order(
        "0.001",
        external_id=str(uuid4()),
        customer_telegram_user_id=CUSTOMER_TELEGRAM_ID,
        description="Support me",
        timeout_seconds=60,
    )

    # Send order to user
    await bot.send_message(
        CUSTOMER_TELEGRAM_ID,
        "Pay",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="👛 Pay via Wallet",
                        url=order.data.payLink,
                    )
                ]
            ]
        )
    )

    await api.session.close()
    await bot.session.close()


asyncio.run(main())
```

## Requirements
1. Python >= 3.11

## Running tests
1. Clone repo  
2. From the root dir run  
```commandline
pytest tests
```

## Running examples
1. Clone repo
2. Run `poetry install --group examples`
3. Add env vars:  
3.1 Add WP_TEST_KEY with your API key  
3.2 (FOR bot.py) Add WP_BOT_TOKEN with bot token bound to your api  
4. Go to examples folder and run them like regular python scripts  

### Note about webhooks example
WARNING! For development purposes only!  
To run webhook example you need dedicated IP address  
You can use ngrok to test your application:  
1. Download ngrok and log in
2. Run `ngrok http 80`
3. Copy your temporary IP address
4. Paste it in your merchant settings
5. !AFTER DEVELOPMENT DON'T FORGET TO REMOVE ADDRESS IN WALLETPAY WEBHOOK SETTINGS PROVIDED FROM NGROK!