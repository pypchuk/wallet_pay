from aiohttp import ClientSession
from .base import BaseSession
from ...methods.base import ResponseType, Method


API_BASE_URL = "https://pay.wallet.tg/wpay/store-api/v1/{}"


class AiohttpSession(BaseSession):
    def __init__(self):
        self.session = ClientSession()
        super().__init__()

    async def make_request(
        self,
        method: Method[ResponseType],
    ) -> ResponseType:
        url = API_BASE_URL.format(method.__api_method__)

        async with self.session.request(
            method.__http_method__,
            url,
            headers=self.headers,
            json=method.to_json(),
            params=method.query_params(),
        ) as r:
            return self.check_response(
                method,
                status_code=r.status,
                content=await r.text(),
            )

    async def close(self) -> None:
        await self.session.close()
