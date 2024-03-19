from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from input import name
from Library_Tab.Auditors_Tab.Auditor_completion import Auditorscomplete
from Login import driver
from Auditarea_completion import Areacomplete

class Area:
    def __init__(self):
        # Initialize any instance-specific attributes here, if needed
        pass

    def add_area(self):
        # Your function code here
        pass

    def input_field_text(self, locator_strategy, locator_value, text):
        input_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((locator_strategy, locator_value)))
        input_field.clear()  # Clear the field in case there is existing text
        input_field.send_keys(text)

    def execute(self):
        # Call the add_agency method
        self.add_area()

        # Find the icon element and click on it
        add_icon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-bs-target='#AuditAreaModal']")))
        add_icon.click()

        # # Locate the toggle button element by its ID, name, or other locator
        # toggle_button = driver.find_element (By.ID, "ara_active")
        # toggle_button.click ()

        # Input text into the input fields
        self.input_field_text(By.ID, "ara_name", name)

        dropdown = Select(driver.find_element(By.ID, "ara_ara_id"))
        dropdown.select_by_index(9)

        icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='addAuditArea']")))
        icon.click()

        area_message_instance = Areacomplete ()
        area_message_instance.areacompletion ()
        area_message_instance.execute ()


# Instantiate the Auditors class and execute its methods
if"__main__" == __name__:
    areas_instance = Area()
    areas_instance.execute()



