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


TARGET_URL = "http://10.10.99.18:8002/auditDetails/88"
driver.get(TARGET_URL)
driver.execute_script("document.body.style.zoom='80%'")
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.ID, "auditPlanSelect"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "//option[normalize-space()='VIII. Audit Team and Audit Assignment']"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.ID, "auditPlanSelect"))).click()
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='audit-teams-modal-trigger'])[1]"))).click()
time.sleep(1)


try:
    Audit_Team_message_label = driver.find_element(By.XPATH, "(//div[@id='error-assigned_auditors'])[1]")
    assert Audit_Team_message_label.text.strip() == "The selected audit area does not have an auditor with the required expertise.", "Incorrect spelling"
    print("✅Test case 1 : Audit_Team_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 1 Failed: Audit_Team_message_label")
except AssertionError as e:
    print(f"❌Test Case 1 Failed: {e}")
time.sleep(1)

############### select audit area

time.sleep(1)
select_audit_area_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select-audit-area")))
select_audit_area_dropdown.click()
select_audit_area_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='select-audit-area']//option[@value='2'][normalize-space()='Financial']")))
select_audit_area_option.click()


time.sleep(1)
Lead_value_dropdown =wait.until(EC.element_to_be_clickable((By.XPATH, "(//select[@id='tm_lead'])[1]")))
Lead_value_dropdown.click()
Lead_value_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='tm_lead']//option[@value='7'][normalize-space()='Jayson Barbara. Internal, SEI']")))
Lead_value_option.click()

external_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@role='combobox'])[2]")))
driver.execute_script("arguments[0].click();", external_dropdown)
time.sleep(1)
external_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='tm_int_aud']//option[@value='12'][normalize-space()='Jayson S. External, FNRI']")))
external_option.click()



####################### select Internal Auditors
time.sleep(1)
internal_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@role='combobox'])[3]")))
driver.execute_script("arguments[0].click();", internal_dropdown)
time.sleep(1)
internal_option = wait.until(
EC.element_to_be_clickable((By.XPATH, "(//option[@value='1'][normalize-space()='Shiela Jeane Jinahon. Caraan1, SEI'])[4]")))
internal_option.click()


####################### Assignment office

office = wait.until(EC.presence_of_element_located((By.ID, "office")))
office.send_keys("TEST")
time.sleep(1)
####################### Assignment Target Completion

target_completion = wait.until(EC.presence_of_element_located((By.ID, "target-completion")))
target_completion.send_keys("5")
time.sleep(1)

####################### Plus and Minus
wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-plus'])[8]"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-minus'])[1]"))).click()

time.sleep(1)
try:
    Remove_alert_Label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Are you sure you want to delete this item?'])[1]")
    actual_text = Remove_alert_Label.text.strip()

    assert actual_text == "Are you sure you want to delete this item?", f"Incorrect spelling: Found '{actual_text}'"
    print("✅Test case 2: Remove_alert_Label Passed")
except NoSuchElementException:
    print("❌Test case 2: Remove_alert_Label")
except AssertionError as e:
    print(f"❌Test case 2: {e}")

time.sleep(1)

ok = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Ok'])[1]")))
ok.click()

time.sleep(1)

try:
    deleted_successfully = driver.find_element(By.XPATH, "(//h2[normalize-space()='Activity deleted successfully'])[1]")
    actual_text = deleted_successfully.text.strip()

    assert actual_text == "Activity deleted successfully", f"Incorrect spelling: Found '{actual_text}'"
    print("✅Test case 3: deleted_successfully message Passed")
except NoSuchElementException:
    print("❌Test case 3: deleted_successfully")
except AssertionError as e:
    print(f"❌Test case 3: {e}")
    time.sleep(1)

ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='swal2-actions'])[1]")))
ok_button.click()
time.sleep(1)


save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addAuditTeam'])[1]")))
save_button.click()

time.sleep(1)

try:
    Save_notify_Label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Audit Team added successfully'])[1]")
    actual_text = Save_notify_Label.text.strip()

    assert actual_text == "Audit Team added successfully", f"Incorrect spelling: Found '{actual_text}'"
    print("✅Test case 4: Remove_alert Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌Test case 4: Remove_alert label Not Found")
