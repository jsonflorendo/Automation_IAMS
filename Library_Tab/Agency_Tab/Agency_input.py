from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from Login import driver

class Agency:
    def __init__(self):
        # Initialize any instance-specific attributes here, if needed
        pass

    def add_agency(self):
        # Your function code here
        pass

    def input_field_text(self, locator_strategy, locator_value, text):
        input_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((locator_strategy, locator_value)))
        input_field.clear()  # Clear the field in case there is existing text
        input_field.send_keys(text)

    def execute(self):
        # Call the add_agency method
        self.add_agency()

        # Find the icon element and click on it
        icon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-bs-target='#AgencyModal']")))
        icon.click()

        # Input text into the input fields
        self.input_field_text(By.ID, "agn_name", "Deaprtment of Science and Technology")
        self.input_field_text(By.ID, "agn_acronym", "DOST")
        self.input_field_text(By.ID, "agn_address", "DOST COmpound, Bicutan Taguig City")
        self.input_field_text(By.ID, "agn_head_name", "Sec. Solidum1")
        self.input_field_text(By.ID, "agn_head_position", "Secretary1")
        self.input_field_text(By.ID, "agn_contact_details", "F883781113")

        icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "addAgency")))
        icon.click()

# Instantiate the Agency class and execute its methods
if"__main__" == __name__:
    agency_instance = Agency()
    agency_instance.execute()



