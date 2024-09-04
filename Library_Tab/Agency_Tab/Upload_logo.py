from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from input import *
from Library_Tab.Auditors_Tab.Auditor_completion import Auditorscomplete
from Login import driver
from modal_assert_agencies import ModalTest
from Agencies_completion import Agenciescomplete
from error_message_assert import error_message
import pyautogui
import time

class Agencies:

    def __init__(self):
        # Initialize any instance-specific attributes here, if needed
        pass

    def add_agencies(self):
        # Your function code here
        pass

    def input_field_text(self, locator_strategy, locator_value, text):
        input_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((locator_strategy, locator_value)))
        input_field.clear()  # Clear the field in case there is existing text
        input_field.send_keys(text)

    def execute(self):
        # Call the add_agency method
        self.add_agencies()

        add_icon = WebDriverWait ( driver, 10 ).until (
            EC.visibility_of_element_located ( (By.XPATH, "//button[@data-bs-target='#AgencyModal']") ) )
        add_icon.click ()



        # Locate the button element
        button = driver.find_element ( By.ID, "agn_logo" )  # Adjust locator based on your button

        # Create an ActionChains object
        actions = ActionChains ( driver )

        # Double-click the button using ActionChains
        actions.double_click ( button ).perform ()
        # Logic for uploading the image (assuming the upload happens after the double-click)
        if "upload" in driver.current_url or "file_input" in driver.page_source:  # Check for upload indicators
            # Locate the file upload element (assuming it appears after double-click)
            file_input = driver.find_element ( By.ID, "file_input" )  # Adjust locator as needed
            file_input.click ()

            wait = WebDriverWait ( driver, 10 )  # Wait for 10 seconds for the file dialog
            wait.until (
                EC.presence_of_element_located ( (By.XPATH, "//input[@type='file']") ) )  # Adjust XPath as needed

            # Use pyautogui to interact with the file dialog
            file_path = r"C:\ITD\Desktop\Pancit_Ilonggo_Style_-_12110747826.jpg"

            # Type the file path and press Enter
            pyautogui.write ( file_path )
            pyautogui.press ( "enter" )
        else:
            print ( "Upload functionality not detected on this page." )  # Handle the case if upload isn't present

# Instantiate the class and execute its methods
if "__main__" == __name__:
    logo_instance = Agencies()
    logo_instance.execute()
