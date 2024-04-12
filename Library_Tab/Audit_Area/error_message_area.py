from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login import driver
import unittest

class error_message:
    def __init__(self):
        pass

    def error_assert(self):
        # Your function code here
        pass

    def execute(self):
        # Call the add_agency method
        self.error_assert()
        try:
            save_button = WebDriverWait ( driver, 10 ).until (
                EC.visibility_of_element_located ( (By.XPATH, "//button[@id='addAuditArea']") ) )
            save_button.click ()

            # Define a dictionary to store field box IDs and associated error message IDs
            field_error_mapping = {
                "ara_name": "error-ara_name",
                # Add more field IDs and associated error message IDs as needed
            }

            # Iterate through each field box and check for error message
            for field_id, error_id in field_error_mapping.items ():
                # Find the field box
                field_box = driver.find_element ( By.ID, field_id )

                # Clear the field box and submit an empty value
                field_box.clear ()
                field_box.send_keys ( Keys.TAB )  # Submitting the field to trigger error message

                # Wait for the error message to appear
                error_message = WebDriverWait ( driver, 10 ).until (
                    EC.visibility_of_element_located ( (By.ID, error_id) )
                )

                # Assert the error message is displayed
                assert error_message.is_displayed (), f"Error message for {field_id} is not displayed"

                print(f"Error message for {field_id} is displayed: {error_message.text}")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    area_error = error_message()
    area_error.execute()