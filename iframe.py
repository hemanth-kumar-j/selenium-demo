import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://seleniumbase.io/demo_page/")

# Switch to iframe and extract text
iframe = driver.find_element(By.ID, "myFrame2")
driver.switch_to.frame(iframe)
iframe_text = driver.find_element(By.TAG_NAME, "h4").text
print(f"IFrame Text: {iframe_text}")

# Switch back to the main content
driver.switch_to.default_content()
time.sleep(2)

# Interact with text input field
text_editor = driver.find_element(By.ID, "myTextInput2")
text_editor.clear()
text_editor.send_keys("Pre-Filled Text Field")

# Small delay before closing
time.sleep(2)
driver.quit()
