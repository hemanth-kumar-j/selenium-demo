from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# Locate table rows and columns
rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
columns = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th")

num_rows = len(rows)
num_columns = len(columns)

print(f"Number of Rows: {num_rows}")
print(f"Number of Columns: {num_columns}\n")

# Print all table values
print("Table Data:")
for row in range(2, num_rows + 1):  # Skipping header row
    row_values = [
        driver.find_element(
            By.XPATH, f"//table[@name='BookTable']/tbody/tr[{row}]/td[{col}]"
        ).text
        for col in range(1, num_columns + 1)
    ]
    print(" | ".join(row_values))

print("\nBooks by Author: Amit")
for row in range(2, num_rows + 1):
    author = driver.find_element(
        By.XPATH, f"//table[@name='BookTable']/tbody/tr[{row}]/td[2]"
    ).text
    if author == "Amit":
        book_name = driver.find_element(
            By.XPATH, f"//table[@name='BookTable']/tbody/tr[{row}]/td[1]"
        ).text
        price = driver.find_element(
            By.XPATH, f"//table[@name='BookTable']/tbody/tr[{row}]/td[4]"
        ).text
        print(f"Book Name: {book_name} | Author: {author} | Price: {price}")

# Close the WebDriver
driver.quit()
