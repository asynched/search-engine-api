from typing import List, Protocol
from enum import Enum


class Parser(Enum):
    REGULAR = 1
    IMAGES = 2
    NEWS = 3


class QueryParser(Protocol):
    def parse(self, text: str, type: Parser) -> List[dict]:
        ...

    def parse_regular(self, text: str) -> List[dict]:
        ...

    def parse_news(self, text: str) -> List[dict]:
        ...

    def parse_images(self, text: str) -> List[dict]:
        ...