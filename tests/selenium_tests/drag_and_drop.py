import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")

# Wait for elements to load
time.sleep(2)

# Locate source and target elements
source = driver.find_element(By.ID, "column-a")
target = driver.find_element(By.ID, "column-b")

# Perform drag-and-drop action
ActionChains(driver).drag_and_drop(source, target).perform()

# Pause for visibility
time.sleep(2)

# Close browser
driver.quit()
