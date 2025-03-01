import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Initialize WebDriver
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/dropdown")

# Locate dropdown element
dropdown_element = browser.find_element(By.ID, "dropdown")
select = Select(dropdown_element)


# Function to select dropdown options
def select_option(method, value):
    """Select dropdown option based on method: text, index, or value."""
    time.sleep(1)  # Small delay for UI stability
    if method == "text":
        select.select_by_visible_text(value)
    elif method == "index":
        select.select_by_index(value)
    elif method == "value":
        select.select_by_value(value)
    selected_text = select.first_selected_option.text
    print(f"Selected: {selected_text}")


# Selecting dropdown options
select_option("text", "Option 1")
select_option("index", 2)
select_option("value", "1")

# Verify dropdown option count
expected_count = 3
option_count = len(select.options)

print("Count is correct" if option_count == expected_count else "Count is incorrect")
time.sleep(2)

# Select target option if available
target_value = "Option 2"
for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option: {target_value}")
        break
    else:
        print(f"Option '{target_value}' not found")

# Close browser
time.sleep(1)
browser.quit()
