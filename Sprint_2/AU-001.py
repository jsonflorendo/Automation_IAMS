import sys
sys.path.append('../Automation_IAMS')  # Add the parent directory to the system path
from Login_new import login
login() # call the script of Login_new.py


from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login_new import driver
import time


time.sleep(3)
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[-1])


################### Audit

driver.get("http://10.10.99.18:8002/audit")

AuditModal_plus_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//button[@data-bs-target='#AuditModal'])[1]")))
AuditModal_plus_button.click()
time.sleep(1)

save_plus_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addAudit'])[1]")))
save_plus_button.click()
time.sleep(1)


try:
    title_required = driver.find_element(By.XPATH, "(//span[@id='error-aud_title'])[1]")
    assert title_required.text.strip() == "This field is required.", "Incorrect spelling"
    print("✅test case 1 : title_required Passed")
except NoSuchElementException:
    print("❌ Test Case 1 Failed: title_required")
except AssertionError as e:
    print(f"❌Test Case 1 Failed: {e}")


try:
    types_required = driver.find_element(By.XPATH, "(//span[@id='error-aud_types'])[1]")
    assert types_required.text.strip() == "This field is required.", "Incorrect spelling"
    print("✅test case 2 : types_required Passed")
except NoSuchElementException:
    print("❌ Test Case 2 Failed: types_required")
except AssertionError as e:
    print(f"❌ Test Case 2 Failed: {e}")


try:
    areas_required = driver.find_element(By.XPATH, "(//span[@id='error-aud_areas'])[1]")
    assert areas_required.text.strip() == "This field is required.", "Incorrect spelling"
    print("✅test case 3 : areas_required Passed")
except NoSuchElementException:
    print("❌ Test Case 3 Failed: areas_required")
except AssertionError as e:
    print(f"❌ Test Case 3 Failed: {e}")


try:
    period_from_required = driver.find_element(By.XPATH, "(//span[@id='error-aud_period_from'])[1]")
    assert period_from_required.text.strip() == "This field is required.", "Incorrect spelling"
    print("✅test case 4 : period_from_required Passed")
except NoSuchElementException:
    print("❌ Test Case 4 Failed: period_from_required")
except AssertionError as e:
    print(f"❌Test Case 4 Failed: {e}")


try:
    period_to_required = driver.find_element(By.XPATH, "(//span[@id='error-aud_period_to'])[1]")
    assert period_to_required.text.strip() == "This field is required.", "Incorrect spelling"
    print("✅test case 5 : period_to_required Passed")
except NoSuchElementException:
    print("❌ Test Case 5 Failed: period_to_required")
except AssertionError as e:
    print(f"❌Test Case 5 Failed: {e}")


title_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "(//textarea[@id='aud_title'])[1]")))
title_input .send_keys("Test 11")
time.sleep(1)


type_input = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//span[@role='combobox'])[1]")))
type_input.click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[contains(text(), 'Financial')]").click()
time.sleep(1)


agency_input = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//span[@role='combobox'])[2]")))
agency_input.click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[contains(text(), 'Financial')]").click()
time.sleep(1)


period_from_input = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//select[@id='aud_period_from'])[1]")))
period_from_input.click()
time.sleep(1)
driver.find_element(By.XPATH, "//select[@id='aud_period_from']/option[text()='2021']").click()
time.sleep(1)


period_to_input = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//select[@id='aud_period_to'])[1]")))
period_to_input.click()
time.sleep(1)
driver.find_element(By.XPATH, "//select[@id='aud_period_to']/option[text()='2023']").click()
time.sleep(1)


audit_save = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addAudit'])[1]")))
audit_save.click()
time.sleep(1)


try:
    audit_save_message_label = driver.find_element(By.ID, "swal2-title")
    actual_text = audit_save_message_label.text.strip()
    assert actual_text.startswith("Audit with reference no.") and actual_text.endswith("added successfully"), "Message format is incorrect"
    print("✅Test Case 6: audit_save_message_label Passed")
except NoSuchElementException:
    print("❌ Test Case 6 Failed: audit_save_message_label not found")
except AssertionError as e:
    print(f"❌ Test Case 6 Failed: {e}")


audit_ok = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]")))
audit_ok.click()
time.sleep(1)


################### Auditees

Auditees = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='Auditees'])[1]")))
Auditees.click()
time.sleep(1)

Auditees_plus_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-plus text-white-100'])[2]")))
Auditees_plus_button.click()

Auditees_save_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addAuditee'])[1]")))
Auditees_save_button.click()
time.sleep(1)


try:
    auditees_title_required = driver.find_element(By.XPATH, "(//span[@id='error-aue_aud_id'])[1]")
    assert auditees_title_required.text.strip() == "This field is required.", "Incorrect spelling"
    print("✅Test Case 7: auditees_title_required Passed")
except NoSuchElementException:
    print("❌ Test Case 7 Failed: auditees_title_required not found")
except AssertionError as e:
    print(f"❌ Test Case 7 Failed: {e}")


try:
    auditees_name_required = driver.find_element(By.XPATH, "(//span[@id='error-aue_agn_id'])[1]")
    assert auditees_name_required.text.strip() == "This field is required.", "Incorrect spelling"
    print("✅Test case 8 :  auditees_name_required Passed")
except NoSuchElementException:
    print("❌ Test Case 8 Failed:  auditees_name_required")
except AssertionError as e:
    print(f"❌ Test Case 8 Failed: {e}")

try:
    auditees_assign_required = driver.find_element(By.XPATH, "(//span[@id='error-aue_aur_id'])[1]")
    actual_text = auditees_assign_required.text.strip()
    assert actual_text == "This field is required.", "Incorrect spelling"
    print("✅Test case 9 :  auditees_assign_required Passed")
except NoSuchElementException:
    print("❌ Test Case 9 Failed:  auditees_assign_required")
except AssertionError as e:
    print(f"❌ Test Case 9 Failed: {e}")


auditees_title_input = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//select[@id='aue_aud_id'])[1]")))
auditees_title_input.click()
time.sleep(1)
driver.find_element(By.XPATH, "(//option[normalize-space()='IT Audit Plan'])[1]").click()
time.sleep(1)


auditees_name_input = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//select[@id='aue_agn_id'])[1]")))
auditees_name_input.click()
time.sleep(1)
driver.find_element(By.XPATH, "(//option[@value='26'][normalize-space()='Department of Social Welfare and Development'])[1]").click()
time.sleep(1)


auditees_name_input = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//select[@id='aue_aur_id'])[1]")))
auditees_name_input.click()
time.sleep(1)
driver.find_element(By.XPATH, "(//option[normalize-space()='De Guzman, Mecaella Fallena'])[1]").click()
time.sleep(1)


auditees_save = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addAuditee'])[1]")))
auditees_save.click()
time.sleep(1)


try:
    auditees_save_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Auditee added successfully'])[1]")
    assert auditees_save_message_label .text.strip() == "Auditee added successfully", "Incorrect spelling"
    print("✅test case 10 : auditees_save_message_label Passed")
except NoSuchElementException:
    print("❌ Test Case 10 Failed: auditees_save_message_label ")
except AssertionError as e:
    print(f"❌ Test Case 10 Failed: {e}")


auditees_ok = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]")))
auditees_ok.click()

time.sleep(3)

# ✅ Close browser
driver.quit()
