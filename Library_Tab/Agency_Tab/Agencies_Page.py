from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import time
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login import driver
from Library_Tab.Library_icon import my_class
from Agency_modal import Agencies
from Assert_agencies import agencytable
import unittest
# Call the Login.py
my_class()

try:
    # Wait for the element containing the text to be visible
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "agencies-tab")))

    # Get the text content of the element
    actual_text = element.text.strip()

    # Define the expected text
    expected_text = "Agencies"

    # Assert that the expected text is present in the actual text
    assert expected_text in actual_text, f"Expected text '{expected_text}' not found in actual text '{actual_text}'"
    print("Text assertion passed: Agencies")

except Exception as e:
    # Handle any exceptions or assertion failures
    print(f"Text assertion failed: {e}")
# Pause the script and wait for user input before closing the browser window

# Click agencies tab
icon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "agencies-tab")))
icon.click()

assert_agencies = agencytable()
assert_agencies.agencies_column_names()

agencies_instance = Agencies()
agencies_instance.execute()

input("Please enter...")






