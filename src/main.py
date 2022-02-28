from core.factories.google import GoogleSearchFactory
from core.query_parsers import ParserType
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/search")
def do_search():
    term = request.args.get("term")

    query_service = GoogleSearchFactory.get_query_service()
    query_parser = GoogleSearchFactory.get_query_parser()

    data = query_service.regular(term)
    parsed = query_parser.parse(data, ParserType.REGULAR)

    return jsonify(parsed), 200


if __name__ == "__main__":
    app.run(host="localhost", port=9091)
