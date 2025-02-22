import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

alert_button = driver.find_element(
    By.XPATH, value="//button[normalize-space()='Click for JS Alert']"
)
confirm_button = driver.find_element(
    By.XPATH, value="//button[normalize-space()='Click for JS Confirm']"
)
prompt_button = driver.find_element(
    By.XPATH, value="//button[normalize-space()='Click for JS Prompt']"
)
buttons = [alert_button, confirm_button]


def click_alert_button(button):
    time.sleep(1)
    button.click()
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    time.sleep(1)


for button in buttons:
    click_alert_button(button)
    driver.switch_to.alert.accept()

if confirm_button:
    click_alert_button(confirm_button)
    driver.switch_to.alert.dismiss()

if prompt_button:
    click_alert_button(prompt_button)
    driver.switch_to.alert.send_keys("This Is Prompt Text")
    driver.switch_to.alert.accept()
    time.sleep(1)

driver.quit()
