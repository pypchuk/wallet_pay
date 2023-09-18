from __future__ import annotations
import abc
from typing import Callable, Any, Optional, Type, Final
from types import TracebackType
import json
import adaptix
from adaptix.load_error import LoadError
from walletpay.methods.base import Method, ResponseType
from ...exceptions import JsonDecodeError, ObjectLoadError, ServerError


DEFAULT_TIMEOUT: float = 60.0

_JsonLoads = Callable[..., Any]

DEFAULT_HEADERS: Final[dict[str, str]] = {
    "Wpay-Store-Api-Key": ""
}

API_BASE_URL = "https://pay.wallet.tg/wpay/store-api/v1/{}"


class BaseSession(abc.ABC):
    def __init__(
        self,
        json_loads: _JsonLoads = json.loads,
        timeout: float = DEFAULT_TIMEOUT,
        headers: dict[str, str] | None = None,
        api_endpoint: str | None = None,
    ) -> None:
        self.json_loads = json_loads
        self.timeout = timeout
        self.retort = adaptix.Retort(
            recipe=[
                adaptix.name_mapping(skip="__.*"),
                adaptix.name_mapping(map={"_with": "with"}),
            ]
        )
        self.headers = headers or DEFAULT_HEADERS
        self.endpoint = api_endpoint or API_BASE_URL

    def check_response(
        self,
        method: Method[ResponseType],
        status_code: int,
        content: str,
    ) -> ResponseType:
        try:
            json_data = self.json_loads(content)
        except Exception as e:
            raise JsonDecodeError(content) from e

        if status_code == 200:
            try:
                obj = method.build_response(json_data)
            except LoadError as e:
                raise ObjectLoadError(json_data, method.__returning__) from e
            return obj

        raise ServerError(
            status_code,
            content,
        )

    @abc.abstractmethod
    async def make_request(
        self,
        method: Method[ResponseType],
    ) -> ResponseType:
        ...

    @abc.abstractmethod
    async def close(self) -> None:
        ...

    async def __aenter__(self) -> BaseSession:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        await self.close()

    async def __call__(
        self,
        method: Method[ResponseType],
    ) -> ResponseType:
        return await self.make_request(method)
