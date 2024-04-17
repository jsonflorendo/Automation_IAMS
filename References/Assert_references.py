from Login import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class referencetable(unittest.TestCase):
    def __init__(self):
        super().__init__()
        # Initialize any instance-specific attributes here, if needed
        pass

    def reference_column_names(self):
        # Locate the table element
        try:
            # Locate the table element
            table = WebDriverWait ( driver, 10 ).until ( EC.visibility_of_element_located (
                (By.ID, "tbl-references") ) )  # Adjust the XPath as per your table's structure

            # Locate the header row of the table
            header_row = table.find_element ( By.XPATH,
                                              "//table[@id='tbl-references']//thead/tr" )  # Adjust the XPath as per your table's structure

            # Retrieve the text from each cell in the header row
            column_names = [cell.text for cell in header_row.find_elements ( By.XPATH, ".//th" )]

            # Assert the column names match the expected values
            expected_column_names = ["Reference No.", "Name/Title", "Description", "Type of Document", "Audit Area", "Last Updated", "Action"]  # Adjust this list with your expected column names
            assert column_names == expected_column_names, f"Expected column names {expected_column_names}, but got {column_names}"

            # If assertion passes, print confirmation
            print ( "Column names assertion passed:", expected_column_names )

        except Exception as e:
            # Handle any exceptions or assertion failures
            print ( f"An error occurred: {e}" )

if __name__ == "__main__":
    assert_reference = referencetable()
    assert_reference.reference_column_names ()
