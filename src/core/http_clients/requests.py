import requests
from . import HTTPClient


class RequestsHTTPClient(HTTPClient):
    def get(self, url: str):
        return requests.get(
            url,
            headers={
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
            },
        )
