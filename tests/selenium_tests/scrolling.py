from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_moved_pixels(driver):
    """Prints the number of pixels scrolled."""
    sleep(1)
    pixels_moved = driver.execute_script("return window.pageYOffset;")
    print("Scrolled pixels:", pixels_moved)


def scroll_operations():
    """Performs different scrolling operations on the webpage."""
    with webdriver.Chrome() as driver:
        driver.maximize_window()
        driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

        # Scroll down by 1000 pixels
        driver.execute_script("window.scrollBy(0, 1000);")
        get_moved_pixels(driver)

        # Scroll to the Flag of India
        flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
        driver.execute_script("arguments[0].scrollIntoView();", flag)
        get_moved_pixels(driver)

        # Scroll to the bottom of the page
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        get_moved_pixels(driver)

        # Scroll back to the top
        driver.execute_script("window.scrollBy(0, -document.body.scrollHeight);")
        get_moved_pixels(driver)


if __name__ == "__main__":
    scroll_operations()
