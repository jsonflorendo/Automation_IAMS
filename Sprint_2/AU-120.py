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
wait.until(EC.element_to_be_clickable((By.XPATH, "//option[normalize-space()='VI. Audit Criteria']"))).click()
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
Audit_area = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[normalize-space()='1234'])[1]"))
).text
Audit_area  = clean_text(Audit_area )
print("Audit area :", Audit_area )

Audit_criteria = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//a[normalize-space()='THIS IS SAMPLES CRITERIA NAM'])[1]"))
).text
Audit_criteria  = clean_text(Audit_criteria )
print("Audit area :", Audit_criteria )

wait.until(EC.element_to_be_clickable((By.XPATH, "(//td[normalize-space()='1234'])[1]"))).click()
time.sleep(1)

#############

time.sleep(1)
Audit_area_model = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//option[@value='18'][normalize-space()='1234'])[2]"))
).text
Audit_area_model = clean_text(Audit_area_model)
print("Audit area:", Audit_area_model)

if  Audit_area == Audit_area_model:
    print("✅ Test 1: Data match!")
else:
    print("❌ Test 1: Data do NOT match!")

Audit_criteria_model = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//label[normalize-space()='THIS IS SAMPLES CRITERIA NAM'])[1]"))
).text
Audit_criteria_model = clean_text(Audit_criteria_model)
print("Audit criteria:", Audit_criteria_model)

if  Audit_criteria == Audit_criteria_model:
    print("✅ Test 2: Data match!")
else:
    print("❌ Test 2: Data do NOT match!")

#############



time.sleep(3)

# ✅ Close browser
driver.quit()
