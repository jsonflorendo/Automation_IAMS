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

import re

def clean_text(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = cleaned_text.replace(u'\xa0', ' ').strip()
    return cleaned_text

#############✅ Test 1
iframe = wait.until(EC.presence_of_element_located((By.ID, "aud_rationale_ifr")))
driver.switch_to.frame(iframe)
editable_body = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))
editable_body.clear()
driver.switch_to.default_content()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-chevron-right fa-2x'])[1]"))).click()
time.sleep(1)


try:
    Rationale_message_label = driver.find_element(By.XPATH, "//body/div[@id='wrapper']/div[@id='content-wrapper']/div[@id='content']/div[@class='container-fluid']/div[@class='row']/div[@class='col-md-12 mb-5']/div/div[@id='auditPlanCarousel']/div[@class='carousel-inner']/div[@class='carousel-item active']/section[@id='section1']/div[@class='row']/div[1]")
    message_text = Rationale_message_label.text.strip()

    if message_text == "This field is required.":
        print("✅ Test Case 1: Rationale_message_label Passed")
    else:
        print(f"❌ Test Case 1 Failed: Text mismatch - Found '{message_text}'")
except Exception as e:
    print(f"❌ Test Case 1 Failed: Rationale_message_label not found - This field is required.")


#############
wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-chevron-left fa-2x '])[1]"))).click()
time.sleep(1)


time.sleep(1)
iframe = wait.until(EC.presence_of_element_located((By.ID, "aud_rationale_ifr")))
driver.switch_to.frame(iframe)

editable_body = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))

editable_body.clear()
editable_body.send_keys("Test input for Audit Timeline.")

driver.switch_to.default_content()


time.sleep(3)

# ✅ Close browser
driver.quit()
