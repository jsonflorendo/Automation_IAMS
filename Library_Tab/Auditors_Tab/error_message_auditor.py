from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login import driver
import unittest

class ErrorMessageChecker:
    def __init__(self):
        pass

    def execute(self):
        try:
            # Click the save button
            save_button = WebDriverWait ( driver, 10 ).until (
                EC.visibility_of_element_located ( (By.ID, "addAuditor") ) )
            save_button.click ()

            # Define a dictionary to store field box IDs and associated error message IDs
            field_error_mapping = {
                "aur_name_last": "error-aur_name_last",
                "aur_name_first": "error-aur_name_first",
                "aur_position": "error-aur_position",
                "aur_salary_grade": "error-aur_salary_grade",
                "aur_email": "error-aur_email",
                "aur_contact_no": "error-aur_contact_no",
                # Add more field IDs and associated error message IDs as needed
            }

            # Iterate through each field box and check for error message
            for field_id, error_id in field_error_mapping.items ():
                # Find the field box
                field_box = driver.find_element ( By.ID, field_id )

                # Clear the field box
                field_box.clear ()

                # Submit an empty value
                field_box.send_keys ( Keys.TAB )

                # Wait for the error message to appear
                error_message = WebDriverWait ( driver, 10 ).until (
                    EC.visibility_of_element_located ( (By.ID, error_id) ) )

                # Assert the error message is displayed
                assert error_message.is_displayed (), f"Error message for {field_id} is not displayed"

                print ( f"Error message for {field_id} is displayed: {error_message.text}" )

                # Check if there are any additional error messages indicating "email already exists"
            additional_error_messages = driver.find_elements ( By.XPATH, "//div[@class='additional-error']" )
            for message in additional_error_messages:
                if "email already exists" in message.text.lower ():
                    print ( "Email already exists error message is displayed" )
                    break  # Exit loop if found

        except Exception as e:
            print ( f"An error occurred: {e}" )

if __name__ == "__main__":
    error_checker = ErrorMessageChecker()
    error_checker.execute()