except AssertionError as e:
    print(f"❌Test case 4: {e}")

time.sleep(1)
save_ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]")))
save_ok_button.click()
time.sleep(1)

################### next page
nextSection = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='nextSectionBtn'])[1]")))
nextSection.click()

time.sleep(1)
driver.execute_script("document.body.style.zoom='80%'")
driver.execute_script("window.scrollBy(0, 1000);")

time.sleep(1)
SelectExpenseCategory = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='line-item-budget-trigger'])[1]")))
SelectExpenseCategory.click()

#################### IX. Line-Item Budget label
save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addLineItemBudget'])[1]")))
save_button.click()
time.sleep(1)

try:
    line_item_message_label = driver.find_element(By.XPATH, "(//span[@class='error-message text-danger'][normalize-space()='This field is required.'])[1]")
    assert line_item_message_label.text.strip() == "This field is required.", "Incorrect spelling"
    print("✅Test case 5 : Required line_item_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 5 Failed: Required line_item_message_label")
except AssertionError as e:
    print(f"❌Test Case 5 Failed: {e}")

try:
    Details_message_label = driver.find_element(By.XPATH, "(//span[@class='error-message text-danger'][normalize-space()='This field is required.'])[2]")
    assert Details_message_label.text.strip() == "This field is required.", "Incorrect spelling"
    print("✅Test case 6 : Required Details_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 6 Failed: Required Details_message_label")
except AssertionError as e:
    print(f"❌Test Case 6 Failed: {e}")

try:
    Amount_message_label = driver.find_element(By.XPATH, "(//span[normalize-space()='The amount field must have 0-2 decimal places.'])[1]")
    assert Amount_message_label.text.strip() == "The amount field must have 0-2 decimal places.", "Incorrect spelling"
    print("✅Test case 7 : Amount_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 7 Failed: Amount_message_label")
except AssertionError as e:
    print(f"❌Test Case 7 Failed: {e}")


################################ input
time.sleep(2)
SelectExpenseCategorySelection = wait.until(EC.element_to_be_clickable((By.XPATH, "(//option[normalize-space()='Representation Expense'])[1]")))
SelectExpenseCategorySelection.click()
selected_value = driver.find_element(By.XPATH, "(//option[normalize-space()='Representation Expense'])[1]").get_attribute("value")


time.sleep(1)
lineItem = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='line-item'])[1]")))
lineItem.send_keys("Test line-item")


time.sleep(1)
details = wait.until(EC.presence_of_element_located((By.XPATH, "(//textarea[@id='details'])[1]")))
details.send_keys("Test details")



time.sleep(1)
calculator = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='calculator-popover'])[1]")))
calculator.click()

time.sleep(1)
calculator7 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='7'])[1]")))
calculator7.click()

time.sleep(1)
CalculatorPlus = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='+'])[1]")))
CalculatorPlus.click()

time.sleep(1)
Calculator5 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='5'])[1]")))
Calculator5.click()

time.sleep(1)
CalculatorEqual = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='='])[1]")))
CalculatorEqual.click()

time.sleep(1)
CopyResult = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='Copy Result'])[1]")))
CopyResult.click()

amount_field = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='lib-amount'])[1]")))
amount_value = amount_field.get_attribute("value")
time.sleep(1)

save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addLineItemBudget'])[1]")))
save_button.click()
time.sleep(1)

try:
    line_item_save_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Line-Item Budget added successfully'])[1]")
    assert line_item_save_message_label .text.strip() == "Line-Item Budget added successfully", "Incorrect spelling"
    print("✅Test case 8 : line_item_save_message_label  Passed")
except NoSuchElementException:
    print("❌Test Case 8 Failed: line_item_save_message_label ")
except AssertionError as e:
    print(f"❌Test Case 8 Failed: {e}")

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]"))).click()
time.sleep(1)

time.sleep(5)

# ✅ Close browser
driver.quit()
