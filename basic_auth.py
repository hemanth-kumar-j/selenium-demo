import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Get browser mode from command-line argument (default: "chrome")
headless = (
    "--headless=new" if len(sys.argv) > 1 and sys.argv[1].lower() == "headless" else ""
)

# Credentials
USERNAME = "admin"
PASSWORD = "admin"
URL = f"https://{USERNAME}:{PASSWORD}@the-internet.herokuapp.com/basic_auth"

# Set Chrome options
options = Options()
if headless:
    options.add_argument(headless)

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

# Initialize WebDriver
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Open the webpage with authentication
driver.get(URL)

# Wait for authentication to process
time.sleep(2)

# Close browser
driver.quit()
