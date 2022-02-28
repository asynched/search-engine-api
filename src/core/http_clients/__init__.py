from typing import Protocol
from requests import Response


class HTTPClient(Protocol):
    async def get(self, url: str) -> str:
        ...
