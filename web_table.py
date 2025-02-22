from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://cosmocode.io/automation-practice-webtable/")
browser.execute_script("window.scrollTo(0,700)")
table = browser.find_element(By.ID, value="countries")
rows = browser.find_elements(By.TAG_NAME, value="tr")
row_count = len(rows)
print(row_count)
target_value = "India"
found = False
for row in rows:
    cells = row.find_elements(By.TAG_NAME, value="td")
    for cell in cells:
        if target_value in cell.text:
            print(f"Found target value '{target_value}'")
            found = True
            break
    if found:
        break
if not found:
    print(f"Target value '{target_value}' not found")
browser.quit()
