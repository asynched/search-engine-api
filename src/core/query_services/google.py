from core.http_clients import HTTPClient
from core.query_services import QueryService


class GoogleQueryService(QueryService):
    def __init__(self, http_client: HTTPClient):
        self.http_client = http_client

    async def regular(self, term: str) -> dict:
        response = await self.http_client.get(f"https://google.com/search?q={term}")
        return response.text

    async def images(self, term: str):
        response = await self.http_client.get(
            f"https://google.com/search?q={term}&tbm=isch"
        )
        return response.text

    async def news(self, term: str):
        response = await self.http_client.get(
            f"https://google.com/search?q={term}&tbm=nws"
        )
        return response.text
