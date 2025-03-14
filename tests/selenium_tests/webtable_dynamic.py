from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def login(driver, wait, username, password):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(
        username
    )
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()


def navigate_to_admin_section(wait):
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Admin']"))
    ).click()
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='oxd-table-card']/div[@role='row']")
        )
    )


def extract_user_data(driver):
    rows = driver.find_elements(
        By.XPATH, "//div[@class='oxd-table-card']/div[@role='row']"
    )
    user_data = []
    enabled_count = 0

    for row in rows:
        cells = row.find_elements(By.CLASS_NAME, "oxd-table-cell")
        row_info = [cells[i].text for i in range(1, 5)]
        user_data.append(row_info)

        if row_info[-1] == "Enabled":
            enabled_count += 1

    return user_data, len(rows), enabled_count


def main():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)

    try:
        login(driver, wait, "Admin", "admin123")
        navigate_to_admin_section(wait)
        user_data, total_users, enabled_users = extract_user_data(driver)

        for row in user_data:
            print(row)

        print("Total Users:", total_users)
        print("Enabled Users:", enabled_users)
        print("Disabled Users:", total_users - enabled_users)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
