import time
from selenium import webdriver

# List of viewport sizes (width, height)
VIEWPORTS = [(1024, 768), (768, 1024), (375, 667), (414, 896)]


def test_viewports(url):
    """Opens a webpage and resizes the browser to multiple viewports."""
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        for width, height in VIEWPORTS:
            print(f"Testing viewport: {width}x{height}")
            driver.set_window_size(width, height)
            time.sleep(2)  # Pause for observation
    finally:
        driver.quit()


# Run the test
test_viewports("https://www.google.com/")
