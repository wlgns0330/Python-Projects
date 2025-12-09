from gather_comments import gather_comments
from graph import graph
import sentiment_analysis

# Website must be the link to the first episode of the webtoon to scrape
website = "https://www.webtoons.com/en/romance/seasons-of-lovesome/episode-1/viewer?title_no=6881&episode_no=1"
info = website.split("/")
title = info[5]

gather_comments(website)
sentiment_analysis.save_data(title)
graph(title)
