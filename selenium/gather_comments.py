from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import time
import os


def gather_comments(website):
    # Open browser without actually showing browser
    options = Options()
    options.add_argument("--headless")               # Run Chrome in headless mode
    options.add_argument("--disable-gpu")            # Optional
    options.add_argument("--window-size=1920,1080")  # Optional

    # Create selenium element
    path = r"C:\Users\wlgns\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    service = Service(path)
    driver = webdriver.Chrome(service=service, options=options)

    # Get webtoon information
    info = website.split("/")
    title = info[5]

    # Start actual algorithm
    print("Currently grabbing comments.")

    # Create dictionary of episode : comments
    dictionary = {}

    while website:
        # Create dictionary key:value pair
        info = website.split("/")
        episode = info[6]
        dictionary[episode] = []

        # Wait until comments load
        driver.get(website)
        time.sleep(2)

        # Grab comments
        comments = driver.find_elements(By.CLASS_NAME, "wcc_TextContent__content")

        # Grab only text and filter "TOP"
        for comment in comments:
            comment_line = comment.text.strip()
            if "TOP" not in comment_line :
                dictionary[episode].append(comment_line)

        print("Comment grabbed for:", episode)
            
        try:
            website = driver.find_element(By.CSS_SELECTOR, 'a.pg_next._nextEpisode').get_attribute("href")
        except:
            website = None

    # Create directory to save comments in
    base_dir = os.path.join("Comment_Analysis", title)
    os.makedirs(base_dir, exist_ok=True)
    filepath = os.path.join(base_dir, "comments.txt")

    with open(filepath, 'w', encoding="utf-8") as f:
        json.dump(dictionary, f, indent=2, ensure_ascii=False)

    print("Program finished!")