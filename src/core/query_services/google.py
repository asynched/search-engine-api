from ..http_clients import HTTPClient
from ..query_services import QueryService


class GoogleQueryService(QueryService):
    def __init__(self, http_client: HTTPClient):
        self.http_client = http_client

    def regular(self, term: str) -> dict:
        response = self.http_client.get(f"https://google.com/search?q={term}")
        return response.text

    def images(self, term: str):
        response = self.http_client.get(f"https://google.com/search?q={term}&tbm=isch")
        return response.text

    def news(self, term: str):
        response = self.http_client.get(f"https://google.com/search?q={term}&tbm=nws")
        return response.text
