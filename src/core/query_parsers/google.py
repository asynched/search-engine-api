import re, json
from core.query_parsers import QueryParser, Parsers
from typing import List
from bs4 import BeautifulSoup


class GoogleQueryParser(QueryParser):
    def parse_regular(self, text: str) -> List[dict]:
        parser = BeautifulSoup(text, features="html.parser")
        regular_nodes = parser.select("div[data-sokoban-container]")
        special_nodes = parser.select("div.hlcw0c")

        parsed = []

        for node in special_nodes:
            title = node.select_one("h3").text
            content = node.select_one(
                "div.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc.lEBKkf span"
            ).text
            url = node.select_one("cite").text

            parsed.append(
                {
                    "title": title,
                    "content": content,
                    "url": url,
                }
            )

        for node in regular_nodes:
            title = node.select_one("h3").text
            content = node.select_one("div[data-content-feature]").text
            url = node.select_one("cite").text.split(" ")[0]

            parsed.append(
                {
                    "title": title,
                    "content": content,
                    "url": url,
                }
            )

        return parsed

    def parse_news(self, text: str) -> List[dict]:
        parser = BeautifulSoup(text, features="html.parser")
        nodes = parser.select("g-card")

        parsed = []

        for node in nodes:
            source = node.select_one("span").text
            source_image_url = node.select_one("img.rISBZc.zr758c")["src"]
            title = node.select_one("div[role=heading]").text
            content = node.select_one("div.GI74Re.nDgy9d").text

            parsed.append(
                {
                    "source": {
                        "name": source,
                        "image_url": source_image_url,
                    },
                    "title": title,
                    "content": content,
                }
            )

        return parsed

    def parse_images(self, text: str) -> List[dict]:
        parser = BeautifulSoup(text, features="html.parser")
        parsed = []

        for image_tag in parser.select(".isv-r.PNCib.MSM1fd.BUooTd"):
            title = image_tag.select_one(".VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb")["title"]
            source = image_tag.select_one(".fxgdke").text
            url = image_tag.select_one(".VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb")["href"]

            parsed.append({"title": title, "source": source, "url": url})

        script_tags = parser.select("script")

        images_data = "".join(
            re.findall(r"AF_initDataCallback\(([^<]+)\);", str(script_tags))
        )

        images_data_fix = json.dumps(images_data)
        images_data_json = json.loads(images_data_fix)

        # https://regex101.com/r/pdZOnW/3
        matched_google_image_data = re.findall(
            r"\[\"GRID_STATE0\",null,\[\[1,\[0,\".*?\",(.*),\"All\",",
            images_data_json,
        )

        removed_matched_google_images_thumbnails = re.sub(
            r"\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]",
            "",
            str(matched_google_image_data),
        )

        matched_google_full_resolution_images = re.findall(
            r"(?:'|,),\[\"(https:|http.*?)\",\d+,\d+\]",
            removed_matched_google_images_thumbnails,
        )

        for index, fixed_full_res_image in enumerate(
            matched_google_full_resolution_images
        ):
            original_size_img_not_fixed = bytes(fixed_full_res_image, "ascii").decode(
                "unicode-escape"
            )
            original_size_img = bytes(original_size_img_not_fixed, "ascii").decode(
                "unicode-escape"
            )

            parsed[index]["image_url"] = original_size_img

        return parsed
