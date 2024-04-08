from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from input import name
from Library_Tab.Type_of_audit.audit_completion import auditcomplete
from Login import driver
from audit_completion import auditcomplete
from modal_assert_audit import ModalTest
class audit:
    def __init__(self):
        # Initialize any instance-specific attributes here, if needed
        pass

    def add_audittype(self):
        # Your function code here
        pass

    def input_field_text(self, locator_strategy, locator_value, text):
        input_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((locator_strategy, locator_value)))
        input_field.clear()  # Clear the field in case there is existing text
        input_field.send_keys(text)

    def execute(self):
        # Call the add_agency method
        self.add_audittype()

        # Find the icon element and click on it
        add_icon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-bs-target='#TypeOfAuditModal']")))
        add_icon.click()

        assert_text = ModalTest ()
        assert_text.execute ()

        # Input text into the input fields
        self.input_field_text(By.ID, "aud_name", name)

        icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "addTypeOfAudit")))
        icon.click()

        message_instance = auditcomplete ()
        message_instance.execute ()

# Instantiate the class and execute its methods
if"__main__" == __name__:
    audit_instance = audit()
    audit_instance.execute()



