import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from tkinter import messagebox

# Initialize Chrome WebDriver Service
service = Service(executable_path="C:/Users/Teacher/Desktop/Report/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the BSPMS Login Page
driver.get("http://10.10.99.18:8004/login")

# Verify the Page Title
title = driver.title
expected_title = "BSPMS - Balik Scientist Program Management System"

# Locate Login Form Elements
if expected_title != title:
    messagebox.showerror("Login Failed", "Page title doesn't match.")
    raise AssertionError("Login Test Failed")
else:
    print("Logged in Successfully")

# Enter Email and Password Credentials
email_input = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input.send_keys("sjjinahon@gmail.com")
password.send_keys("Dost@123")
try:
    assert email_input.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password.get_attribute("value") == "Dost@123", "Password input mismatch"
    print("Logged in Successfully")
except AssertionError as e:
    print(f"7th attempt Assertion failed: {e}")
login_button.click()
time.sleep(3)

print("Successfully entered the page.")

# Verify Header Text: 'REPUBLIC OF THE PHILIPPINES
try:
    expected_text = "REPUBLIC OF THE PHILIPPINES"
    header = driver.find_element(By.XPATH, "//p[text()='Republic of the Philippines']")
    actual_text = header.text.strip()

    if actual_text == expected_text:
        print(f"Header text verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Header text verification FAILED: Expected '{expected_text}', but found '{actual_text}'")
        assert False, "Header text mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify Header Text: 'Balik Scientist Program'
try:
    expected_text = "Balik Scientist Program"
    header = driver.find_element(By.XPATH, '//p[normalize-space(text())="Balik Scientist Program"]')
    actual_text = header.text.strip()

    if actual_text == expected_text:
        print(f"Header text verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Header text verification FAILED: Expected '{expected_text}', but found '{actual_text}'")
        assert False, "Header text mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify Header Text: 'DEPARTMENT OF SCIENCE AND TECHNOLOGY
try:
    expected_text = "DEPARTMENT OF SCIENCE AND TECHNOLOGY"
    header = driver.find_element(By.XPATH, '//p[normalize-space(text())="Department of Science and Technology"]')
    actual_text = header.text.strip()

    if actual_text == expected_text:
        print(f"Header text sverification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Header text verification FAILED: Expected '{expected_text}', but found '{actual_text}'")
        assert False, "Header text mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify the 'Applications' sidebar menu label
try:
    expected_text = "Applications"
    App_label = driver.find_element(By.XPATH, '//*[@id="drawer-navigation"]/div[1]/ul/li/a/span[2]')
    actual_text = App_label.text.strip()

    if actual_text == expected_text:
        print(f"Sidebar menu label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Sidebar menu label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Sidebar menu label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify the 'Applications' header label
try:
    expected_text = "Applications"
    App_label = driver.find_element(By.XPATH, '//*[@id="bsp-content"]/header/div/h2/div/span')
    actual_text = App_label.text.strip()

    if actual_text == expected_text:
        print(f"Header text verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Header text verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Header text mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify the 'Filter by' label on the Applications page
try:
    expected_text = "Filter by"
    filter_label = driver.find_element(By.XPATH, '//*[@id="bsp-content"]/main/div[1]/div[1]/div[1]/span')
    actual_text = filter_label.text.strip()

    if actual_text == expected_text:
        print(f"Filter label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Filter label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Filter label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify Profile button visibility and navigate to profile page
try:
    Profile = driver.find_element(By.XPATH, '//*[@id="user-menu-button"]')
    assert Profile.is_displayed(), "Profile button is not visible."
    driver.execute_script("arguments[0].click();", Profile)
    time.sleep(3)
    print("Navigated to profile page.")
except AssertionError as ae:
    print(f"Assertion failed: {ae}")
except Exception as e:
    print(f"Error occurred while clicking Profile: {e}")

print("Navigated to profile page.")

# Verify 'SYSTEM ADMIN' label in the profile dropdown
try:
    expected_text = "SYSTEM ADMIN"
    SysAd_label = driver.find_element(By.XPATH, '//*[@id="user-dropdown"]/div/span[1]')
    actual_text = SysAd_label.text.strip()

    if actual_text == expected_text:
        print(f"System Admin label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"System Admin label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "System Admin label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify 'Monitoring Council' sub-label in the profile dropdown
try:
    expected_text = "Monitoring Council"
    DOSTCO_label = driver.find_element(By.XPATH, '//*[@id="user-dropdown"]/div/span[2]')
    actual_text = DOSTCO_label.text.strip()

    if actual_text == expected_text:
        print(f"DOST-CO sub-label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"DOST-CO sub-label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "DOST-CO label mismatch"
except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify 'Change password' action link
try:
    expected_text = "Change password"
    Change_Ac = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
    actual_text = Change_Ac.text.strip()

    if actual_text == expected_text:
        print(f"Change password Action link verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Change password Acation link verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Change password label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")


# Verify that the "Log Out" action link is displayed and has correct text
try:
    expected_text = "Log Out"
    Log_Out = driver.find_element(By.XPATH, '//*[@id="logout-button"]')
    actual_text = Log_Out.text.strip()

    if actual_text == expected_text:
        print(f"Log Out Action link verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Log Out Action link verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Log Out label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Click the "Change Password" button
try:
    Change_pass = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
    assert Change_pass.is_displayed(), "Change Password button is not visible."
    driver.execute_script("arguments[0].click();", Change_pass)
    time.sleep(2)
    print("The Change Password button was clicked.")
except AssertionError as ae:
    print(f"Assertion failed: {ae}")
except Exception as e:
    print(f"Error occurred while clicking Change Password: {e}")

# Verify "Change Password" modal title text
try:
    expected_text = "Change Password"
    ChangePass = driver.find_element(By.XPATH, '//*[@id="change_password_modal"]/div/div/div[1]/h3')
    actual_text = ChangePass.text.strip()

    if actual_text == expected_text:
        print(f"Change password Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Change password label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Change password label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify "Confirm New Password" label in form
try:
    expected_text = "Confirm New Password"
    ChangePass = driver.find_element(By.XPATH, '//*[@id="change_password_form"]/div/div[3]/label')
    actual_text = ChangePass.text.strip()

    if actual_text == expected_text:
        print(f"Change New password Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Change New password label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Change New password label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify "Current Password" label in form
try:
    expected_text = "Current Password"
    ChangePass = driver.find_element(By.XPATH, '//*[@id="change_password_form"]/div/div[1]/label')
    actual_text = ChangePass.text.strip()

    if actual_text == expected_text:
        print(f"Current password Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Current password label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Change New password label mismatch"
except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "New Password"
    ChangePass = driver.find_element(By.XPATH, '//*[@id="change_password_form"]/div/div[2]/label')
    actual_text = ChangePass.text.strip()

    if actual_text == expected_text:
        print(f"New password Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"New password label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "New password label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify "Confirm New Password" label again in form
try:
    expected_text = "Confirm New Password"
    ChangePass = driver.find_element(By.XPATH, '//*[@id="change_password_form"]/div/div[3]/label')
    actual_text = ChangePass.text.strip()

    if actual_text == expected_text:
        print(f"Change New password Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Change New password label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Change New password label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify "Save" button text in form
try:
    expected_text = "Save"
    ChangePass = driver.find_element(By.XPATH, '//*[@id="save_password_button"]')
    actual_text = ChangePass.text.strip()

    if actual_text == expected_text:
        print(f"Button Text verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Button Text verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Button Text mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")


# Close the Change Password modal by clicking the close button
try:
    Close_but = driver.find_element(By.ID, "change_password_modal_close")
    assert Close_but.is_displayed(), "Close button is not visible."
    driver.execute_script("arguments[0].click();", Close_but)
    time.sleep(2)
    print("It closed the close button of the change password modal.")
except AssertionError as ae:
    print(f"Assertion failed: {ae}")
except Exception as e:
    print(f"Error occurred while clicking the close button: {e}")

# Click the Profile button to navigate to Profile page
try:
    Profile = driver.find_element(By.XPATH, '//*[@id="user-menu-button"]')
    assert Profile.is_displayed(), "Profile button is not visible."
    driver.execute_script("arguments[0].click();", Profile)
    time.sleep(3)
    print("Navigated to profile page.")
except AssertionError as ae:
    print(f"Assertion failed: {ae}")
except Exception as e:
    print(f"Error occurred while clicking Profile: {e}")

print("Navigated to profile page.")


# Click the "Change Password" button again to reopen the modal
try:
    Change_pass = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
    assert Change_pass.is_displayed(), "Change Password button is not visible."
    driver.execute_script("arguments[0].click();", Change_pass)
    time.sleep(2)
    print("The Change Password button was clicked.")
except AssertionError as ae:
    print(f"Assertion failed: {ae}")
except Exception as e:
    print(f"Error occurred while clicking Change Password: {e}")

# Clear password fields and attempt to submit the form with empty fields
Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Save = driver.find_element(By.XPATH, '//*[@id="save_password_button"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("")
New_pass.send_keys("")
Confirm_pass.send_keys("")
Save.click()
time.sleep(2)

try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

# Verify error message
try:
    expected_text = "This field is required."
    Error_Message = driver.find_element(By.XPATH, '//*[@id="current_password_error"]')
    actual_text = Error_Message.text.strip()

    if actual_text == expected_text:
        print(f"Error Message verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Error Message verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Error Message mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify error message for New Password required field
try:
    expected_text = "This field is required."
    Error_Message = driver.find_element(By.XPATH, '//*[@id="new_password_error"]')
    actual_text = Error_Message.text.strip()

    if actual_text == expected_text:
        print(f"Error Message verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Error Message verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Error Message mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify error message for Confirm New Password required field
try:
    expected_text = "This field is required."
    Error_Message = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation_error"]')
    actual_text = Error_Message.text.strip()

    if actual_text == expected_text:
        print(f"Error Message verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Error Message verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Error Message mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")


# Click the Change Password button to open the modal
Change_pas = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
driver.execute_script("arguments[0].click();", Change_pas)
time.sleep(2)
print("The Change Password button was clicked.")

# Fill out Change Password form with valid values and save
Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Save = driver.find_element(By.XPATH, '//*[@id="save_password_button"]')

Current_pass.send_keys("Dost@12345")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("Dost@123")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

ok = driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='OK']")
driver.execute_script("arguments[0].click();", ok)
time.sleep(2)

Change_pass = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
driver.execute_script("arguments[0].click();", Change_pass)
time.sleep(2)
Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Change_pass = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
driver.execute_script("arguments[0].click();", Change_pass)
time.sleep(2)
Current_pass.send_keys("Dost@123")
New_pass.send_keys("Dost@12345")
Confirm_pass.send_keys("Dost@123")
Save.click()
time.sleep(3)

# Verify password fields retain expected values after submission
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

try:
    expected_text = "Passwords do not match."
    Error_Message = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation_error"]')
    actual_text = Error_Message.text.strip()

    if actual_text == expected_text:
        print(f"Error Message verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Error Message verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Error Message"

except AssertionError as e:
    print(f"Assertion failed: {e}")


Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("Dost@123")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("Dost@12345")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("A7f$5Lp@9xQ2mZe6sW1vBn8T#pY4dJhVkC5uEoGqRtX1y!Ws12345")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("Dost@123")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

# Click OK on success SweetAlert popup
ok = driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='OK']")
driver.execute_script("arguments[0].click();", ok)
time.sleep(2)

Profile = driver.find_element(By.XPATH, '//*[@id="user-menu-button"]')
driver.execute_script("arguments[0].click();", Profile)
time.sleep(2)

Change_pass = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
driver.execute_script("arguments[0].click();", Change_pass)
time.sleep(2)

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("Dost@1")
New_pass.send_keys("A7f$5Lp@9xQ2mZe6sW1vBn8T#pY4dJhVkC5uEoGqRtX1y!Ws12345")
Confirm_pass.send_keys("Dost@12")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("Dost@1")
New_pass.send_keys("Dost@1")
Confirm_pass.send_keys("A7f$5Lp@9xQ2mZe6sW1vBn8T#pY4dJhVkC5uEoGqRtX1y!Ws12345")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("Dost@123")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("Dost@123")
New_pass.send_keys("")
Confirm_pass.send_keys("Dost@12345")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("Dost@123")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.send_keys("Dost@123")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("Dost@123")
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
    print("Change password Successfully")
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")
Save.click()
time.sleep(2)



# Verify the 'Filter by' label
try:
    expected_text = "Password changed successfully."
    Modal_label = driver.find_element(By.XPATH, '//*[@id="swal2-title"]')
    actual_text = Modal_label.text.strip()

    if actual_text == expected_text:
        print(f"Modal label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Modal label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Modal label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify modal message for session timeout and ensure it displays the correct label
try:
    expected_text = "Please login again."
    Modal_label = driver.find_element(By.XPATH, '//*[@id="swal2-html-container"]')
    actual_text = Modal_label.text.strip()

    if actual_text == expected_text:
        print(f"Sub-label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Sub-label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Sub-label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify OK button text on modal
try:
    expected_text = "OK"
    Modal_label = driver.find_element(By.XPATH, "//button[text()='OK']")
    actual_text = Modal_label.text.strip()

    if actual_text == expected_text:
        print(f"Button Text verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Button Text verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Button Text mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Click the OK button on the modal
ok_button = driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='OK']")
ok_button.click()
time.sleep(2)

# Re-login with provided credentials
email_input6 = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password6 = driver.find_element(By.ID, "password")
login_button6 = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input6.send_keys("sjjinahon@gmail.com")
password6.send_keys("Dost@123")
try:
    assert email_input6.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password6.get_attribute("value") == "Dost@123", "Password input mismatch"
    print("Logged in Successfully")
except AssertionError as e:
    print(f"7th attempt Assertion failed: {e}")
login_button6.click()
time.sleep(3)

print("Successfully entered the page.")


# Verify the 'Filter by' label
try:
    expected_text = "Filter by"
    filter_label = driver.find_element(By.XPATH, '//*[@id="bsp-content"]/main/div[1]/div[1]/div[1]/span')
    actual_text = filter_label.text.strip()

    if actual_text == expected_text:
        print(f"Filter label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Filter label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Filter label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Click the ellipsis button to open the options menu
Ell = driver.find_element(By.XPATH, '//*[@id="applications_table"]/tbody/tr[1]/td[6]/div/button')
driver.execute_script("arguments[0].click();", Ell)
time.sleep(3)

# Verify the 'Assign to' label in the menu
try:
    expected_text = "Assign to"
    Assign = driver.find_element(By.XPATH, "//*[@id='assign-menu-item']")
    actual_text = Assign.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")


# Verify the 'Edit' label in the menu
try:
    expected_text = "Edit"
    Edit = driver.find_element(By.XPATH, '//*[@id="edit-menu-item"]')
    actual_text = Edit.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")


# Verify the 'Track' label in the menu
try:
    expected_text = "Track"
    Track = driver.find_element(By.XPATH, '//*[@id="track-menu-item"]')
    actual_text = Track.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")


# Verify the 'Attach' label in the menu
try:
    expected_text = "Attach"
    Attach = driver.find_element(By.XPATH, '//*[@id="attach-menu-item"]')
    actual_text = Attach.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")


# Verify the 'Delete' label in the menu
try:
    expected_text = "Delete"
    Delete = driver.find_element(By.XPATH, '//*[@id="delete-menu-item"]')
    actual_text = Delete.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Hover over the 'Assign to' element and highlight each lists
assign_to = wait(driver, 4).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='assign-menu-item']")))
ActionChains(driver).move_to_element(assign_to).perform()
Alist = wait(driver, 4).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='assign-submenu']/div/button[1]")))
print("Found Assign to:", assign_to.text)
driver.execute_script("arguments[0].style.border='2px solid gray'", Alist)
time.sleep(4)
driver.execute_script("arguments[0].style.border=''", assign_to)

# Verify the 'DOST-CO' label in the assign submenu
try:
    expected_text = "DOST-CO"
    Co = driver.find_element(By.XPATH, '//*[@id="assign-submenu"]/div/button[1]')
    actual_text = Co.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")


# Verify the 'PCAARRD' label in the assign submenu
try:
    expected_text = "PCAARRD"
    PCA = driver.find_element(By.XPATH, '//*[@id="assign-submenu"]/div/button[2]')
    actual_text = PCA.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")


# Verify the 'PCHRD' label in the assign submenu
try:
    expected_text = "PCHRD"
    PCH = driver.find_element(By.XPATH, '//*[@id="assign-submenu"]/div/button[3]')
    actual_text = PCH.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")


# Verify the 'PCIEERD' label in the assign submenu
try:
    expected_text = "PCIEERD"
    PCI = driver.find_element(By.XPATH, '//*[@id="assign-submenu"]/div/button[4]')
    actual_text = PCI.text.strip()

    if actual_text == expected_text:
        print(f"Label verification pASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Edit Menu Interaction
Edit = driver.find_element(By.XPATH, '//*[@id="edit-menu-item"]')
driver.execute_script("arguments[0].style.border='2px solid gray'", Edit)
ActionChains(driver).move_to_element(Edit).perform()
time.sleep(3)
driver.execute_script("arguments[0].click();", Edit)
time.sleep(3)
driver.back()
time.sleep(2)
driver.execute_script("arguments[0].style.border=''", Edit)


# Track Menu Interaction
Ellipsissss = driver.find_element(By.XPATH, '//*[@id="applications_table"]/tbody/tr[1]/td[6]/div/button')
driver.execute_script("arguments[0].click();", Ellipsissss)
time.sleep(3)
Track = driver.find_element(By.XPATH, '//*[@id="track-menu-item"]')
driver.execute_script("arguments[0].style.border='2px solid gray'", Track)
ActionChains(driver).move_to_element(Track).perform()
time.sleep(3)
driver.execute_script("arguments[0].click();", Track)
time.sleep(3)
Close = driver.find_element(By.XPATH, '//*[@id="tracking-modal"]/div/div/div[1]/button')
driver.execute_script("arguments[0].click();", Close)
time.sleep(3)
driver.execute_script("arguments[0].style.border=''", Track)


# Attach Menu Interaction
Ellipsissss = driver.find_element(By.XPATH, '//*[@id="applications_table"]/tbody/tr[1]/td[6]/div/button')
driver.execute_script("arguments[0].click();", Ellipsissss)
time.sleep(3)
Attach = driver.find_element(By.XPATH, '//*[@id="attach-menu-item"]')
driver.execute_script("arguments[0].style.border='2px solid gray'", Attach)
ActionChains(driver).move_to_element(Attach).perform()
time.sleep(3)
driver.execute_script("arguments[0].click();", Attach)
time.sleep(3)
Close_A = driver.find_element(By.XPATH, '//*[@id="attachments-modal"]/div/div/div[1]/button')
driver.execute_script("arguments[0].click();", Close_A)
time.sleep(3)
driver.execute_script("arguments[0].style.border=''", Attach)


# Delete Menu Interaction
Ellipsissss = driver.find_element(By.XPATH, '//*[@id="applications_table"]/tbody/tr[1]/td[6]/div/button')
driver.execute_script("arguments[0].click();", Ellipsissss)
time.sleep(3)
Delete = driver.find_element(By.XPATH, '//*[@id="delete-menu-item"]')
driver.execute_script("arguments[0].style.border='2px solid gray'", Delete)
ActionChains(driver).move_to_element(Delete).perform()
time.sleep(3)
driver.execute_script("arguments[0].click();", Delete)
time.sleep(3)
Cancel = driver.find_element(By.XPATH, "//button[@class='swal2-cancel swal2-styled' and text()='Cancel']")
driver.execute_script("arguments[0].click();", Cancel)

try:
    expected_text = "Are you sure you want to delete this item?"
    PCH = driver.find_element(By.XPATH, '//*[@id="swal2-title"]')
    actual_text = PCH.text.strip()

    if actual_text == expected_text:
        print(f"Verification message PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Verification messaage FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Cancel"
    PCH = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[6]/button[3]')
    actual_text = PCH.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Delete"
    PCH = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[6]/button[1]')
    actual_text = PCH.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

time.sleep(3)
driver.execute_script("arguments[0].style.border=''", Delete)

# Verify No. Column Sorting
No = driver.find_element(By.XPATH, '//span[contains(@class, "ascending") and contains(@class, "icon-[solar--sort-vertical-bold-duotone]")]')
driver.execute_script("arguments[0].click();", No)
time.sleep(2)
No1 = driver.find_element(By.XPATH, '//span[contains(@class, "descending") and contains(@class, "icon-[solar--sort-vertical-bold-duotone]")]')
driver.execute_script("arguments[0].click();", No1)
time.sleep(2)

try:
    expected_text = "No."
    No = driver.find_element(By.XPATH, '//*[@id="applications_table"]/thead/tr/th[1]/button/div/span[4]')
    actual_text = No.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

Name = driver.find_element(By.XPATH, '//span[text()="Name"]')
driver.execute_script("arguments[0].click();", Name)
time.sleep(2)
Name1 = driver.find_element(By.XPATH, '//span[text()="Name"]')
driver.execute_script("arguments[0].click();", Name1)
time.sleep(2)

try:
    expected_text = "Name"
    Name = driver.find_element(By.XPATH, '//*[@id="applications_table"]/thead/tr/th[2]/button/div/span[4]')
    actual_text = Name.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")


Engagement = driver.find_element(By.XPATH, '//span[text()="Engagement"]')
driver.execute_script("arguments[0].click();", Engagement)
time.sleep(2)
Engagement1 = driver.find_element(By.XPATH, '//span[text()="Engagement"]')
driver.execute_script("arguments[0].click();", Engagement1)
time.sleep(2)

try:
    expected_text = "Engagement"
    Engage = driver.find_element(By.XPATH, '//*[@id="applications_table"]/thead/tr/th[3]/button/div/span[4]')
    actual_text = Engage.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

HostI = driver.find_element(By.XPATH, '//span[text()="Host Institution"]')
driver.execute_script("arguments[0].click();", HostI)
time.sleep(2)
HostI1 = driver.find_element(By.XPATH, '//span[text()="Host Institution"]')
driver.execute_script("arguments[0].click();", HostI1)
time.sleep(2)

try:
    expected_text = "Host Institution"
    Host_I = driver.find_element(By.XPATH, '//*[@id="applications_table"]/thead/tr/th[4]/button/div/span[4]')
    actual_text = Host_I.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

Status = driver.find_element(By.XPATH, '//span[text()="Status"]')
driver.execute_script("arguments[0].click();", Status)
time.sleep(2)
Status1 = driver.find_element(By.XPATH, '//span[text()="Status"]')
driver.execute_script("arguments[0].click();", Status1)
time.sleep(2)

dropdown_element = driver.find_element(By.ID, "council_filter")
dropdown_element.click()
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("DOST-CO")
time.sleep(1)
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("PCAARRD")
time.sleep(1)
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("PCIEERD")
time.sleep(1)
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("PCHRD")
time.sleep(1)
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("All")
time.sleep(1)

try:
    expected_text = "All"
    label = driver.find_element(By.XPATH, '//*[@id="council_filter"]/option[1]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "DOST-CO"
    label = driver.find_element(By.XPATH, '//*[@id="council_filter"]/option[2]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "PCAARRD"
    label = driver.find_element(By.XPATH, '//*[@id="council_filter"]/option[3]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "PCHRD"
    label = driver.find_element(By.XPATH, '//*[@id="council_filter"]/option[4]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "PCIEERD"
    label = driver.find_element(By.XPATH, '//*[@id="council_filter"]/option[5]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

dropdown1 = driver.find_element(By.ID, 'status_filter')
dropdown1.click()
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Approval')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Legal Clearance')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Evaluation')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Request')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Others')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Approved')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Disapproved')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Revision')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Status')
time.sleep(1)

try:
    expected_text = "Status"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[1]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Approval"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[2]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Legal Clearance"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[3]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Evaluation"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[4]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Request"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[5]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Others"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[6]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Approved"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[7]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Disapproved"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[8]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Revision"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[9]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Search..."
    label = driver.find_element(By.XPATH, '//*[@id="applications_search"]')
    actual_text = label.get_attribute('placeholder').strip()

    if actual_text == expected_text:
        print(f"Label verification passed: '{actual_text}' matches expected.")
    else:
        print(f"Label verification failed: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

search_input = driver.find_element(By.ID, 'applications_search')
search_input.send_keys("ñew")
time.sleep(2)
search_input.clear()
search_input = driver.find_element(By.ID, 'applications_search')
search_input.send_keys("ÑEW")
time.sleep(2)
search_input.clear()
search_input = driver.find_element(By.ID, 'applications_search')
search_input.send_keys("M@%ks*")
time.sleep(2)
search_input.clear()
search_input = driver.find_element(By.ID, 'applications_search')
search_input.send_keys("Lan")
time.sleep(2)

Select_data = driver.find_element(By.XPATH, '//*[@id="applications_table"]/tbody/tr/td[2]')
driver.execute_script("arguments[0].click();", Select_data)
time.sleep(5)
print("Data had been selected")

original_window = driver.current_window_handle
all_windows = driver.window_handles

for window in all_windows:
    driver.switch_to.window(window)
    if "BSPMS - Balik Scientist Program Management System" in driver.title:
        print("Currently at Selected Profile window.")
        break

driver.get("http://10.10.99.18:8004/applications")

print("Navigated to BSPMS")
time.sleep(3)

Profile = driver.find_element(By.XPATH, '//*[@id="user-menu-button"]')
driver.execute_script("arguments[0].click();", Profile)
time.sleep(3)
print("Navigated to profile page.")

try:
    expected_text = "Log Out"
    label = driver.find_element(By.XPATH, '//*[@id="logout-button"]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"Action link verification passed: '{actual_text}' matches expected.")
    else:
        print(f"Action link verification failed: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Action link mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "© 2025"
    label = driver.find_element(By.XPATH, '//*[@id="drawer-navigation"]/div[2]/p[1]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"Action link verification passed: '{actual_text}' matches expected.")
    else:
        print(f"Action link verification failed: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Action link mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "DEPARTMENT OF SCIENCE AND TECHNOLOGY"
    label = driver.find_element(By.XPATH, '//*[@id="drawer-navigation"]/div[2]/p[2]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"Action link verification passed: '{actual_text}' matches expected.")
    else:
        print(f"Action link verification failed: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Action link mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "ALL RIGHTS RESERVED"
    label = driver.find_element(By.XPATH, '//*[@id="drawer-navigation"]/div[2]/p[3]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"Action link verification passed: '{actual_text}' matches expected.")
    else:
        print(f"Action link verification failed: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Action link mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

Log_Out = driver.find_element(By.XPATH, '//*[@id="logout-button"]')
driver.execute_script("arguments[0].click();", Log_Out)
time.sleep(2)
print("Logout completed.")


input("Press Enter to exit and close the browser...")
driver.quit()
