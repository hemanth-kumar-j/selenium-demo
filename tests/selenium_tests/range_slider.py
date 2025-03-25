from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the webpage
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

# Locate slider elements
min_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[1]")
max_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[2]")

# Print initial slider positions
print("Slider positions before moving:")
print(f"Min slider: {min_slider.location}")
print(f"Max slider: {max_slider.location}")

# Move sliders using ActionChains
actions = ActionChains(driver)
actions.drag_and_drop_by_offset(min_slider, 100, 0).perform()
actions.drag_and_drop_by_offset(max_slider, -100, 0).perform()
sleep(1)

# Print updated slider positions
print("Slider positions after moving:")
print(f"Min slider: {min_slider.location}")
print(f"Max slider: {max_slider.location}")

# Close the browser
driver.quit()
