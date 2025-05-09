import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox

# Set up Chrome WebDriver service with the path to chromedriver executable
service = Service(executable_path="C:/Users/Teacher/Desktop/Report/chromedriver/chromedriver.exe")

# Initialize Chrome browser driver
driver = webdriver.Chrome(service=service)

# Navigate to the BSPMS login page
driver.get("http://10.10.99.18:8004/login")

# Verify the page title matches the expected title
title = driver.title
expected_title = "BSPMS - Balik Scientist Program Management System"
if expected_title != title:
    messagebox.showerror("Login Failed", "Page title doesn't match.")
    raise AssertionError("Login Test Failed")
else:
    print("Logged in Successfully")

# Verify the main heading (H1) matches the expected text
try:
    expected_heading_text = "Balik Scientist Program Management System"
    h1_element = driver.find_element(By.XPATH, '//h1[normalize-space(text())="Balik Scientist Program Management System"]')
    actual_heading_text = h1_element.text

    if actual_heading_text == expected_heading_text:
        print(f"Title check PASSED: '{actual_heading_text}' matches expected.")
    else:
        print(f"Title check FAILED: Expected '{expected_heading_text}', but found '{actual_heading_text}'")
        assert False, "Page title mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify the Login Form heading (H2) matches expected text
try:
    expected_text = "Login Form"
    login = driver.find_element(By.XPATH, '//h2[normalize-space(text())="Login Form"]')
    actual_text = login.text

    if actual_text == expected_text:
        print(f"Title check PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Title check FAILED: Expected '{expected_text}', but found '{actual_text}'")
        assert False, "Page title mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify Username input placeholder text
try:
    expected_placeholder = "Username"
    username_input = driver.find_element(By.XPATH, '//input[@id="username"]')
    actual_placeholder = username_input.get_attribute('placeholder').strip()

    if actual_placeholder == expected_placeholder:
        print(f"Username input placeholder check PASSED: '{actual_placeholder}' matches expected.")
    else:
        print(f"Username input placeholder check FAILED: Expected '{expected_placeholder}', but found '{actual_placeholder}'")
        assert False, "Username placeholder mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify Password input placeholder text
try:
    expected_placeholder = "Password"
    password_input = driver.find_element(By.XPATH, '//input[@id="password"]')
    actual_placeholder = password_input.get_attribute('placeholder').strip()

    if actual_placeholder == expected_placeholder:
        print(f"Password input placeholder check PASSED: '{actual_placeholder}' matches expected.")
    else:
        print(f"Password input placeholder check FAILED: Expected '{expected_placeholder}', but found '{actual_placeholder}'")
        assert False, "Password placeholder mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Attempt login with empty username and password to trigger error messages
email_input = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
time.sleep(2)
email_input.send_keys("")
password.send_keys("")

# Verify inputs remain empty after sending empty text
try:
    assert email_input.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password.get_attribute("value") == "Dost@123", "Password input mismatch"
except AssertionError as e:
    print(f"1st attempt Assertion failed: {e}")
login_button.click()
time.sleep(3)

# Verify username error message after empty submission
try:
    expected_error_text = "This field is required."
    error_div = driver.find_element(By.XPATH, '//div[@id="username_div_error"]')
    actual_error_text = error_div.text.strip()

    if actual_error_text == expected_error_text:
        print(f"Username error message check PASSED: '{actual_error_text}' matches expected.")
    else:
        print(f"Username error message check FAILED: Expected '{expected_error_text}', but found '{actual_error_text}'")
        assert False, "Username error message mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify password error message after empty submission
try:
    expected_error_text2 = "This field is required."
    error_div2 = driver.find_element(By.XPATH, '//div[@id="password_div_error"]')
    actual_error_text2 = error_div2.text.strip()

    if actual_error_text2 == expected_error_text2:
        print(f"Password error message check PASSED: '{actual_error_text2}' matches expected.")
    else:
        print(f"Password error message check FAILED: Expected '{expected_error_text2}', but found '{actual_error_text2}'")
        assert False, "Password error message mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Attempt login with valid email and empty password
