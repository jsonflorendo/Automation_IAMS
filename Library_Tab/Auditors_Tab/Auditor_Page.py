from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import time
from Auditor_modal import Auditors
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login import driver
from Assert_auditors_table import auditortable
from Library_Tab.Library_icon import my_class

# Call the Login.py
my_class()

try:
    # Wait for the element containing the text to be visible
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@id='pool-auditors-tab']")))

    # Get the text content of the element
    actual_text = element.text.strip()

    # Define the expected text
    expected_text = "Auditors"

    # Assert that the expected text is present in the actual text
    assert expected_text in actual_text, f"Expected text '{expected_text}' not found in actual text '{actual_text}'"
    print("Text assertion passed: Auditors")

except Exception as e:
    # Handle any exceptions or assertion failures
    print(f"Text assertion failed: {e}")
# Pause the script and wait for user input before closing the browser window

# Find the icon element
icon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@id='pool-auditors-tab']")))
icon.click()

assert_auditor = auditortable()
assert_auditor.auditor_column_names()

auditors_instance = Auditors()
auditors_instance.execute()

input("Press enter to continue")






