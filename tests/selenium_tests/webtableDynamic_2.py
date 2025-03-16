from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Initialize WebDriver (Make sure to set your driver path)
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(1)
driver.get("https://testautomationpractice.blogspot.com/")

# Locate table
table = driver.find_element(By.ID, "taskTable")
actions = ActionChains(driver)
actions.move_to_element(table).perform()

# Get headers to find dynamic column positions
headers = table.find_elements(By.XPATH, ".//thead/tr/th")
header_texts = [header.text for header in headers]

# Identify column positions
cpu_index = header_texts.index("CPU (%)")
network_index = header_texts.index("Network (Mbps)")
disk_index = header_texts.index("Disk (MB/s)")
memory_index = header_texts.index("Memory (MB)")

# Get all rows
rows = table.find_elements(By.XPATH, ".//tbody/tr")

# Dictionary to store extracted data
data = {}

# Iterate through rows
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    name = cells[0].text  # First column is always Name

    # Store values based on the identified indexes
    data[name] = {
        "CPU (%)": cells[cpu_index].text,
        "Network (Mbps)": cells[network_index].text,
        "Disk (MB/s)": cells[disk_index].text,
        "Memory (MB)": cells[memory_index].text,
    }

# Print data in required format
print(f"CPU load of Chrome process: {data['Chrome']['CPU (%)']}\n")
print(f"Memory Size of Firefox process: {data['Firefox']['Memory (MB)']}\n")
print(f"Network speed of Chrome process: {data['Chrome']['Network (Mbps)']}\n")
print(f"Disk space of Firefox process: {data['Firefox']['Disk (MB/s)']}\n")

# Close driver
driver.quit()
