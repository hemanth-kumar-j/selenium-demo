import sys
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/datepicker/")
wait = WebDriverWait(driver, 10)


def click_datepicker_after_closing_popup(index):
    """Closes an attention popup (if present) and switches to the date picker iframe."""
    # Close popup if present
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, f"(//a[@class='close_img'])[{index}]")
        )
    ).click()

    # Switch to the date picker iframe
    dropdown_date_frame = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, f"(//iframe[@class='demo-frame lazyloaded'])[{index}]")
        )
    )
    driver.switch_to.frame(dropdown_date_frame)

    # Click on the date picker input field
    time.sleep(2)
    driver.find_element(By.ID, "datepicker").click()

    # Get current and next date
    current_date = datetime.now()
    next_date = current_date + timedelta(days=1)

    return current_date, next_date


def handle_simple_datepicker():
    """Handles the Simple Date Picker by selecting the next day's date."""
    current_date, next_date = click_datepicker_after_closing_popup(1)

    # Format date as MM/DD/YYYY and enter it
    formatted_date = next_date.strftime("%m/%d/%Y")
    driver.find_element(By.ID, "datepicker").send_keys(formatted_date + Keys.TAB)

    time.sleep(2)
    selected_date = driver.find_element(By.ID, "datepicker").get_attribute("value")
    print(f"Simple Date Picker: {selected_date}")

    driver.switch_to.default_content()


def handle_dropdown_datepicker():
    """Handles the Dropdown Date Picker by selecting the next day's date manually."""
    driver.find_element(By.XPATH, "//li[@id='DropDown DatePicker']").click()
    current_date, next_date = click_datepicker_after_closing_popup(2)

    time.sleep(2)

    # Extract date components
    next_day = str(next_date.day)
    current_month = datetime.now().month
    current_year = current_date.year
    next_month = current_month % 12

    # Select Month
    Select(
        driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-month")
    ).select_by_value(str(next_month))

    # Select Year
    Select(driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-year")).select_by_value(
        str(current_year)
    )

    # Select Day
    driver.find_element(By.LINK_TEXT, next_day).click()

    time.sleep(2)
    selected_date = driver.find_element(By.ID, "datepicker").get_attribute("value")
    print(f"Dropdown Date Picker: {selected_date}")

    driver.switch_to.default_content()


# Run test cases based on command-line arguments
if __name__ == "__main__":
    test_cases = {
        "simple": handle_simple_datepicker,
        "dropdown": handle_dropdown_datepicker,
    }

    args = sys.argv[1:]  # Get all command-line arguments (excluding script name)

    if not args:
        # If no arguments are given, run ALL test cases automatically
        print("\n🔹 No test case specified. Running ALL test cases...")
        for test in test_cases.values():
            test()
    else:
        for test_name in args:
            if test_name in test_cases:
                print(f"\n🔹 Running Test: {test_name}")
                test_cases[test_name]()
            else:
                print(f"❌ Invalid test case: {test_name}. Use 'simple' or 'dropdown'.")

    driver.quit()
