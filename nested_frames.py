from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/nested_frames")


def switch_to_frame(frame_name):
    """Switch to a given frame by name."""
    driver.switch_to.frame(frame_name)


def get_frame_content(locator):
    """Retrieve text content from a frame."""
    return driver.find_element(
        By.ID if locator == "content" else By.TAG_NAME, value=locator
    ).text


# Navigate through frames and extract content
switch_to_frame("frame-top")
switch_to_frame("frame-middle")
print("Content in middle frame:", get_frame_content("content"))

# Return to main document and switch to bottom frame
driver.switch_to.default_content()
switch_to_frame("frame-bottom")
print("Content in bottom frame:", get_frame_content("body"))

# Close browser
driver.quit()
