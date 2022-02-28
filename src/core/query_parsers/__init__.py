from typing import List, Protocol
from enum import Enum


class Parsers(Enum):
    REGULAR = 1
    IMAGES = 2
    NEWS = 3

    def get_parser(type: str):
        if type == "img":
            return Parsers.IMAGES

        if type == "nws":
            return Parsers.NEWS

        return Parsers.REGULAR


class QueryParser(Protocol):
    def parse(self, text: str, type: Parsers) -> List[dict]:
        if type == Parsers.REGULAR:
            return self.parse_regular(text)
        if type == Parsers.IMAGES:
            return self.parse_images(text)
        if type == Parsers.NEWS:
            return self.parse_news(text)

    def parse_regular(self, text: str) -> List[dict]:
        ...

    def parse_news(self, text: str) -> List[dict]:
        ...

    def parse_images(self, text: str) -> List[dict]:
        ...
