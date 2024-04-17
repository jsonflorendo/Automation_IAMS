from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import time
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login import driver
from Library_Tab. Library_icon import my_class
from References_icon import my_reference
from Assert_references import  referencetable
# Call the Login.py
my_reference()

try:
    # Wait for the element containing the text to be visible
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='References']")))

    # Get the text content of the element
    actual_text = element.text.strip()

    # Define the expected text
    expected_text = "References"

    # Assert that the expected text is present in the actual text
    assert expected_text in actual_text, f"Expected text '{expected_text}' not found in actual text '{actual_text}'"
    print("Text assertion passed: References")

except Exception as e:
    # Handle any exceptions or assertion failures
    print(f"Text assertion failed: {e}")

# # Find the icon element
# icon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='References']")))
# # Click on the icon
# icon.click()

assert_reference = referencetable()
assert_reference.reference_column_names ()

input("Please enter...")






