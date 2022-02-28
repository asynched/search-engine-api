from typing import Protocol
from core.query_parsers import QueryParser
from core.query_services import QueryService


class SearchFactory(Protocol):
    def get_query_service() -> QueryService:
        ...

    def get_query_parser() -> QueryParser:
        ...
