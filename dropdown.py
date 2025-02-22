import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.maximize_window()
login_url = "https://the-internet.herokuapp.com/dropdown"
browser.get(login_url)

dropdown_element = browser.find_element(By.ID, value="dropdown")
select = Select(dropdown_element)
option_count = len(select.options)
target_value = "Option 2"

# Select the value by Visible text
time.sleep(2)
select.select_by_visible_text("Option 1")

# Select the value by Index
time.sleep(2)
select.select_by_index(2)

# Select the value by a Value
time.sleep(2)
select.select_by_value("1")


expected_count = 3

if option_count == expected_count:
    print("Count is correct")
else:
    print("Count is incorrect")
time.sleep(2)


for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is {target_value}")
        break
    else:
        print(f"Option {target_value} not found")
time.sleep(2)

browser.quit()
