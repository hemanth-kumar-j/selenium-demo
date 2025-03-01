import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

CSV_FILE = "testdata.csv"
URL = "https://www.saucedemo.com/"


def read_test_data(csv_file):
    """Reads test data from CSV and returns a list of dictionaries."""
    with open(csv_file, "r", newline="") as file:
        return list(csv.DictReader(file))


def login_test(driver, username, password):
    """Performs the login operation."""
    driver.get(URL)
    sleep(2)  # Wait for page load
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    sleep(2)  # Wait for login action


def main():
    """Main function to execute test cases."""
    test_data = read_test_data(CSV_FILE)
    print(test_data)

    driver = webdriver.Chrome()
    driver.maximize_window()

    for data in test_data:
        login_test(driver, data["Username"], data["Password"])

    driver.quit()


if __name__ == "__main__":
    main()
