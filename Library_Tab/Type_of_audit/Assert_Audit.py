from Login import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class audittable(unittest.TestCase):
    def __init__(self):
        super().__init__()
        # Initialize any instance-specific attributes here, if needed
        pass

    def audit_column_names(self):
        # Locate the table element
        try:
            # Locate the table element
            table = WebDriverWait ( driver, 10 ).until ( EC.visibility_of_element_located (
                (By.XPATH, "//div[@class='dataTables_scrollHead']")))  # Adjust the XPath as per your table's structure

            # Locate the header row of the table
            header_row = table.find_element ( By.XPATH,"//th[contains(text(),'Type of Audit')]" )  # Adjust the XPath as per your table's structure

            # Retrieve the text from each cell in the header row
            column_names = [cell.text for cell in header_row.find_elements ( By.XPATH, ".//th" )]

            # Assert the column names match the expected values
            expected_column_names = ["Type of Audit"] # Adjust this list with your expected column names
            assert column_names == expected_column_names, f"Expected column names {expected_column_names}, but got {column_names}"

            # If assertion passes, print confirmation
            print ( "Column names assertion passed:", expected_column_names )

        except Exception as e:
            # Handle any exceptions or assertion failures
            print ( f"An error occurred: {e}" )
#
# # Assert table data to data from edit modal
#             # Locate the table cell containing the text you want to assert
#             table_cell_xpath = "//table[@id='table_id']/tbody/tr[1]/td[2]"
#
#             table_cell = WebDriverWait ( driver, 10 ).until (
#                 EC.visibility_of_element_located ( (By.XPATH, table_cell_xpath) ) )
#
#             # Get the text from the table cell
#             table_cell_text = table_cell.text
#
#             # Locate the edit modal
#             edit_modal = driver.find_element ( By.ID, "edit_modal" )
#
#             # Locate the input field in the edit modal containing the corresponding data
#             input_field = edit_modal.find_element ( By.ID,
#                                                     "input_field_id" )  # Replace "input_field_id" with the actual ID of the input field
#
#             # Get the text from the input field in the edit modal
#             edit_modal_text = input_field.get_attribute ( "value" )
#
#             # Assert the text
#             assert table_cell_text == edit_modal_text, f"Text in table cell '{table_cell_text}' does not match text in edit modal '{edit_modal_text}'"

if __name__ == "__main__":
    assert_audit = audittable()
    assert_audit.audit_column_names()