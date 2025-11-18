import scrapy
import json
import re

class WebtoonCommentsSpider(scrapy.Spider):
    name = "webtoon_comments"

    def start_requests(self):
        title_id = 3596
        episode_no = 1  

        api_url = (
            "https://global.apis.naver.com/commentBox/cbox/web_neo_list_jsonp.json?"
            f"ticket=WEBTOON&templateId=default&pool=cbox2&lang=en&pageSize=100&page=1&objectId={title_id}_{episode_no}"
        )

        yield scrapy.Request(
            api_url,
            headers={
                "User-Agent": "Mozilla/5.0",
                "Referer": f"https://www.webtoons.com/en/fantasy/the-greatest-estate-developer/episode-{episode_no}/viewer?title_no={title_id}&episode_no={episode_no}",
            },
            callback=self.parse_comments
        )

    def parse_comments(self, response):
        # Extract JSON from JSONP callback
        json_text = re.search(r"\((.*)\)$", response.text).group(1)
        data = json.loads(json_text)

        for c in data["result"].get("commentList", []):
            yield {
                "user": c["userName"],
                "content": c["contents"],
                "likes": c["sympathyCount"]
            }
