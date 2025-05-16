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
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-chevron-right fa-2x'])[1]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-chevron-right fa-2x'])[1]"))).click()
time.sleep(1)

import re

def clean_text(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = cleaned_text.replace(u'\xa0', ' ').strip()
    return cleaned_text

#############✅ Test 1
No = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[contains(text(),'1')])[2]"))
).text
No  = clean_text(No )
print("No:", No )

objective = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[contains(text(),'THIS IS SAMPLE OBJECTIVE ONLY')])[1]"))
).text
objective = clean_text(objective)
print("objective:", objective)

Action = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[contains(text(),'THIS ACTION PLANS IS SAMPLE ONLY')])[1]"))
).text
Action  = clean_text(Action )
print("Action:", Action )

wait.until(EC.element_to_be_clickable((By.XPATH, "(//td)[48]"))).click()

No_label = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@id='obj_seqnum'])[1]"))
).get_attribute("value")
No_label = clean_text(No_label)
print("No.:", No_label)

if No == No_label:
    print("✅ Test 1: Data match!")
else:
    print("❌ Test 1: Data do NOT match!")



objective_label = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//textarea[@id='obj_desc'])[1]"))
).get_attribute("value")
objective_label = clean_text(objective_label)
print("No.:", objective_label)

if objective == objective_label:
    print("✅ Test 2: Data match!")
else:
    print("❌ Test 2: Data do NOT match!")



Action_label = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//textarea[normalize-space()='THIS ACTION PLANS IS SAMPLE ONLY'])[1]"))
).text
Action_label = clean_text(Action_label)
print("Action:", Action_label)

if Action == Action_label:
    print("✅ Test 3: Data match!")
else:
    print("❌ Test 3: Data do NOT match!")

time.sleep(3)

# ✅ Close browser
driver.quit()
