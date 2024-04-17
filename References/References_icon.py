from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import time
# from Auditor_input import Agency
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login import my_function
from Login import driver
# # Launch the browser
# driver = webdriver.Chrome()
def my_reference():
    # Your function code here
    pass
# Execute your function if the script is run directly
if __name__ == "__main__":
    my_reference()

# Call the Login.py
my_function()

# add_agency()

# Find the icon element
icon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//i[@class='fas fa-fw fad fa-swatchbook fa-2x']")))

# Click on the icon
icon.click()

# Introduce a delay
time.sleep(2)

try:
    # Wait for the element containing the text to be visible
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@id='references']")))

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
# Pause the script and wait for user input before closing the browser window

# Find the icon element
icon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@id='references']")))

# Click on the icon
icon.click()






