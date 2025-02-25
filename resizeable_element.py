import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Resizable.html")
time.sleep(1)  # Allow page to load

# Locate resizable element
resizable_box = driver.find_element(By.ID, "resizable")
resize_handle = driver.find_element(
    By.CSS_SELECTOR,
    ".ui-resizable-handle.ui-resizable-se.ui-icon.ui-icon-gripsmall-diagonal-se",
)

# Get initial size
initial_size = resizable_box.size
print(f"Initial Size: {initial_size}")

# Perform resize action
actions = ActionChains(driver)
actions.click_and_hold(resize_handle).move_by_offset(100, 100).release().perform()
time.sleep(1)  # Allow resizing effect to be visible

# Get resized dimensions
new_size = resizable_box.size
print(f"Resized To: {new_size}")

# Close the browser
driver.quit()
