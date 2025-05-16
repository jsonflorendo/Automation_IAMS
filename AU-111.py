import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://10.10.99.18:8002/login")
driver.maximize_window()
#driver.execute_script("document.body.style.zoom='50%'")


wait = WebDriverWait(driver, 15)

username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
username_input.send_keys("bnjmntumbaga@gmail.com")

password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
password_input.send_keys("Dost@123")

login_button = wait.until(EC.element_to_be_clickable((By.ID, "login")))
login_button.click()

time.sleep(3)
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[-1])


TARGET_URL = "http://10.10.99.18:8002/auditDetails/73"
driver.get(TARGET_URL)
driver.execute_script("document.body.style.zoom='80%'")
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.ID, "auditPlanSelect"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "//option[normalize-space()='III. Audit Objectives']"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.ID, "auditPlanSelect"))).click()
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-plus'])[1]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addAuditObjective'])[1]"))).click()
time.sleep(1)

try:
    Audit_Objective_message_label = driver.find_element(By.XPATH, "(//span[@id='error-obj_desc'])[1]")
    assert Audit_Objective_message_label.text.strip() == "This field is required.", "Incorrect spelling"
    print("✅Test case 1 : Required Audit_Objective_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 1 Failed: Required Audit_Objective_message_label")
except AssertionError as e:
    print(f"❌Test Case 1 Failed: {e}")

try:
    Audit_ActionPlans_message_label = driver.find_element(By.XPATH, "(//span[@id='error-empty-action-plan'])[1]")
    assert Audit_ActionPlans_message_label.text.strip() == "This field is required.", "Incorrect spelling"
    print("✅Test case 2 : Required Audit_ActionPlans_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 2 Failed: Required Audit_ActionPlans_message_label")
except AssertionError as e:
    print(f"❌Test Case 2 Failed: {e}")

time.sleep(1)
Audit_Objective_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//textarea[@id='obj_desc'])[1]")))
Audit_Objective_input.send_keys("object TEST")

time.sleep(1)
Audit_ActionPlans_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//textarea[@class='form-control'])[5]")))
Audit_ActionPlans_input.send_keys("audit TEST")

time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-plus'])[5]"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-minus'])[1]"))).click()
time.sleep(1)

try:
    Audit_delete_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Are you sure you want to delete this item?'])[1]")
    assert Audit_delete_message_label.text.strip() == "Are you sure you want to delete this item?", "Incorrect spelling"
    print("✅Test case 3 : Audit_delete_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 3 Failed: Audit_delete_message_label")
except AssertionError as e:
    print(f"❌Test Case 3 Failed: {e}")

time.sleep(1)
Audit_delete_ok_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='swal2-actions']//button[normalize-space()='OK' or normalize-space()='Ok']"))
)
Audit_delete_ok_button.click()
time.sleep(1)
try:
    Audit_success_delete_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Action Plan deleted successfully'])[1]")
    assert Audit_success_delete_message_label.text.strip() == "Action Plan deleted successfully", "Incorrect spelling"
    print("✅Test case 4 : Audit_success_delete_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 4 Failed: Audit_success_delete_message_label")
except AssertionError as e:
    print(f"❌Test Case 4 Failed: {e}")

time.sleep(1)
Audit_success_ok_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='swal2-actions']//button[normalize-space()='OK' or normalize-space()='Ok']"))
)
Audit_success_ok_button.click()
time.sleep(1)

time.sleep(1)
Audit_ActionPlans_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//textarea[@class='form-control'])[5]")))
Audit_ActionPlans_input.send_keys("audit TEST")

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addAuditObjective'])[1]"))).click()
time.sleep(1)

try:
    Audit_success_save_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Audit Objective added successfully'])[1]")
    assert Audit_success_save_message_label.text.strip() == "Audit Objective added successfully", "Incorrect spelling"
    print("✅Test case 5 : Audit_success_save_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 5 Failed: Audit_success_save_message_label")
except AssertionError as e:
    print(f"❌Test Case 5 Failed: {e}")
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]"))).click()
time.sleep(1)

#################################### audit criteria
wait.until(EC.element_to_be_clickable((By.ID, "auditPlanSelect"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "//option[normalize-space()='VI. Audit Criteria']"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.ID, "auditPlanSelect"))).click()
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-plus'])[2]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='update-area-criteria-entry'])[1]"))).click()
time.sleep(1)

try:
    Audit_criteria_save_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Audit Criteria updated successfully'])[1]")
    assert Audit_criteria_save_message_label.text.strip() == "Audit Criteria updated successfully", "Incorrect spelling"
    print("✅Test case 6 : Audit_criteria_save_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 6 Failed: Audit_criteria_save_message_label")
except AssertionError as e:
    print(f"❌Test Case 6 Failed: {e}")
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-plus'])[2]"))).click()
time.sleep(1)

audit_criteria_input = wait.until(EC.element_to_be_clickable((By.XPATH, "(//select[@id='crn_ara_id'])[1]")))
audit_criteria_input.click()
time.sleep(1)
driver.find_element(By.XPATH, "(//option[@value='2'][normalize-space()='Financial'])[2]").click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='clear-area-criteria-entry'])[1]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@name='crn_cra_id[]'])[1]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='update-area-criteria-entry'])[1]"))).click()
time.sleep(1)

try:
    Audit_criteria_save_add_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Audit Criteria updated successfully'])[1]")
    assert Audit_criteria_save_add_message_label.text.strip() == "Audit Criteria updated successfully", "Incorrect spelling"
    print("✅Test case 7 : Audit_criteria_save_add_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 7 Failed: Audit_criteria_save_add_message_label")
except AssertionError as e:
    print(f"❌Test Case 7 Failed: {e}")
time.sleep(1)
Audit_criteria_save_ok_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='swal2-actions']//button[normalize-space()='OK' or normalize-space()='Ok']"))
)
Audit_criteria_save_ok_button.click()
time.sleep(1)

time.sleep(5)

# ✅ Close browser
driver.quit()
