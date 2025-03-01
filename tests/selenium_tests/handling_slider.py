import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/horizontal_slider")

# Wait for the page to load
time.sleep(1)

# Locate the slider element
slider = driver.find_element(By.XPATH, '//*[@id="content"]//input[@type="range"]')

# Move the slider
actions = ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(46, 0).release().perform()

# Wait to observe the movement
time.sleep(2)

# Close the browser
driver.quit()
