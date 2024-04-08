from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from input import *
from Library_Tab.Auditors_Tab.Auditor_completion import Auditorscomplete
from Login import driver
from modal_assert_agencies import ModalTest
from Agencies_completion import Agenciescomplete

class Agencies:

    def __init__(self):
        # Initialize any instance-specific attributes here, if needed
        pass

    def add_agencies(self):
        pass

    def input_field_text(self, locator_strategy, locator_value, text):
        input_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((locator_strategy, locator_value)))
        input_field.clear()  # Clear the field in case there is existing text
        input_field.send_keys(text)

    def execute(self):
        # Call the add_agency method
        self.add_agencies()

        add_icon = WebDriverWait ( driver, 10 ).until (
            EC.visibility_of_element_located ( (By.XPATH, "//button[@data-bs-target='#AgencyModal']") ) )
        add_icon.click ()

        assert_text = ModalTest ()
        assert_text.execute ()

        # Input text into the input fields
        self.input_field_text(By.ID, "agn_name", name)
        self.input_field_text(By.ID, "agn_acronym", short_name)
        self.input_field_text(By.ID, "agn_address", address)
        self.input_field_text(By.ID, "agn_head_name", name_head)
        self.input_field_text(By.ID, "agn_head_position", position_head)
        self.input_field_text(By.ID, "agn_contact_details", contact_details)

        save_button = WebDriverWait ( driver, 10 ).until (
            EC.visibility_of_element_located ( (By.ID, "addAgency") ) )
        save_button.click ()

        agencies_instance = Agenciescomplete ()
        agencies_instance.execute ()

# Instantiate the class and execute its methods
if "__main__" == __name__:
    agencies_instance = Agencies()
    agencies_instance.execute()
