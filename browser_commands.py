import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)
driver.find_element(
    By.CSS_SELECTOR, value=".oxd-text.oxd-text--p.orangehrm-login-forgot-header"
).click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.quit()
