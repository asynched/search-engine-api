from ..factories import SearchFactory
from ..http_clients import HTTPClient
from ..query_parsers import QueryParser
from ..query_services import QueryService

from ..http_clients.requests import RequestsHTTPClient

from ..query_parsers.google import GoogleQueryParser
from ..query_services.google import GoogleQueryService


class GoogleSearchFactory(SearchFactory):
    def get_query_service(
        http_client: HTTPClient = RequestsHTTPClient(),
    ) -> QueryService:
        return GoogleQueryService(http_client)

    def get_query_parser() -> QueryParser:
        return GoogleQueryParser()
