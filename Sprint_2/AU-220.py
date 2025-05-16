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

driver.execute_script("document.body.style.zoom='80%'")

wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='icq_ara_id']"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "(//option[@class='fw-bold'][normalize-space()='Financial'])[1]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@aria-label='Print'])[1]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='ICQ (Questions only)'])[1]"))).click()
time.sleep(1)

print(" Test 1: No message ")

time.sleep(3)

# ✅ Close browser
driver.quit()
