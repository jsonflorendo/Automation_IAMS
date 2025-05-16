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

wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='icq_ara_id']"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "(//option[@class='fw-bold'][normalize-space()='Financial'])[1]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@onclick='addSchedOfActivity()'])[1]"))).click()
time.sleep(1)

activity_input= wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='sch_event'])[1]")))
activity_input .send_keys("Test activity")
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='sch_end'])[1]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='29'])[1]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Done'])[1]"))).click()
time.sleep(1)

venue_input= wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='sch_venue'])[1]")))
venue_input .send_keys("Test Venue")
time.sleep(1)

remarks_input= wait.until(EC.presence_of_element_located((By.XPATH, "(//textarea[@id='sch_remarks'])[1]")))
remarks_input .send_keys("Test Remark")
time.sleep(1)

attendees_input = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@role='combobox'])[2]")))
attendees_input.click()
time.sleep(1)
driver.find_element(By.XPATH, "(//option[@value='14'][normalize-space()='Amar, Omaira Mabang'])[1]").click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addSchedule'])[1]"))).click()
time.sleep(1)
try:
    save_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Schedule of activity added successfully'])[1]")
    assert save_message_label.text.strip() == "Schedule of activity added successfully", "Incorrect spelling"
    print("✅test case 1 : save_message_label Passed")
except NoSuchElementException:
    print("❌ Test Case 1 Failed: save_message_label")
except AssertionError as e:
    print(f"❌ Test Case 1 Failed: {e}")

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]"))).click()
time.sleep(1)
###########################

wait.until(EC.element_to_be_clickable((By.XPATH, "(//tbody)[1]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='updateSchedule'])[1]"))).click()
time.sleep(1)



try:
    update_save_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Schedule of activity updated successfully'])[1]")
    assert update_save_message_label.text.strip() == "Schedule of activity updated successfully", "Incorrect spelling"
    print("✅test case 2 : update_save_message_label Passed")
except NoSuchElementException:
    print("❌ Test Case 2 Failed: update_save_message_label")
except AssertionError as e:
    print(f"❌ Test Case 2 Failed: {e}")

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//tbody)[1]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Delete'])[1]"))).click()
time.sleep(1)

try:
    delete_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Are you sure you want to delete this item?'])[1]")
    assert delete_message_label.text.strip() == "Are you sure you want to delete this item?", "Incorrect spelling"
    print("✅test case 3 : delete_message_label Passed")
except NoSuchElementException:
    print("❌ Test Case 3 Failed: delete_message_label")
except AssertionError as e:
    print(f"❌ Test Case 3 Failed: {e}")

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Ok'])[1]"))).click()
time.sleep(1)

try:
    delete_success_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Schedule of activity deleted successfully'])[1]")
    assert delete_success_message_label.text.strip() == "Schedule of activity deleted successfully", "Incorrect spelling"
    print("✅test case 4 : delete_success_message_label Passed")
except NoSuchElementException:
    print("❌ Test Case 4 Failed: delete_success_message_label")
except AssertionError as e:
    print(f"❌ Test Case 4 Failed: {e}")

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]"))).click()

time.sleep(5)

driver.quit()
