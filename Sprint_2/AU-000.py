import sys
sys.path.append('../Automation_IAMS')  # Add the parent directory to the system path
from Login_new import login
login() # call the script of Login_new.py


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login_new import driver
import time


time.sleep(3)
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[-1])

import re

def clean_text(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = cleaned_text.replace(u'\xa0', ' ').strip()
    return cleaned_text

#############✅ Test 1

driver.get("http://10.10.99.18:8002/audit")
time.sleep(1)
No = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[normalize-space()='2025-73'])[1]"))
).text
No = clean_text(No)
print("NO:", No)

#############✅ Test 2

Title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//td[normalize-space()='Annual Compliance Audit'])[1]"))).text
Title = clean_text(Title)
print("Title:", Title)

#############✅ Test 3

Auditee = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//td[contains(text(),'NHS')])[1]"))).text
Auditee = clean_text(Auditee)
print("Auditee:", Auditee)

#############✅ Test 4

Type_of_Audit = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//td[normalize-space()='Environmental'])[1]"))).text
Type_of_Audit = clean_text(Type_of_Audit)
print("Type of Audit:", Type_of_Audit)

#############✅ Test 5

Agency = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//td[normalize-space()='Revenue'])[1]"))).text
Agency = clean_text(Agency)
print("Agency:", Agency)

#############✅ Test 6

Status = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//td)[15]"))).text
Status = clean_text(Status)
print("Status:", Status)

#############✅ Test 7

Description_Remarks = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[8]"))).text
Description_Remarks = clean_text(Description_Remarks)
print("Description/Remarks:", Description_Remarks)

#############

print("\n")

driver.get("http://10.10.99.18:8002/auditDetails/73")
time.sleep(1)
AUDIT_No = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='aud-no fw-bold text-primary'])[1]"))).text
AUDIT_No = clean_text(AUDIT_No)
print("AUDIT No.:", AUDIT_No)

if No == AUDIT_No:
    print("✅ Test 1: Data match!")
else:
    print("❌ Test 1: Data do NOT match!")

print("\n")

Title_model = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='aud-title'])[1]"))).text
Title_model = clean_text(Title_model)
print("Title :", Title_model)

if Title == Title_model:
    print("✅ Test 2: Data match!")
else:
    print("❌ Test 2: Data do NOT match!")

print("\n")

Auditee_model = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//td[contains(text(),'NHS')])[1]"))).text
Auditee_model = clean_text(Auditee_model)
print("Auditee :", Auditee_model)

if Auditee== Auditee_model:
    print("✅ Test 3: Data match!")
else:
    print("❌ Test 3: Data do NOT match!")

print("\n")

Type_of_Audit_model = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='aud-type'])[1]"))).text
Type_of_Audit_model = clean_text(Type_of_Audit_model)
print("Audit type :", Type_of_Audit_model)

if Type_of_Audit== Type_of_Audit_model:
    print("✅ Test 4: Data match!")
else:
    print("❌ Test 4: Data do NOT match!")

print("\n")

Agency_model = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='aud-areas'])[1]"))).text
Agency_model = clean_text(Agency_model)
print("Audit type :", Agency_model)

if Agency== Agency_model:
    print("✅ Test 5: Data match!")
else:
    print("❌ Test 5: Data do NOT match!")

print("\n")

Status_model = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='aud-open fw-bold'])[1]"))).text
Status_model = clean_text(Status_model)
print("Status :", Status_model)

if Status== Status_model:
    print("✅ Test 6: Data match!")
else:
    print("❌ Test 6: Data do NOT match!")

print("\n")

Description_model = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='aud-desc'])[1]"))).text
Description_model = clean_text(Description_model)

Remarks_model = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='aud-remarks'])[1]"))).text
Remarks_model = clean_text(Remarks_model)

Description_Remarks_model = f"{Description_model} {Remarks_model}"
print("Description/Remarks:", Description_Remarks_model)

if Description_Remarks== Description_Remarks_model:
    print("✅ Test 7: Data match!")
else:
    print("❌ Test 7: Data do NOT match!")

#############

time.sleep(5)

# ✅ Close browser
driver.quit()
