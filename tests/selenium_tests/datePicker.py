from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta


def setup_driver():
    """Initialize the WebDriver and open the datepicker page."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://jqueryui.com/datepicker/")
    return driver


def switch_to_datepicker_frame(driver):
    """Switch to the datepicker iframe."""
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))


def select_date(driver, day, month, year, navigation_class):
    """Select a specific date in the jQuery datepicker."""
    driver.find_element(By.ID, "datepicker").click()

    while True:
        dp_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
        dp_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

        if dp_month == month and str(dp_year) == str(year):
            break
        driver.find_element(By.CLASS_NAME, navigation_class).click()

    # Click the required date
    for date in driver.find_elements(
        By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td/a"
    ):
        if date.text == day:
            date.click()
            break


def get_selected_date(driver):
    """Retrieve the selected date from the datepicker input."""
    return driver.find_element(By.ID, "datepicker").get_attribute("value")


def main():
    driver = setup_driver()
    switch_to_datepicker_frame(driver)
    today = datetime.today()

    # Select previous date (previous day, previous month, previous year)
    pre_date = today - timedelta(days=1)
    pre_day = str(pre_date.day)
    pre_month_num = today.month - 1 if today.month > 1 else 12
    pre_month = datetime(today.year, pre_month_num, 1).strftime("%B")
    pre_year = today.year - 1
    # pre_year = today.year if today.month > 1 else today.year - 1  # Fix: Only decrease year if January
    select_date(driver, pre_day, pre_month, pre_year, "ui-datepicker-prev")
    print("Selected previous date:", get_selected_date(driver))

    # Refresh and re-enter frame
    driver.refresh()
    switch_to_datepicker_frame(driver)

    # Select future date (next day, next month, next year)
    next_date = today + timedelta(days=1)
    next_day = str(next_date.day)
    next_month_num = today.month + 1 if today.month < 12 else 1
    next_month = datetime(today.year, next_month_num, 1).strftime("%B")
    next_year = today.year + 1
    select_date(driver, next_day, next_month, next_year, "ui-datepicker-next")
    print("Selected future date:", get_selected_date(driver))

    driver.quit()


if __name__ == "__main__":
    main()
