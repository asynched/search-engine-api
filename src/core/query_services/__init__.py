from typing import Protocol


class QueryService(Protocol):
    def regular(self, term: str):
        ...

    def images(self, term: str):
        ...

    def news(self, term: str):
        ...