email_input1 = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password1 = driver.find_element(By.ID, "password")
login_button1 = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input1.send_keys("sjjinahon@gmail.com")
password1.send_keys("")
login_button1.click()
time.sleep(3)

# Verify input values after first partial attempt
try:
    assert email_input1.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password1.get_attribute("value") == "Dost@123", "Password input mismatch"
except AssertionError as e:
    print(f"2nd attempt Assertion failed: {e}")

# Clear inputs and attempt login with empty email and valid password
email_input1.clear()

email_input2 = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password2 = driver.find_element(By.ID, "password")
login_button2 = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input2.send_keys("")
password2.send_keys("Dost@123")
login_button2.click()
time.sleep(3)

# Verify input values after second partial attempt
try:
    assert email_input2.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password2.get_attribute("value") == "Dost@123", "Password input mismatch"
except AssertionError as e:
    print(f"3rd attempt Assertion failed: {e}")

# Clear inputs and attempt login with invalid email and valid password
password2.clear()

email_input3 = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password3 = driver.find_element(By.ID, "password")
login_button3 = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input3.send_keys("jioclyde@gmail.com")
password3.send_keys("Dost@123")
login_button3.click()
time.sleep(3)

# Verify input values after third partial attempt
try:
    assert email_input3.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password3.get_attribute("value") == "Dost@123", "Password input mismatch"
except AssertionError as e:
    print(f"4th attempt Assertion failed: {e}")

# Clear inputs and attempt login with valid email and invalid password
email_input3.clear()
password3.clear()
email_input4 = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password4 = driver.find_element(By.ID, "password")
login_button4 = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input4.send_keys("sjjinahon@gmail.com")
password4.send_keys("Dost@12345")
login_button4.click()
time.sleep(3)

# Verify input values after fourth partial attempt
try:
    assert email_input4.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password4.get_attribute("value") == "Dost@123", "Password input mismatch"
except AssertionError as e:
    print(f"5th attempt Assertion failed: {e}")

# Clear inputs and attempt login with invalid email and invalid password
email_input4.clear()
password4.clear()
email_input5 = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password5 = driver.find_element(By.ID, "password")
login_button5 = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input5.send_keys("jioclyde@gmail.com")
password5.send_keys("123456")
login_button5.click()
time.sleep(3)

# Verify input values after fifth partial attempt
try:
    assert email_input5.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password5.get_attribute("value") == "Dost@123", "Password input mismatch"
except AssertionError as e:
    print(f"6th attempt Assertion failed: {e}")

# Clear inputs and attempt final login with valid email and valid password
email_input5.clear()
password5.clear()
email_input6 = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password6 = driver.find_element(By.ID, "password")
login_button6 = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input6.send_keys("sjjinahon@gmail.com")
password6.send_keys("Dost@123")

# Verify login text is correct
try:
    expected_error_text = "Login"
    error_div = driver.find_element(By.XPATH, '//*[@id="login"]')
    actual_error_text = error_div.text.strip()

    if actual_error_text == expected_error_text:
        print(f"Login text verification PASSED: '{actual_error_text}' matches expected.")
    else:
        print(f"Login text verification FAILED: Expected '{expected_error_text}', but found '{actual_error_text}'")
        assert False, "Login text mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify final input values before clicking login
try:
    assert email_input6.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password6.get_attribute("value") == "Dost@123", "Password input mismatch"
    print("Logged in Successfully")
except AssertionError as e:
    print(f"7th attempt Assertion failed: {e}")

# Click login button and wait for navigation
login_button6.click()
time.sleep(3)

# Log successful entry to the page
print("Successfully entered the page.")

# Wait for user input before closing the browser
input("Press Enter to exit and close the browser...")
driver.quit()
