import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
time.sleep(2)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
checkboxes = browser.find_elements(By.XPATH, value="//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

checked_count = 0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count += 1

expected_checked_count = 7

if checked_count == expected_checked_count:
    print("Checkbox count verified")
else:
    print("Checkbox count mismatch")
    print(f"Checked checkbox: {checked_count}")
time.sleep(2)

browser.quit()
