from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver (for Chrome)
driver = webdriver.Chrome()
driver.maximize_window()
username = "standard_user"
password = "secret_sauce"
login_url = "https://www.saucedemo.com/"
driver.get(login_url)
# Open a website
# driver.get("https://www.google.com")
# driver.get("http://selenium.dev/")
username_field = driver.find_element(By.ID, value="user-name")
password_field = driver.find_element(By.ID, value="password")

username_field.send_keys(username)
password_field.send_keys(password)

login_button = driver.find_element(By.ID, value="login-button")
assert not login_button.get_attribute("disabled")
login_button.click()

success_element = driver.find_element(By.CSS_SELECTOR, value=".title")
assert success_element.text == "Products"

# Print the page title
title = driver.title
print("Page title is:", title)
# assert "Selenium" in title

# Close the browser
driver.quit()
