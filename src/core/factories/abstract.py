from enum import Enum

from core.factories import SearchFactory
from core.factories.google import GoogleSearchFactory


class Providers(Enum):
    GOOGLE = 1


class AbstractSearchFactory:
    def get_factory(provider: Providers) -> SearchFactory:
        return GoogleSearchFactory
