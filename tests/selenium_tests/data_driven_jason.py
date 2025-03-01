import json
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

JSON_FILE = "testdata.json"
URL = "https://www.saucedemo.com/"

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def read_test_data(json_file):
    """Reads test data from JSON and returns it."""
    try:
        with open(json_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Error reading JSON file: {e}")
        return {"users": []}  # Return empty structure to avoid crashes


def login_test(driver, username, password):
    """Performs the login operation."""
    driver.get(URL)

    wait = WebDriverWait(driver, 10)  # Wait for elements to be available
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()


def main():
    """Main function to execute test cases."""
    test_data = read_test_data(JSON_FILE)

    if not test_data.get("users"):
        logging.warning("No user data found in the JSON file.")
        return

    driver = webdriver.Chrome()
    driver.maximize_window()

    for data in test_data["users"]:
        logging.info(f"Testing login for user: {data['Username']}")
        login_test(driver, data["Username"], data["Password"])

    driver.quit()


if __name__ == "__main__":
    main()
