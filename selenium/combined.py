from gather_comments import gather_comments
from graph import graph
import sentiment_analysis

# Website must be the link to the first episode of the webtoon to scrape
website = "https://www.webtoons.com/en/romance/the-grim-reaper-is-my-guardian/ep-0-prologue/viewer?title_no=8861&episode_no=1"
info = website.split("/")
title = info[5]

gather_comments(website)
sentiment_analysis.save_data(title)
graph(title)
