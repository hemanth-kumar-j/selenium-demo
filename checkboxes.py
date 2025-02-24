import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

# Initialize WebDriver
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Wait for page load
time.sleep(2)

# Scroll to bottom of the page
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Select all checkboxes
checkboxes = browser.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

# Count selected checkboxes
checked_count = sum(1 for checkbox in checkboxes if checkbox.is_selected())

# Verify checkbox count
expected_checked_count = 7
if checked_count == expected_checked_count:
    print("Checkbox count verified")
else:
    print(
        f"Checkbox count mismatch: {checked_count} checked (Expected: {expected_checked_count})"
    )

# Close browser
time.sleep(2)
browser.quit()
