import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
url = "https://jqueryui.com/"
browser.maximize_window()
browser.get(url)

all_links = browser.find_elements(By.TAG_NAME, value="a")
print(f"Total number of links on the page: {len(all_links)}")

for link in all_links:
    href = link.get_attribute("href")
    response = requests.get(href)
    if response.status_code >= 400:
        print(f"Broken link: {href}(status_code: {response.status_code})")

browser.quit()
