import os
import time
import glob
from selenium import webdriver
from selenium.webdriver.common.by import By

# Define download directory
DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def get_browser_driver(browser="chrome"):
    """Initialize and return a web driver with custom download settings."""
    preferences = {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
    }

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", preferences)
        return webdriver.Chrome(options=options)

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", DOWNLOAD_DIR)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference(
            "browser.helperApps.neverAsk.saveToDisk",
            "application/msword, application/pdf, application/octet-stream",
        )
        return webdriver.Firefox(options=options)

    if browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option("prefs", preferences)
        return webdriver.Edge(options=options)

    raise ValueError("Unsupported browser!")


def get_latest_downloaded_file():
    """Retrieve the most recent downloaded file matching the pattern."""
    files = glob.glob(os.path.join(DOWNLOAD_DIR, "SampleDOCFile_100kb*.doc"))
    return max(files, key=os.path.getctime) if files else None


def wait_for_download(timeout=10, check_interval=2):
    """Wait for the file download to complete within the given timeout."""
    start_time = time.time()
    previous_size = -1

    while time.time() - start_time < timeout:
        latest_file = get_latest_downloaded_file()

        if latest_file and os.path.exists(latest_file):
            current_size = os.path.getsize(latest_file)
            if current_size == previous_size:
                print(f"Download completed: {os.path.basename(latest_file)}")
                return latest_file
            previous_size = current_size

        time.sleep(check_interval)

    print("Download timed out!")
    return None


def main():
    """Main function to initiate browser, download file, and verify download."""
    driver = get_browser_driver("chrome")
    driver.maximize_window()
    driver.get("https://www.sample-videos.com/download-sample-doc-file.php")
    driver.find_element(By.XPATH, "//td/a[@download='SampleDOCFile_100kb.doc']").click()

    latest_file = wait_for_download()
    assert latest_file and os.path.exists(
        latest_file
    ), "File not downloaded successfully"

    driver.quit()


if __name__ == "__main__":
    main()
