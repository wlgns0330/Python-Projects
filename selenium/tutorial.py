from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

website = 'https://www.webtoons.com/en/romance/marriage-of-convenience/episode-1/viewer?title_no=8959&episode_no=1'
path = r"C:\Users\wlgns\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(path)
driver = webdriver.Chrome(service=service)
driver.get(website)

time.sleep(5)

comments = driver.find_elements(By.CLASS_NAME, "wcc_TextContent__content")

for comment in comments:
    text = comment.text.strip()
    print(text)

# Keep browser open until user presses Enter
input("Press Enter to close the browser...")
driver.quit()