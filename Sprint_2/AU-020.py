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


TARGET_URL = "http://10.10.99.18:8002/audit"
driver.get(TARGET_URL)

driver.execute_script("document.body.style.zoom='80%'")


import re

def clean_text(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = cleaned_text.replace(u'\xa0', ' ').strip()
    return cleaned_text

#############✅ Test 1
wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='Auditees'])[1]"))).click()


time.sleep(1)
Auditee = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[contains(text(),'FNRI')])[4]"))
).text
Auditee = clean_text(Auditee)
print("Auditee:", Auditee)


driver.get("http://10.10.99.18:8002/auditeeDetails/1")
time.sleep(2)
Auditee_model = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//span[normalize-space()='2025-01    FNRI'])[1]"))
).text
Auditee_model = clean_text(Auditee_model)
Auditee_model = Auditee_model.split()[-1]
print("Auditee :", Auditee_model)

if Auditee == Auditee_model:
    print("✅ Test 1: Data match!")
else:
    print("❌ Test 1: Data do NOT match!")

time.sleep(5)

# ✅ Close browser
driver.quit()
