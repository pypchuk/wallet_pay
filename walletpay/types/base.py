from typing import Any


class Response:
    ...

    @classmethod
    def from_json(cls, json: dict[str, Any]) -> "Response":
        raise NotImplementedError
