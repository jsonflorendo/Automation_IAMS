from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import time
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login import driver
from Library_Tab. Library_icon import my_class
from account_modal import user
from Assert_account import accounttable


# Call the Login.py
my_class()

try:
    # Wait for the element containing the text to be visible
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-accounts-tab")))

    # Get the text content of the element
    actual_text = element.text.strip()

    # Define the expected text
    expected_text = "User Accounts"

    # Assert that the expected text is present in the actual text
    assert expected_text in actual_text, f"Expected text '{expected_text}' not found in actual text '{actual_text}'"
    print("Text assertion passed: User Accounts")

except Exception as e:
    # Handle any exceptions or assertion failures
    print(f"Text assertion failed: {e}")
# Pause the script and wait for user input before closing the browser window

# Find the icon element
icon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-accounts-tab")))
icon.click()

assert_account = accounttable()
assert_account.account_column_names()

account_instance = user()
account_instance.add_user()
account_instance.execute()

input("Please enter...")






