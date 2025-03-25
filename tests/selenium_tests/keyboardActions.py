from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def main():
    # Initialize the Chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://text-compare.com/")

    try:
        # Get the text area elements
        text_area_1 = driver.find_element(By.ID, "inputText1")
        text_area_2 = driver.find_element(By.ID, "inputText2")

        # Enter text into the first text area
        text_to_copy = "Hello"
        text_area_1.send_keys(text_to_copy)

        # Create an ActionChains object
        action = ActionChains(driver)

        # Select, copy, and paste text using keyboard shortcuts
        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        action.send_keys(Keys.TAB).perform()

        # Assert that the cursor is in the second text area
        assert (
            driver.switch_to.active_element == text_area_2
        ), "Cursor is not in the second text area"
        print("Cursor is in the second text area")

        action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        print("Text pasted in the second text area")

        sleep(1)  # Wait for a second to observe the result

    finally:
        driver.quit()
        print("Browser closed")


if __name__ == "__main__":
    main()
