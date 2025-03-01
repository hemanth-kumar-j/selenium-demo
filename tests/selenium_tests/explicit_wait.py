from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()

# Open the website
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "react-burger-menu-btn").click()

# Logout
wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
wait.until(EC.visibility_of_element_located((By.ID, "user-name")))

# Verify login field is present (optional assertion)
assert driver.find_element(By.ID, "user-name"), "Login field not found after logout"

# Close the browser
driver.quit()
