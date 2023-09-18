from typing import Any, TypeVar, Generic, cast

from adaptix import Retort


ResponseType = TypeVar("ResponseType", bound=Any)


class Method(Generic[ResponseType]):
    __returning__: type
    __api_method__: str
    __http_method__: str

    def query_params(self) -> dict[str, Any] | None:
        return None

    def to_json(self) -> dict[str, Any] | None:
        retort = Retort()

        return cast(dict[str, Any], retort.dump(self))

    def build_response(self, json: dict[str, Any]) -> ResponseType:
        return self.__returning__.from_json(json)  # type: ignore
