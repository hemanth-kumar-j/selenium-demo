import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Locate alert buttons
buttons = {
    "alert": driver.find_element(
        By.XPATH, "//button[normalize-space()='Click for JS Alert']"
    ),
    "confirm": driver.find_element(
        By.XPATH, "//button[normalize-space()='Click for JS Confirm']"
    ),
    "prompt": driver.find_element(
        By.XPATH, "//button[normalize-space()='Click for JS Prompt']"
    ),
}


def handle_alert(action="accept", text=None):
    """Handles alerts by accepting, dismissing, or sending text."""
    time.sleep(1)  # Small delay for UI stability
    alert = driver.switch_to.alert
    print(f"Alert Text: {alert.text}")

    if text:
        alert.send_keys(text)

    if action == "accept":
        alert.accept()
    elif action == "dismiss":
        alert.dismiss()


# Click & handle JS Alert
buttons["alert"].click()
handle_alert()

# Click & handle JS Confirm (Accept & Dismiss)
buttons["confirm"].click()
handle_alert("accept")

buttons["confirm"].click()
handle_alert("dismiss")

# Click & handle JS Prompt (Send Text & Accept)
buttons["prompt"].click()
handle_alert("accept", text="This Is Prompt Text")

# Close browser
driver.quit()
