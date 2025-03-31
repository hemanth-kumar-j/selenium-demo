import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_file_path(filename: str, folder: str = "downloads") -> str:
    """Returns the absolute file path in the specified folder."""
    return os.path.join(os.getcwd(), folder, filename)


def validate_file_exists(file_path: str):
    """Checks if the specified file exists."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")


def upload_file(driver, file_path: str):
    """Uploads the specified file using Selenium WebDriver."""
    driver.get("https://demoqa.com/upload-download")
    upload = driver.find_element(By.ID, "uploadFile")
    upload.send_keys(file_path)

    # Wait for upload confirmation
    wait = WebDriverWait(driver, 5)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "uploadedFilePath"), os.path.basename(file_path)
        )
    )

    uploaded_file = driver.find_element(By.ID, "uploadedFilePath")
    assert os.path.basename(file_path) in uploaded_file.text, "File upload failed"
    print("File uploaded successfully")


def main():
    """Main function to execute file upload test."""
    filename = "file-sample_150kB.pdf"
    file_path = get_file_path(filename)
    validate_file_exists(file_path)

    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        upload_file(driver, file_path)
        sleep(2)  # Pause to observe the result
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
