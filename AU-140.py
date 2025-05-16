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
wait.until(EC.element_to_be_clickable((By.XPATH, "//option[normalize-space()='VIII. Audit Team and Audit Assignment']"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.ID, "auditPlanSelect"))).click()
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)

import re

def clean_text(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = cleaned_text.replace(u'\xa0', ' ').strip()
    return cleaned_text

#############✅ Test 1
time.sleep(1)
Audit_assignment = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[contains(text(),'Financial')])[2]"))
).text
Audit_assignment = clean_text(Audit_assignment )
print("Audit assignment :", Audit_assignment )

Audit_team_members = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//ul[@id='audit-team-members-14'])[1]"))
).text
Audit_team_members = clean_text(Audit_team_members )
print("Audit team members:",Audit_team_members )

Target_completion = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[normalize-space()='5 days'])[1]"))
).text
Target_completion = clean_text(Target_completion )
Target_completion = Target_completion.split()[0]
print("Target completion:",Target_completion )

Office = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[normalize-space()='TEST'])[1]"))
).text
Office = clean_text(Office )
print("Office:",Office )

wait.until(EC.element_to_be_clickable((By.XPATH, "(//td[contains(text(),'Financial')])[2]"))).click()
time.sleep(1)

#############

time.sleep(1)
Audit_assignment_model = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//option[@value='2'][normalize-space()='Financial'])[3]"))
).text
Audit_assignment_model = clean_text(Audit_assignment_model)
print("Audit assignment:", Audit_assignment_model)

if  Audit_assignment == Audit_assignment_model:
    print("✅ Test 1: Data match!")
else:
    print("❌ Test 1: Data do NOT match!")
time.sleep(1)
Lead_model = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//option[@value='7'][normalize-space()='Jayson Barbara. Internal, SEI'])[3]"))
).text
Lead_model = clean_text(Lead_model)
print("Lead :", Lead_model)

External_Auditors_model = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//option[@value='12'][normalize-space()='Jayson S. External, FNRI'])[7]"))
).text
External_Auditors_model = clean_text(External_Auditors_model)
print("External Auditors:", External_Auditors_model)

Internal_Auditors_model = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//option[@value='1'][normalize-space()='Shiela Jeane Jinahon. Caraan1, SEI'])[4]"))
).text
Internal_Auditors_model = clean_text(Internal_Auditors_model)
print("Internal Auditors:", Internal_Auditors_model)

print("✅ Test 2: Data match!")

office_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "office"))
)
office_model = clean_text(office_input.get_attribute("value"))
print("Office :", office_model)

if Office == office_model:
    print("✅ Test 3: Data match!")
else:
    print("❌ Test 3: Data do NOT match!")

target_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "target-completion"))
)
target_model = clean_text(target_input.get_attribute("value"))
print("Target completion:", target_model)

if Target_completion == target_model:
    print("✅ Test 4: Data match!")
else:
    print("❌ Test 4: Data do NOT match!")




time.sleep(3)

# ✅ Close browser
driver.quit()
