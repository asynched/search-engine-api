from . import QueryParser, ParserType
from typing import List
from bs4 import BeautifulSoup


class GoogleQueryParser(QueryParser):
    def parse(self, text: str, type: ParserType) -> List[dict]:
        if type == ParserType.REGULAR:
            return self.parse_regular(text)
        return []

    def parse_regular(self, text: str) -> List[dict]:
        parser = BeautifulSoup(text, features="html.parser")
        nodes = parser.select("div[data-sokoban-container]")

        parsed = []

        for node in nodes:
            title = node.select_one("h3").text
            content = node.select_one("div[data-content-feature]").text
            url = node.select_one("cite").text.split(" ")[0]

            parsed.append({"title": title, "content": content, "url": url})

        return parsed
