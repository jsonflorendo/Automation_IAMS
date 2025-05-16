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

driver.execute_script("document.body.style.zoom='70%'")

wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='icq_ara_id']"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "(//option[@class='fw-bold'][normalize-space()='Financial'])[1]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//td)[3]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-minus'])[1]"))).click()
time.sleep(1)


try:
    delete_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Are you sure you want to delete this item?'])[1]")
    assert delete_message_label.text.strip() == "Are you sure you want to delete this item?", "Incorrect spelling"
    print("✅Test Case 1: delete_message_label Passed")
except NoSuchElementException:
    print("❌ Test Case 1 Failed: delete_message_label not found")
except AssertionError as e:
    print(f"❌ Test Case 1 Failed: {e}")

time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Ok'])[1]"))).click()
time.sleep(1)

try:
    delete_success_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Audit question deleted successfully'])[1]")
    assert delete_success_message_label.text.strip() == "Audit question deleted successfully", "Incorrect spelling"
    print("✅Test Case 2: delete_success_message_label Passed")
except NoSuchElementException:
    print("❌ Test Case 2 Failed: delete_success_message_label not found")
except AssertionError as e:
    print(f"❌ Test Case 2 Failed: {e}")

time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]"))).click()
time.sleep(1)


wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='updateIcqParticulars'])[1]"))).click()
time.sleep(1)
try:
    save_success_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Internal control questionnaire added successfully'])[1]")
    assert save_success_message_label.text.strip() == "Internal control questionnaire added successfully", "Incorrect spelling"
    print("✅Test Case 3: save_success_message_label Passed")
except NoSuchElementException:
    print("❌ Test Case 3 Failed: save_success_message_label not found")
except AssertionError as e:
    print(f"❌ Test Case 3 Failed: {e}")

time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//td)[3]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@aria-label='Reference'])[3]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@id='addIcqReference'])[3]"))).click()
time.sleep(1)

reference_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='ref_no'])[1]")))
reference_input.send_keys("Test11")
time.sleep(1)
title_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='ref_title'])[1]")))
title_input.send_keys("Test11")
time.sleep(1)
dis_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//textarea[@id='ref_desc'])[1]")))
dis_input.send_keys("Test")
time.sleep(1)
source_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='ref_source'])[1]")))
source_input.send_keys("Test")
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//select[@id='ref_typ_id'])[1]"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "(//option[@value='13'][normalize-space()='Audit Report'])[1]"))).click()
time.sleep(1)
keyword_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='ref_metadata'])[1]")))
keyword_input.send_keys("Test")
time.sleep(1)
url_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='ref_url'])[1]")))
url_input.send_keys("https://www.google.com")
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addReference'])[1]"))).click()
time.sleep(1)

try:
    save_reference_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Reference added successfully'])[1]")
    assert save_reference_message_label.text.strip() == "Reference added successfully", "Incorrect spelling"
    print("✅Test Case 4: save_reference_message_label Passed")
except NoSuchElementException:
    print("❌ Test Case 4 Failed: save_reference_message_label not found")
except AssertionError as e:
    print(f"❌ Test Case 4 Failed: {e}")
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]"))).click()
time.sleep(1)

time.sleep(5)

driver.quit()
