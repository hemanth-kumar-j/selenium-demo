from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# Open the website
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Logout
driver.find_element(By.ID, "react-burger-menu-btn").click()
driver.find_element(By.ID, "logout_sidebar_link").click()

# Verify login field is present (optional assertion)
assert driver.find_element(By.ID, "user-name"), "Login field not found after logout"

# Close the browser
driver.quit()
