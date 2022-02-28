import time
from lib.cache import Cache
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks

from core.query_parsers import Parsers
from core.factories.abstract import AbstractSearchFactory, Providers
from core.query_services import Queries
from lib.functional import compose
from lib.loggers import Logger

app = FastAPI()
logger = Logger()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cache = Cache({})


@app.get("/search")
async def search(
    term: str = "",
    type: str = "regular",
):
    start_time = time.perf_counter()
    cache_key = f"{type}:{term}"
    cached_query = cache.get(cache_key)

    if cached_query:
        end_time = time.perf_counter()
        logger.info(f"Cache: {cache}")
        logger.info(
            f"Querying for term '{term}' of type '{type}' took {end_time - start_time:.2f}s."
        )

        return cached_query

    logger.info("Instantiating query service and parser")

    search_factory = AbstractSearchFactory.get_factory(Providers.GOOGLE)
    query_service = search_factory.get_query_service()
    query_parser = search_factory.get_query_parser()

    query = Queries.get_query(type)
    parser = Parsers.get_parser(type)

    logger.info(f"Querying for term: '{term}'")
    data = await query_service.query(term, query)

    logger.info(f"Parsing query with parser of type: '{type}'")

    parsed = query_parser.parse(data, parser)

    cache[cache_key] = parsed

    end_time = time.perf_counter()

    query_time = end_time - start_time

    logger.info(
        f"Querying for term '{term}' of type '{type}' took {end_time - start_time:.2f}s."
    )

    return parsed
