from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from input import *
from Library_Tab.Auditors_Tab.Auditor_completion import Auditorscomplete
from Login import driver
from  modal_assert_auditors import ModalTest
from error_message_auditor import ErrorMessageChecker
from existing_error_message_auditor import ExistingerrorMessage
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
        icon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-bs-target='#AuditorModal']")))
        icon.click()

        assert_text = ModalTest ()
        assert_text.execute ()

        error_checker = ErrorMessageChecker ()
        error_checker.execute ()

        # Locate the radio button for Internal
        radio_button =WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "aur_external_0")))
        radio_button.click()

        # # Locate the radio button for External
        # radio_button = driver.find_element (By.ID, "aur_external_1")
        # radio_button.click ()

        # # Locate the toggle button element by its ID, name, or other locator
        # toggle_button = driver.find_element (By.ID, "aur_active")
        # toggle_button.click ()

        # Input text into the input fields
        self.input_field_text(By.ID, "aur_name_last", name_last)
        self.input_field_text(By.ID, "aur_name_first", name_first)
        self.input_field_text(By.ID, "aur_name_middle", name_middle)
        self.input_field_text(By.ID, "aur_name_suffix", name_suffix)
        self.input_field_text(By.ID, "aur_name_prefix", name_prefix)
        self.input_field_text(By.ID, "aur_position", position)
        self.input_field_text ( By.ID, "aur_salary_grade", salary_grade )

        # Find the dropdown element
        agency_dropdown = Select(driver.find_element(By.ID, "aur_agn_id"))
        agency_dropdown.select_by_index(0)

        # Check if the dropdown has options
        if len ( agency_dropdown.options ) == 0:
            # If the dropdown has no options, find and click the "Add" button
            add_button = driver.find_element(By. XPATH,
                "//button[@class='btn btn-outline-secondary add-another-agency']" )  # Replace "add_button_id" with the actual ID of your "Add" button
            add_button.click ()
        else:
            # If the dropdown has options, select an option (optional)
            agency_dropdown.select_by_index ( 2 )  # Select the first option (index 0) as an example

            expertise_dropdown = Select ( driver.find_element ( By.ID, "aur_expertise" ) )
            expertise_dropdown.select_by_index ( 0 )

            # Check if the dropdown has options
            if len ( expertise_dropdown.options ) == 0:
                # If the dropdown has no options, find and click the "Add" button
                add_button = driver.find_element(By. XPATH,
                    "//body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[12]/div[1]/button[1]" )  # Replace "add_button_id" with the actual ID of your "Add" button
                add_button.click ()
            else:
                # If the dropdown has options, select an option (optional)
                agency_dropdown.select_by_index ( 2 )  # Select the first option (index 0) as an example

        # expertise_dropdown = Select (driver.find_element (By.ID, "aur_expertise"))
        # indices_to_select = [1, 4, 6]  # Example indices of options to select
        # for index in indices_to_select:
        #     expertise_dropdown.select_by_index(index)


        self.input_field_text (By.ID, "aur_email", email)

        # Locate the date input field by its ID or other locator
        date_input = driver.find_element(By.ID, "aur_birthdate")

        # Click on the date input field to open the date picker
        date_input.clear()

        # Locate and click on the day element corresponding to the desired date
        desired_date = "03-15-1986"  # Example date in MM-DD-YYYY format
        date_input.send_keys(desired_date)

        self.input_field_text(By.ID, "aur_contact_no", contact_no)

        dropdown = Select(driver.find_element (By.ID, "aur_status"))
        dropdown.select_by_index(2)

        save_button = WebDriverWait ( driver, 10 ).until (
            EC.visibility_of_element_located ( (By.ID, "addAuditor") ) )
        save_button.click ()

        error_checker = ExistingerrorMessage ()
        error_checker.execute ()

        message_instance = Auditorscomplete ()
        message_instance.completion ()
        message_instance.execute ()

# Instantiate the Auditors class and execute its methods
if"__main__" == __name__:
    auditors_instance = Auditors()
    auditors_instance.execute()



