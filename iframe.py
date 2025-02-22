import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://seleniumbase.io/demo_page/")

iframe = driver.find_element(By.ID, value="myFrame2")
driver.switch_to.frame(iframe)
iframe_text = driver.find_element(By.XPATH, value="/html/body/h4")
text = iframe_text.text
print(f"{text}")
driver.switch_to.default_content()

text_editor = driver.find_element(By.ID, value="myTextInput2")
text_editor.clear()
text_editor.send_keys("Pre-Filled Text Field")
time.sleep(1)
# checkbox = driver.find_element(By.ID, value='checkBox1')
# checkbox.click()
# time.sleep(1)
# assert checkbox.is_selected() == True
# if checkbox.is_selected():
#    print("Checkbox is checked")
driver.quit()
