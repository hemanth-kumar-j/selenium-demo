from time import sleep
from selenium import webdriver

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")  # Disable browser notifications

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Open the website
driver.get("https://whatmylocation.com/")
sleep(2)  # Wait for page to load

# Close the browser
driver.quit()
