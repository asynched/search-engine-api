from core.factories import SearchFactory
from core.http_clients import HTTPClient
from core.query_parsers import QueryParser
from core.query_services import QueryService

from core.http_clients.requests import RequestsHTTPClient

from core.query_parsers.google import GoogleQueryParser
from core.query_services.google import GoogleQueryService


class GoogleSearchFactory(SearchFactory):
    def get_query_service(
        http_client: HTTPClient = RequestsHTTPClient(),
    ) -> QueryService:
        return GoogleQueryService(http_client)

    def get_query_parser() -> QueryParser:
        return GoogleQueryParser()
