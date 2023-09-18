from typing import Any


class APIError(Exception):
    ...


class CheckResponseError(APIError):
    ...


class JsonDecodeError(CheckResponseError):
    def __init__(
            self,
            content: str,
    ) -> None:
        self.content = content

    def __str__(self) -> str:
        return f"Can't decode str to json, content:\n{self.content}"


class ObjectLoadError(CheckResponseError):
    def __init__(
            self,
            json_data: Any,
            response_type: type,
    ) -> None:
        self.json_data = json_data
        self.response_type = response_type

    def __str__(self) -> str:
        return f"Can't load json as response object of type {self.response_type}\nJson data:\n{self.json_data}"


class ServerError(CheckResponseError):
    def __init__(
            self,
            status_code: int,
            content: str,
    ) -> None:
        self.status_code = status_code
        self.content = content

    def __str__(self) -> str:
        return f"[{self.status_code}]: Server error, {self.content}"
