from typing import Protocol
from requests import Response


class HTTPClient(Protocol):
    def get(self, url: str) -> Response:
        ...
