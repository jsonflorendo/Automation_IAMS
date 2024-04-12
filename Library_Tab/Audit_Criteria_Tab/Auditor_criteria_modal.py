from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from input import *
from Library_Tab.Auditors_Tab.Auditor_completion import Auditorscomplete
from Login import driver
from modal_assert_citeria import ModalTest
from error_message_crieteria import error_message
class Auditors:
    def __init__(self):
        # Initialize any instance-specific attributes here, if needed
        pass

    def add_auditors(self):
        # Your function code here
        pass

    def input_field_text(self, locator_strategy, locator_value, text):
        input_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((locator_strategy, locator_value)))
        input_field.clear()  # Clear the field in case there is existing text
        input_field.send_keys(text)

    def execute(self):
        # Call the add_agency method
        self.add_auditors()

        # Find the icon element and click on it
        icon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-bs-target='#AuditCriteriaModal']")))
        icon.click()

        assert_text = ModalTest ()
        assert_text.execute ()

        criteria_error = error_message ()
        criteria_error.execute ()

        # Locate the radio button for Internal
        radio_button =WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cra_active")))
        radio_button.click()

        # # Locate the radio button for External
        # radio_button = driver.find_element (By.ID, "aur_external_1")
        # radio_button.click ()

        # # Locate the toggle button element by its ID, name, or other locator
        # toggle_button = driver.find_element (By.ID, "aur_active")
        # toggle_button.click ()

        # Input text into the input fields
        self.input_field_text(By.ID, "cra_name", name)

        audit_area = Select(driver.find_element (By.ID, "cra_areas"))
        indices_to_select = [1, 4, 6]  # Example indices of options to select
        for index in indices_to_select:
            audit_area.select_by_index(index)

        self.input_field_text ( By.ID, "cra_url", reference_link )

        # Locate the date input field by its ID or other locator
        date_input = driver.find_element(By.ID, "aur_birthdate")

        # Click on the date input field to open the date picker
        date_input.clear()

        # Now, you need to locate and click on the specific date in the date picker.
        # This may vary depending on how the date picker is implemented.
        # Here's an example of selecting a date by clicking on a specific day element:

        # Locate and click on the day element corresponding to the desired date
        desired_date = "03-15-1986"  # Example date in YYYY-MM-DD format
        date_input.send_keys(desired_date)

        self.input_field_text(By.ID, "aur_contact_no", "88378113 Local 310")

        dropdown = Select(driver.find_element (By.ID, "aur_status"))
        dropdown.select_by_index(4)

        save_button = WebDriverWait ( driver, 10 ).until (
            EC.visibility_of_element_located ( (By.ID, "addAuditor") ) )
        save_button.click ()

        message_instance = Auditorscomplete ()
        message_instance.completion ()
        message_instance.execute ()

# Instantiate the Auditors class and execute its methods
if"__main__" == __name__:
    auditors_instance = Auditors()
    auditors_instance.execute()



