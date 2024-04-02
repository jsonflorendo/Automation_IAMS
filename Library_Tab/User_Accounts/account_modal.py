from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from input import email
from Library_Tab.Auditors_Tab.Auditor_completion import Auditorscomplete
from Login import driver
from account_completion import usercomplete

class user:
    def __init__(self):
        # Initialize any instance-specific attributes here, if needed
        pass

    def add_user(self):
        # Your function code here
        pass

    def input_field_text(self, locator_strategy, locator_value, text):
        input_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((locator_strategy, locator_value)))
        input_field.clear()  # Clear the field in case there is existing text
        input_field.send_keys(text)

    def execute(self):
        # Call the add_agency method
        self.add_user()

        # Find the icon element and click on it
        add_icon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-bs-target='#UserAccountModal']")))
        add_icon.click()

        # # Locate the toggle button element by its ID, name, or other locator
        # toggle_button = driver.find_element (By.ID, "ara_active")
        # toggle_button.click ()

        name_dropdown = WebDriverWait ( driver, 10 ).until (
            EC.element_to_be_clickable ( (By.ID, "usr_aur_id") )
        )

        # Once the dropdown is present, convert it into a Select element
        name_dropdown = Select ( name_dropdown )

        # Select the option by index
        name_dropdown.select_by_index ( 3 )

        level_access_dropdown = Select(driver.find_element(By.ID, "role" ) )
        level_access_dropdown.select_by_index(2)

        # Input text into the input fields
        self.input_field_text(By.ID, "email", email)

        reset_button = WebDriverWait ( driver, 10 ).until (
            EC.visibility_of_element_located ( (By.ID, "reset-password") ) )
        reset_button.click ()

        save_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "addUser")))
        save_button.click()

        message_instance = usercomplete ()
        message_instance.execute ()

# Instantiate the class and execute its methods
if"__main__" == __name__:
    account_instance = user()
    account_instance.execute()



