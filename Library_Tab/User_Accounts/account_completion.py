from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from Login import driver
class usercomplete:
    def __init__(self):
        pass

    def usercompletion(self):
        # Your function code here
        pass

    def execute(self):
        # Call the add_agency method
        self.usercompletion()
        try:
            # Wait for the element containing the text to be visible
            message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[@id='swal2-title']")))

            # Get the text content of the element
            actual_text = message.text.strip()

            # Define the expected text
            expected_text = "User Account added successfully."

            # Assert that the expected text is present in the actual text
            assert expected_text in actual_text, f"Expected text '{expected_text}' not found in actual text '{actual_text}'"
            print("Text assertion passed: User Account added successfully.")

        except Exception as e:
            # Handle any exceptions or assertion failures
            print ( f"An error occurred: {e}" )

            ok_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "swal2-actions")))
            ok_button.click()

if"__main__" == __name__:
    message_instance = usercomplete()
    message_instance.execute()