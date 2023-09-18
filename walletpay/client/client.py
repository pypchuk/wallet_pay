from decimal import Decimal
from .session.base import BaseSession
from .session._aiohttp import AiohttpSession

from ..methods import GetPreview, GetOrderAmount, Create, GetOrderList
from ..types import GetPreviewResponse, GetOrderAmountResponse, CreateResponse, MoneyAmount, CurrencyCode, OrderList


DEFAULT_TIMEOUT_SECONDS = 60


class Client:
    def __init__(
            self,
            api_key: str,
            session: BaseSession | None = None,
    ):
        _session = session or AiohttpSession()
        _session.headers["Wpay-Store-Api-Key"] = api_key
        self.session = _session

    async def get_preview(self, _id: str) -> GetPreviewResponse:
        return await self.session(GetPreview(_id))

    async def get_order_amount(self) -> GetOrderAmountResponse:
        return await self.session(GetOrderAmount())

    async def get_order_list(self, offset: int, count: int) -> OrderList:
        return await self.session(GetOrderList(offset, count))

    async def create_order(
            self,
            money_amount: int | float | str | Decimal,
            external_id: str,
            customer_telegram_user_id: int,
            description: str,
            currency_code: CurrencyCode = CurrencyCode.TON,
            timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
            custom_data: str | None = None,
            return_url: str | None = None,
            fail_return_url: str | None = None,
    ) -> CreateResponse:
        if not isinstance(money_amount, Decimal):
            money_amount = Decimal(money_amount)

        return await self.session(
            Create(
                MoneyAmount(
                    currency_code,
                    money_amount,
                ),
                externalId=external_id,
                timeoutSeconds=timeout_seconds,
                customerTelegramUserId=customer_telegram_user_id,
                description=description,
                customData=custom_data,
                returnUrl=return_url,
                failReturnUrl=fail_return_url,
            )
        )
