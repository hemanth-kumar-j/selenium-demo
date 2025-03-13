import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
browser = webdriver.Chrome()
browser.maximize_window()

# Open the webpage
url = "https://jqueryui.com/"
browser.get(url)

# Get all links on the page
all_links = browser.find_elements(By.TAG_NAME, "a")
print(f"Total number of links on the page: {len(all_links)}")


# Function to check for broken links
def check_broken_link(href, session):
    """Checks if a link is broken by sending a request and verifying the status code."""
    if not href:  # Skip empty or None links
        return

    try:
        response = session.get(href, timeout=5)  # Set a timeout to avoid hanging
        if response.status_code >= 400:
            print(f"Broken link: {href} (Status Code: {response.status_code})")
    except requests.RequestException as e:
        print(f"Error checking link {href}: {e}")


# Use a single session for efficient requests
with requests.Session() as session:
    for link in all_links:
        check_broken_link(link.get_attribute("href"), session)

# Close the browser
browser.quit()
