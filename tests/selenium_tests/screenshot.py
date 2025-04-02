import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Open the target website
    driver.get("https://demo.nopcommerce.com/")

    # Wait until the target element is present
    wait = WebDriverWait(driver, 10)
    element_xpath = "//div[@aria-label='1 / 2']//*[@class='slider-img']"
    wait.until(EC.presence_of_element_located((By.XPATH, element_xpath)))

    # Capture and save screenshot
    screenshot_path = os.path.join(os.getcwd(), "nopcommerce.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot taken and saved at: {screenshot_path}")

finally:
    # Close the WebDriver
    driver.quit()
