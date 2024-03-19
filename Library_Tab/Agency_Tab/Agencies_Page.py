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

# Assert table column
table = driver.find_element_by_xpath("//table[@id='your_table_id']")

# Find the header row
header_row = table.find_element_by_tag_name("tr")

# Extract text from each header cell
header_cells = header_row.find_elements_by_tag_name("th")
column_titles = [cell.text for cell in header_cells]

# Perform assertions
expected_titles = ["Title1", "Title2", "Title3"]  # Your expected column titles
for actual_title, expected_title in zip(column_titles, expected_titles):
    assert actual_title == expected_title, f"Expected {expected_title}, but got {actual_title}"

agencies_instance = Agencies()
agencies_instance.add_agencies()
agencies_instance.execute()

input("Please enter...")






