from typing import Protocol, Tuple
from enum import Enum


class Queries(Enum):
    REGULAR = 1
    IMAGES = 2
    NEWS = 3

    def get_query(type: str):
        if type == "nws":
            return Queries.NEWS

        if type == "img":
            return Queries.IMAGES

        return Queries.REGULAR


class QueryService(Protocol):
    async def query(self, term: str, type: Queries) -> str:
        if type == Queries.REGULAR:
            return await self.regular(term)

        if type == Queries.IMAGES:
            return await self.images(term)

        if type == Queries.NEWS:
            return await self.news(term)

    async def regular(self, term: str) -> str:
        ...

    async def images(self, term: str) -> str:
        ...

    async def news(self, term: str) -> str:
        ...
