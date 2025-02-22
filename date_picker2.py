import time
from selenium import webdriver
from selenium.webdriver import Keys
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/datepicker/")
wait = WebDriverWait(driver, 10)


def get_date():
    date_picker = driver.find_element(By.ID, value="datepicker")
    selected_date = date_picker.get_attribute("value")
    return selected_date


def click_datepicker_after_closing_attention(index):
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, f"(//a[@class='close_img'])[{index}]")
        )
    ).click()
    dropdown_date_frame = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, f"(//iframe[@class='demo-frame lazyloaded'])[{index}]")
        )
    )
    driver.switch_to.frame(dropdown_date_frame)
    time.sleep(2)
    driver.find_element(By.ID, value="datepicker").click()
    current_date = datetime.now()
    next_date = current_date + timedelta(days=1)
    return current_date, next_date


current_date, next_date = click_datepicker_after_closing_attention(1)
formatted_date = next_date.strftime("%m/%d/%Y")
driver.find_element(By.ID, value="datepicker").send_keys(formatted_date + Keys.TAB)
time.sleep(2)
selected_date = get_date()
print(f"Simple Date Picker: {selected_date}")
driver.switch_to.default_content()


driver.find_element(By.XPATH, value="//li[@id='DropDown DatePicker']").click()
current_date, next_date = click_datepicker_after_closing_attention(2)
time.sleep(2)
# print(current_date)
# print(next_date)
next_day = str(next_date.day)
# print(next_day)
current_month = datetime.now().month
current_year = current_date.year
next_month = current_month % 12
# next_month_year = f"{next_month}/{current_year}"
month_dropdown = driver.find_element(By.CSS_SELECTOR, value=".ui-datepicker-month")
select = Select(month_dropdown)
select.select_by_value(str(next_month))
year_dropdown = driver.find_element(By.CSS_SELECTOR, value=".ui-datepicker-year")
select = Select(year_dropdown)
select.select_by_value(str(current_year))
driver.find_element(By.LINK_TEXT, next_day).click()
time.sleep(2)
selected_date = get_date()
print(f"Dropdown Date Picker: {selected_date}")
driver.switch_to.default_content()

driver.quit()
