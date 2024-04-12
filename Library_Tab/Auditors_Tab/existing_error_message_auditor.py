from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login import driver
import unittest

class ExistingerrorMessage:
    def __init__(self):
        pass

    def execute(self):
        try:
            # error message for existing email address
            wait = WebDriverWait ( driver, 10 )
            existing_email_error = wait.until ( EC.visibility_of_element_located (
                (By.XPATH, "//span[@id='error-aur_email']") ) )

            if existing_email_error.is_displayed ():
                print ( "The email address is already taken." )

        except Exception as e:
            print ( f"An error occurred: {e}" )

if __name__ == "__main__":
    error_checker = ExistingerrorMessage()
    error_checker.execute()