from flask import Flask, jsonify, request

from core.query_parsers import Parsers
from core.factories.abstract import AbstractSearchFactory, Providers

app = Flask(__name__)


@app.get("/search")
def do_search():
    term = request.args.get("term")

    search_factory = AbstractSearchFactory.get_factory(Providers.GOOGLE)

    query_service = search_factory.get_query_service()
    query_parser = search_factory.get_query_parser()

    data = query_service.regular(term)
    parsed = query_parser.parse(data, Parsers.REGULAR)

    return jsonify(parsed), 200


if __name__ == "__main__":
    app.run(host="localhost", port=9091)
