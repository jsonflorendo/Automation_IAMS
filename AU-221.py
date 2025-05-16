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

driver.get("http://10.10.99.18:8002/auditor")
driver.maximize_window()


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

import re

def clean_text(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = cleaned_text.replace(u'\xa0', ' ').strip()
    return cleaned_text

#############✅ Test 1
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-plus'])[1]"))).click()
time.sleep(1)

auditees_input= wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@name='icq_auditees[]'])[1]")))
auditees_input .send_keys("Benjamin S. Tumbaga JR.")
time.sleep(1)

reference1_model = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//td)[4]"))
).text
reference1_model = clean_text(reference1_model)
print("Reference:", reference1_model)

reference2_model = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//td)[10]"))
).text
reference2_model = clean_text(reference2_model)
print("Reference:", reference2_model)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//td[@class='updateIcqParticularsRow'])[1]"))).click()
time.sleep(1)

reference1 = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//textarea[normalize-space()='fghfgfgfg'])[1]"))
).text
Audit_assignment_model = clean_text(reference1)
print("Reference:", reference1)

if  reference1_model == reference1:
    print("✅ Test 1: Data match!")
else:
    print("❌ Test 1: Data do NOT match!")

reference2 = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//textarea[normalize-space()='fgfgfg'])[1]"))
).text
reference2 = clean_text(reference2)
print("Reference:", reference2)

if  reference2_model == reference2:
    print("✅ Test 2: Data match!")
else:
    print("❌ Test 2: Data do NOT match!")

time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Close'])[2]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='btn btn-default btn-sm border-1'])[1]"))).click()
time.sleep(1)

try:
    delete_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Are you sure you want to delete this item?'])[1]")
    message_text = delete_message_label.text.strip()

    if message_text == "Are you sure you want to delete this item?":
        print("✅ Test Case 3: delete_message_label Passed")
    else:
        print(f"❌ Test Case 3 Failed: Text mismatch - Found '{message_text}'")
except Exception as e:
    print(f"❌ Test Case 3 Failed: delete_message_label not found - {str(e)}")

time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Ok'])[1]"))).click()
time.sleep(3)

# ✅ Close browser
driver.quit()
