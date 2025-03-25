from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Open the webpage
    driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

    # Locate the button and perform a right-click action
    button = driver.find_element(By.XPATH, "//span[text()='right click me']")
    ActionChains(driver).context_click(button).perform()

    # Click on the "Edit" option from the context menu
    sleep(1)  # Small delay for menu to appear
    driver.find_element(By.XPATH, "//span[text()='Edit']").click()

    # Handle the alert and print the text
    sleep(1)  # Allow time for the alert to appear
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()

finally:
    # Ensure driver quits even if an error occurs
    sleep(1)  # Optional delay before closing
    driver.quit()
