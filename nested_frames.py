from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/nested_frames")

# Switching to TOP Frame

driver.switch_to.frame("frame-top")

# Switching to MIDDLE Frame

driver.switch_to.frame("frame-middle")

content = driver.find_element(By.ID, value="content").text
print("Content in middle frame", content)

# Switching to Default Content

driver.switch_to.default_content()

# Switching to Bottom Frame

driver.switch_to.frame("frame-bottom")

content_bottom = driver.find_element(By.TAG_NAME, value="body").text
print("Content in bottom frame", content_bottom)

driver.quit()
