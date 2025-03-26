import os
import time
import glob
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set download directory
DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def setup_driver(browser="chrome"):
    """Setup WebDriver with custom download settings."""
    preferences = {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,
    }

    if browser == "chrome":
        options = webdriver.ChromeOptions()
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", DOWNLOAD_DIR)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference(
            "browser.helperApps.neverAsk.saveToDisk",
            "application/pdf,application/msword,application/octet-stream",
        )
        options.set_preference("pdfjs.disabled", True)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
    else:
        raise ValueError("Unsupported browser!")

    (
        options.add_experimental_option("prefs", preferences)
        if browser in ["chrome", "edge"]
        else None
    )
    return (
        webdriver.Chrome(options=options)
        if browser == "chrome"
        else (
            webdriver.Firefox(options=options)
            if browser == "firefox"
            else webdriver.Edge(options=options)
        )
    )


def get_latest_file():
    """Retrieve the latest downloaded PDF file."""
    files = glob.glob(os.path.join(DOWNLOAD_DIR, "SamplePDFFile_5mb*.pdf"))
    return max(files, key=os.path.getctime) if files else None


def wait_for_download(timeout=10):
    """Wait for the file to be fully downloaded."""
    start_time = time.time()
    previous_size = -1

    while time.time() - start_time < timeout:
        latest_file = get_latest_file()
        if latest_file and os.path.exists(latest_file):
            current_size = os.path.getsize(latest_file)
            if current_size == previous_size:
                print(f"Download completed: {os.path.basename(latest_file)}")
                return latest_file
            previous_size = current_size
        time.sleep(2)

    print("Download timed out!")
    return None


# Main execution
driver = setup_driver("chrome")
driver.maximize_window()
driver.get("https://www.sample-videos.com/download-sample-pdf.php")
driver.find_element(By.XPATH, "//td/a[@download='SamplePDFFile_5mb.pdf']").click()

# Validate download
latest_file = wait_for_download()
assert latest_file, "File download failed!"
driver.quit()
