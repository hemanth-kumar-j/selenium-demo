from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def drag_and_drop(driver, source, target):
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()
    sleep(1)
    bg_color = source.value_of_css_property("background-color")
    assert "0, 255, 0" in bg_color, f"Expected green, got {bg_color}"
    country_name = target.text.split("\n")[0].strip()  # Extract only the country name
    print(f"Moved: {source.text.strip()} -> {country_name}")


def exucute_first_drag_and_drop(driver):
    # Drag and Drop with Explicit Element Assignments
    print("Drag and Drop with Explicit Element Assignments")
    capitals_ids = ["box1", "box2", "box3", "box4", "box5", "box6", "box7"]
    countries_ids = [
        "box101",
        "box102",
        "box103",
        "box104",
        "box105",
        "box106",
        "box107",
    ]

    capitals = [driver.find_element(By.ID, cid) for cid in capitals_ids]
    countries = [driver.find_element(By.ID, cid) for cid in countries_ids]

    for capital, country in zip(capitals, countries):
        drag_and_drop(driver, capital, country)


def exucute_second_drag_and_drop(driver):
    # Performing drag and drop operation with fresh elements
    print("Performing drag and drop operation with fresh elements")

    for i in range(1, 8):
        capital = driver.find_element(By.ID, f"box{i}")
        country = driver.find_element(By.ID, f"box10{i}")
        drag_and_drop(driver, capital, country)


def dynamic_drag_and_drop(driver):
    # Drag and Drop with Dynamic Mapping
    print("Drag and Drop with Dynamic Mapping")

    capital_country_map = {
        "Oslo": "Norway",
        "Stockholm": "Sweden",
        "Washington": "United States",
        "Copenhagen": "Denmark",
        "Seoul": "South Korea",
        "Rome": "Italy",
        "Madrid": "Spain",
    }

    capitals = [
        el
        for el in driver.find_elements(By.CSS_SELECTOR, "#dropContent .dragableBox")
        if el.is_displayed()
    ]
    countries = driver.find_elements(By.CSS_SELECTOR, "#countries .dragableBoxRight")
    country_elements = {country.text.strip(): country for country in countries}

    for capital in capitals:
        capital_text = capital.text.strip()
        if capital_text in capital_country_map:
            country_name = capital_country_map[capital_text]
            if country_name in country_elements:
                drag_and_drop(driver, capital, country_elements[country_name])
            else:
                print(
                    f"Country '{country_name}' not found for capital '{capital_text}'"
                )
        else:
            print(f"No mapping found for capital: {capital_text}")


def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
    )

    # Method 1
    exucute_first_drag_and_drop(driver)

    # Refresh and Perform Again with method 2
    driver.refresh()
    exucute_second_drag_and_drop(driver)

    # Refresh and Perform Again with method 3
    driver.refresh()
    dynamic_drag_and_drop(driver)

    print("Test Passed")
    sleep(1)
    driver.quit()


if __name__ == "__main__":
    main()
