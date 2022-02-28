from aiohttp import ClientSession
from core.http_clients import HTTPClient


class AIOHTTPClient(HTTPClient):
    async def get(self, url: str) -> str:
        async with ClientSession(
            headers={
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
            }
        ) as session:
            async with session.get(url) as response:
                return await response.text("utf-8")
