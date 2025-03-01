from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Open Google
driver.get("https://www.google.com/")
sleep(2)

# Close browser
driver.quit()
