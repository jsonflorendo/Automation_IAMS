from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login import driver
import unittest

class ModalTest:
    def __init__(self):
        pass

    def asserttext(self):
        # Your function code here
        pass

    def execute(self):
        # Call the add_agency method
        self.asserttext()
        try:
            # XPaths for label elements
            text_xpaths = [
                "//label[normalize-space()='Last Name']",  # XPath for first label element
                "//label[normalize-space()='First Name']",
                "//label[normalize-space()='Middle Name']",
                "//label[normalize-space()='Name Suffix']",
                "//label[normalize-space()='Prefix/Title']",
                "//label[normalize-space()='Position']",
                "//label[normalize-space()='Salary Grade']",
                "//label[normalize-space()='Agency']",
                "//label[normalize-space()='Expertise']",
                "//label[normalize-space()='Email Address']",
                "//label[normalize-space()='Birthdate']",
                "//label[normalize-space()='Contact No.']",
                "//label[normalize-space()='Status']",

                # Add more XPaths for additional label elements if needed
            ]

            # Expected texts corresponding to each XPath
            expected_texts = [
                "Last Name",
                "First Name",
                "Middle Name",
                "Name Suffix",
                "Prefix/Title",
                "Position",
                "Salary Grade",
                "Agency",
                "Expertise",
                "Email Address",
                "Birthdate",
                "Contact No.",
                "Status",


                # Add more expected texts corresponding to each XPath
            ]

            # Iterate through each XPath and its corresponding expected text
            for i, xpath in enumerate ( text_xpaths ):
                # Find the label element within the modal
                label_element = WebDriverWait ( driver, 10 ).until (
                    EC.visibility_of_element_located ( (By.XPATH, xpath) )
                )

                # Extract text from the label element
                actual_text = label_element.text

                # Verify if the actual text matches the expected text
                if actual_text.strip () == expected_texts[i].strip ():
                    print ( f"Field name {i + 1} verification successful! Text: '{actual_text}'" )
                else:
                    print (
                        f"Field name {i + 1} verification failed! Expected: '{expected_texts[i]}', Actual: '{actual_text}'" )

        except Exception as e:
            print ( "An error occurred:", e )

if __name__ == "__main__":
    assert_text = ModalTest()
    assert_text.execute()