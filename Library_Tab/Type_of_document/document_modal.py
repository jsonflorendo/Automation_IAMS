from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from input import name
from Library_Tab.Auditors_Tab.Auditor_completion import Auditorscomplete
from Login import driver
from document_completion import documentcomplete

class document:
    def __init__(self):
        # Initialize any instance-specific attributes here, if needed
        pass

    def add_document(self):
        # Your function code here
        pass

    def input_field_text(self, locator_strategy, locator_value, text):
        input_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((locator_strategy, locator_value)))
        input_field.clear()  # Clear the field in case there is existing text
        input_field.send_keys(text)

    def execute(self):
        # Call the add_agency method
        self.add_document()

        # Find the icon element and click on it
        add_icon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-bs-target='#TypeOfDocumentModal']//i[@class='fas fa-plus fa-2x text-white-100']")))
        add_icon.click()

        # # Locate the toggle button element by its ID, name, or other locator
        # toggle_button = driver.find_element (By.ID, "ara_active")
        # toggle_button.click ()

        # Input text into the input fields
        self.input_field_text(By.ID, "typ_name", name)

        icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "addTypeOfDocument")))
        icon.click()

        message_instance = documentcomplete ()
        message_instance.execute ()

# Instantiate the class and execute its methods
if"__main__" == __name__:
    document_instance = document()
    document_instance.execute()



