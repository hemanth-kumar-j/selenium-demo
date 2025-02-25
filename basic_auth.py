import time
from selenium import webdriver

# Credentials
USERNAME = "admin"
PASSWORD = "admin"
URL = f"https://{USERNAME}:{PASSWORD}@the-internet.herokuapp.com/basic_auth"

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the webpage with authentication
driver.get(URL)

# Wait for authentication to process
time.sleep(2)

# Close browser
driver.quit()
