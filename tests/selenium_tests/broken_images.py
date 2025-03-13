import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/broken_images")


def find_broken_images():
    """Finds and returns a list of broken images on the webpage."""
    broken_images = []
    for image in browser.find_elements(By.TAG_NAME, "img"):
        src = image.get_attribute("src")
        if src and requests.get(src).status_code != 200:
            broken_images.append(src)

    return broken_images


# Get broken images
broken_images = find_broken_images()

# Print results
if broken_images:
    print(f"Found {len(broken_images)} broken images:")
    for img in broken_images:
        print(f"- {img}")
else:
    print("No broken images found.")

# Close the browser
browser.quit()
