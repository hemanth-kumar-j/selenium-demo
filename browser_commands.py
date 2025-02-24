import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")


# Define a short wait function
def wait(seconds=2):
    time.sleep(seconds)


# Click on "Forgot Password"
wait(5)
forgot_password = driver.find_element(
    By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header"
)
forgot_password.click()

# Navigate browser history
wait(5)
driver.back()

wait(5)
driver.forward()

wait(5)
driver.refresh()

# Close browser
wait(5)
driver.quit()
