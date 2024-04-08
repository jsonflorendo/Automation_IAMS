from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import time
from Auditor_criteria_modal import Auditors
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login import driver
0.
from Library_Tab.Library_icon import my_class
from Assert_criteria_table import criteriatable
# Call the Login.py
my_class()

try:
    # Wait for the element containing the text to be visible
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@id='audit-criteria-tab']")))

    # Get the text content of the element
    actual_text = element.text.strip()

    # Define the expected text
    expected_text = "Audit Criteria"

    # Assert that the expected text is present in the actual text
    assert expected_text in actual_text, f"Expected text '{expected_text}' not found in actual text '{actual_text}'"
    print("Text assertion passed: Audit Criteria")

except Exception as e:
    # Handle any exceptions or assertion failures
    print(f"Text assertion failed: {e}")
# Pause the script and wait for user input before closing the browser window

# Find the icon element
icon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@id='audit-criteria-tab']")))

# Click on the icon
icon.click()

assert_criteria = criteriatable()
assert_criteria.criteria_column_names()

auditors_instance = Auditors()
auditors_instance.execute()








