from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def initialize_driver():
    """Initialize and return a Selenium WebDriver instance."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(1)
    driver.get("https://testautomationpractice.blogspot.com/")
    return driver


def get_column_indices(driver):
    """Retrieve column indices from the table header."""
    header_row = driver.find_element(By.ID, "headers")
    ActionChains(driver).move_to_element(header_row).perform()

    headers = header_row.find_elements(By.TAG_NAME, "th")
    column_names = [header.text.strip() for header in headers]

    return {
        "cpu": column_names.index("CPU (%)"),
        "network": column_names.index("Network (Mbps)"),
        "disk": column_names.index("Disk (MB/s)"),
        "memory": column_names.index("Memory (MB)"),
    }


def extract_and_analyze_data(driver, column_indices):
    """Extract table data and analyze system usage."""
    rows = driver.find_elements(By.XPATH, "//tbody[@id='rows']/tr")

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        name = cells[0].text.strip()  # Name column is always first

        # Extract values
        cpu_value = cells[column_indices["cpu"]].text.strip()
        network_value = cells[column_indices["network"]].text.strip()
        disk_value = cells[column_indices["disk"]].text.strip()
        memory_value = cells[column_indices["memory"]].text.strip()

        # Perform analysis
        analyze_usage(name, cpu_value, network_value, disk_value, memory_value)


def analyze_usage(name, cpu, network, disk, memory):
    """Analyze usage values and print warnings if thresholds are exceeded."""
    if "%" in cpu and float(cpu.replace("%", "")) > 2:
        print(f"{name} has high CPU usage: {cpu}")

    if "MB/s" in disk and float(disk.replace("MB/s", "")) < 1:
        print(f"{name} has low Disk usage: {disk}")

    if "MB" in memory and float(memory.replace("MB", "")) > 40:
        print(f"{name} has high Memory usage: {memory}")

    if "Mbps" in network and float(network.replace("Mbps", "")) > 1:
        print(f"{name} has high Network usage: {network}")


def main():
    driver = initialize_driver()
    try:
        column_indices = get_column_indices(driver)
        extract_and_analyze_data(driver, column_indices)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
