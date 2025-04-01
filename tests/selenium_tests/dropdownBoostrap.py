import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Initialize WebDriver
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    return driver


# Select a random country from the dropdown
def select_random_country(driver):
    wait = WebDriverWait(driver, 5)
    driver.find_element(By.ID, "select2-billing_country-container").click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='select2-billing_country-results']/li")
        )
    )
    country_list = driver.find_elements(
        By.XPATH, "//*[@id='select2-billing_country-results']/li"
    )

    print(f"Number of countries available: {len(country_list)}")

    selected_country = random.choice(country_list).text
    print(f"Randomly selected country: {selected_country}")

    for country in country_list:
        if country.text == selected_country:
            country.click()
            break

    return selected_country


# Verify the selected country
def verify_selection(driver, expected_country):
    wait = WebDriverWait(driver, 5)
    selected_dropdown = driver.find_element(By.ID, "select2-billing_country-container")
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "select2-billing_country-container"), expected_country
        )
    )

    selected_country = selected_dropdown.text
    assert (
        selected_country == expected_country
    ), f"Expected {expected_country}, but got {selected_country}"
    print(f"Selected country: {selected_country}")


# Main execution
def main():
    driver = setup_driver()
    try:
        selected_country = select_random_country(driver)
        verify_selection(driver, selected_country)
        sleep(2)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
