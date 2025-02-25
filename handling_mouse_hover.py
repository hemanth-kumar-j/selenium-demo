import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Datepicker.html")

# Initialize ActionChains
actions = ActionChains(driver)

# Hover over "SwitchTo" menu and click "Frames" option
switch_to_menu = driver.find_element(
    By.XPATH, '//*[@id="header"]//a[contains(text(), "SwitchTo")]'
)
actions.move_to_element(switch_to_menu).perform()
time.sleep(1)  # Small delay for UI stability

driver.find_element(By.CSS_SELECTOR, "a[href='Frames.html']").click()
time.sleep(2)  # Wait for navigation

# Close the browser
driver.quit()
