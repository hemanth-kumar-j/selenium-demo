from selenium import webdriver

# Initialize the browser
driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")


# Utility function to print cookies
def print_cookies():
    cookies = driver.get_cookies()
    print(f"\nNumber of cookies: {len(cookies)}")
    for cookie in cookies:
        print(f"\n{cookie}")


# --- Step 1: Print all cookies from the browser ---
print("All Cookies From Browser:")
print_cookies()

# --- Step 2: Delete a specific cookie ---
cookie_name = ".Nop.Culture"
if driver.get_cookie(cookie_name):
    driver.delete_cookie(cookie_name)

    try:
        assert driver.get_cookie(cookie_name) is None
        print(f"\nCookie '{cookie_name}' successfully deleted.")
    except AssertionError:
        print(f"\nAssertion failed: '{cookie_name}' cookie still exists!")

else:
    print(f"\nCookie '{cookie_name}' not found — nothing to delete.")

print_cookies()

# --- Step 3: Delete all cookies ---
driver.delete_all_cookies()

try:
    cookies = driver.get_cookies()
    assert cookies == [], "Cookies are not deleted"
    print("\nAll cookies successfully deleted.")
except AssertionError as e:
    print(f"\nAssertion failed: {e}")

print("\nAfter deleting all cookies:")
print_cookies()

# --- Step 4: Add a new cookie ---
new_cookie = {"name": "TestCookie", "value": "TestValue"}
driver.add_cookie(new_cookie)

print("\nAfter adding a new cookie:")
print_cookies()

# --- Step 5: Close the browser ---
driver.quit()
