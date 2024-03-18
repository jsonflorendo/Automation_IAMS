import driver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch the browser
driver = webdriver.Chrome()

# Define your function
def my_function():
    # Your function code here
    pass

# Execute your function if the script is run directly
if __name__ == "__main__":
    my_function()

driver.maximize_window ()

driver.get("http://10.10.99.18:8002/login")

# Define the class name of the element you want to find
class_name = "text-center"
expected_field_name = "LOGIN"

try:
    # Attempt to find the element using its class name
    element = driver.find_element(By.CLASS_NAME, class_name)

    # Retrieve the text of the element
    field_name = element.text.strip()

    # Check if the retrieved field name matches the expected field name
    if field_name == expected_field_name:
        print(f"Field with class '{class_name}' has the correct name '{expected_field_name}'!")
    else:
        print(f"Field with class '{class_name}' has a different name: '{field_name}'")
except NoSuchElementException:
    print(f"Element with class '{class_name}' does not exist!")

class_name = "form-label"
expected_field_name = "Username"

try:
    # Attempt to find the element using its class name
    element = driver.find_element(By.CLASS_NAME, class_name)

    # Retrieve the text of the element
    field_name = element.text.strip()

    # Check if the retrieved field name matches the expected field name
    if field_name == expected_field_name:
        print(f"Field with class '{class_name}' has the correct name '{expected_field_name}'!")
    else:
        print(f"Field with class '{class_name}' has a different name: '{field_name}'")
except NoSuchElementException:
    print(f"Element with class '{class_name}' does not exist!")

password_id = "form-control"
expected_field_name = "Password"

try:
    # Attempt to find the password input field using its ID
    element = driver.find_element(By.CSS_SELECTOR, "label[for='password']")

    # Retrieve the label text associated with the password input field
    # label_element = driver.find_element(By.CSS_SELECTOR, password_id)
    field_name = element.text.strip()

    # Check if the retrieved field name matches the expected field name
    if field_name == expected_field_name:
        print (f"Field with id '{password_id}' has the correct name '{expected_field_name}'!")
    else:
        print (f"Field with id '{password_id}' has a different name: '{expected_field_name}'")
except NoSuchElementException:
    print (f"Element with id '{password_id}' does not exist!")

login_button = "btn bsb-btn-xl btn-primary"
expected_field_name = "LOGIN"

try:
     # Attempt to find the password input field using its ID
    element = driver.find_element (By.CSS_SELECTOR, "#login")

    # Retrieve the label text associated with the password input field
        # label_element = driver.find_element(By.CSS_SELECTOR, password_id)
    field_name = element.text.strip ()

    # Check if the retrieved field name matches the expected field name
    if field_name == expected_field_name:
            print(f"Field with id '{login_button}' has the correct name '{expected_field_name}'!")
    else:
        print(f"Field with id '{login_button}' has a different name: '{expected_field_name}'")
except NoSuchElementException:
    print(f"Element with id '{login_button}' does not exist!")

    # Find the username and password input fields and submit button
username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login")))

# Input your credentials
username_field.send_keys("superadmin1@gmail.com")

# Introduce a delay
# time.sleep(1)

password_field.send_keys("qwerqwer")
# Introduce a delay
# time.sleep(1)

# Click the submit button
login_button.click()

# # Wait for the login process to complete and page to load (you may need to adjust the timeout value)
# WebDriverWait(driver, 10).until(EC.url_to_be("http://10.10.99.18:8002/dashboard"))
# input("Please enter")
# # Close the browser window
# driver.quit()
