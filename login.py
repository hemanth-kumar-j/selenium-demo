from selenium import webdriver
from selenium.webdriver.common.by import By

# Constants
LOGIN_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(LOGIN_URL)

# Locate input fields & login button
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# Perform login actions
username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
assert not login_button.get_attribute("disabled"), "Login button should not be disabled"
login_button.click()

# Verify successful login
success_element = driver.find_element(By.CSS_SELECTOR, ".title")
assert success_element.text == "Products", "Login failed or incorrect page loaded"

# Print page title
print(f"Page title is: {driver.title}")

# Close browser
driver.quit()
