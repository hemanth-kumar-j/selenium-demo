import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open Selenium website
driver.get("https://www.selenium.dev/")
time.sleep(2)

# Open Playwright website in a new tab
driver.switch_to.new_window()
driver.get("https://playwright.dev/")

# Get tab details
tabs = driver.window_handles
current_tab = driver.current_window_handle

print(f"Total number of tabs: {len(tabs)}")
print(f"Tab handles: {tabs}")
print(f"Current tab handle: {current_tab}")

# Click "Get Started" button on Playwright site
try:
    driver.find_element(By.CSS_SELECTOR, ".getStarted_Sjon").click()
except Exception as e:
    print(f"Error: {e}")

time.sleep(2)

# Switch back to the first tab (Selenium site) and interact with it
if current_tab != tabs[0]:
    driver.switch_to.window(tabs[0])
    try:
        driver.find_element(By.ID, "navbarDropdown").click()
    except Exception as e:
        print(f"Error: {e}")

time.sleep(2)
driver.quit()
