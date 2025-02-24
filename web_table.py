from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
browser = webdriver.Chrome()
browser.maximize_window()

# Open the webpage
browser.get("https://cosmocode.io/automation-practice-webtable/")
browser.execute_script("window.scrollTo(0, 700)")

# Locate the web table
table = browser.find_element(By.ID, "countries")
rows = table.find_elements(By.TAG_NAME, "tr")

# Get row count
print(f"Total Rows: {len(rows)}")

# Search for the target value in the table
target_value = "India"
found = False

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")

    if any(target_value in cell.text for cell in cells):
        print(f"Found target value: '{target_value}'")
        found = True
        break

if not found:
    print(f"Target value '{target_value}' not found")

# Close the browser
browser.quit()

