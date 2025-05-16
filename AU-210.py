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
username_input.send_keys("superadmin@gmail.com")

password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
password_input.send_keys("Dost@123")

login_button = wait.until(EC.element_to_be_clickable((By.ID, "login")))
login_button.click()

time.sleep(3)
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[-1])


TARGET_URL = "http://10.10.99.18:8002/auditeeDetails/76"
driver.get(TARGET_URL)
driver.execute_script("document.body.style.zoom='80%'")


import re

def clean_text(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = cleaned_text.replace(u'\xa0', ' ').strip()
    return cleaned_text

#############✅ Test 1
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='IC Questionnaire'])[1]"))).click()
time.sleep(1)

driver.execute_script("document.body.style.zoom='80%'")

wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='icq_ara_id']"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "(//option[@data-original-name='Lorem Ipsum'])[1]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='icq_approve_btn'])[1]"))).click()
time.sleep(1)

try:
    approve_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Are you sure you want to approved this ICQ?'])[1]")
    message_text = approve_message_label.text.strip()

    if message_text == "Are you sure you want to approved this ICQ?":
        print("✅ Test Case 1: approve_message_label Passed")
    else:
        print(f"❌ Test Case 1 Failed: Text mismatch - Found '{message_text}'")
except Exception as e:
    print(f"❌ Test Case 1 Failed: approve_message_label not found - {str(e)}")

time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Ok'])[1]"))).click()
time.sleep(1)

try:
    ICQ_approve_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='ICQ approved successfully'])[1]")
    message_text = ICQ_approve_message_label.text.strip()

    if message_text == "ICQ approved successfully":
        print("✅ Test Case 2: ICQ_approve_message_label Passed")
    else:
        print(f"❌ Test Case 2 Failed: Text mismatch - Found '{message_text}'")
except Exception as e:
    print(f"❌ Test Case 2 Failed: ICQ_approve_message_label not found - {str(e)}")
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]"))).click()
time.sleep(1)


time.sleep(5)

driver.quit()
