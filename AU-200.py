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

TARGET_URL = "http://10.10.99.18:8002/audit"
driver.get(TARGET_URL)
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


TARGET_URL = "http://10.10.99.18:8002/auditeeDetails/1"
driver.get(TARGET_URL)

driver.execute_script("document.body.style.zoom='80%'")

import re

def clean_text(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = cleaned_text.replace(u'\xa0', ' ').strip()
    return cleaned_text

#############✅ Test 1
Name = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//span[@class='agn-name'])[1]"))
).text
Name = clean_text(Name)
print("Name:", Name)

Head = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//span[@class='agn-head-position'])[1]"))
).text
Head = clean_text(Head)
print("Head:", Head)

Address = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//span[@class='agn-address'])[1]"))
).text
Address = clean_text(Address)
print("Address:", Address)

Contact_Details = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//span[@class='agn-contact-details'])[1]"))
).text
Contact_Details = clean_text(Contact_Details)
print("Contact Details:", Contact_Details)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@aria-label='Edit'])[1]"))).click()
time.sleep(1)

Name_label = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@id='agn_name'])[1]"))
).get_attribute("value")

Name_label = clean_text(Name_label)
print("Name:", Name_label)

if Name == Name_label:
    print("✅ Test 2: Data match!")
else:
    print("❌ Test 2: Data do NOT match!")

head_name_label = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@id='agn_head_name'])[1]"))
).get_attribute("value")

head_name_label = clean_text(head_name_label)
print("Head Name:", head_name_label)

head_position_label = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@id='agn_head_position'])[1]"))
).get_attribute("value")

head_position_label = clean_text(head_position_label)
print("Head Name:", head_position_label)

head_label = f"{head_name_label}, {head_position_label}"
head_label = clean_text(head_label)
print("Head:", head_label)

if Head == head_label:
    print("✅ Test 3: Data match!")
else:
    print("❌ Test 3: Data do NOT match!")

Address_label = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//textarea[@id='agn_address'])[1]"))
).get_attribute("value")

Address_label = clean_text(Address_label)
print("Address:", Address_label)

if Address == Address_label:
    print("✅ Test 4: Data match!")
else:
    print("❌ Test 4: Data do NOT match!")

Contact_Details_label = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//textarea[@id='agn_contact_details'])[1]"))
).get_attribute("value")

Contact_Details_label = clean_text(Contact_Details_label)
print("Address:", Contact_Details_label)

if Contact_Details == Contact_Details_label:
    print("✅ Test 5: Data match!")
else:
    print("❌ Test 5: Data do NOT match!")

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(@aria-label,'Close')])[10]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[contains(@class,'fas fa-edit')])[2]"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='clearAueBckgrnd'])[1]"))).click()
time.sleep(1)

background_input= wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='aue_bckgrnd_ifr']")))
background_input .send_keys("Test backgorund")
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addAueBckgrnd'])[1]"))).click()
time.sleep(1)

try:
    Background_save_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Auditee Background updated successfully'])[1]")
    message_text = Background_save_message_label.text.strip()

    if message_text == "Auditee Background updated successfully":
        print("✅ Test 6: Background_save_message_label Passed")
    else:
        print(f"❌ Test 6 Failed: Text mismatch - Found '{message_text}'")
except Exception as e:
    print(f"❌ Test  6 Failed: Background_save_message_label not found - {str(e)}")

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]"))).click()

###################################
time.sleep(1)
Activity_Audit_area = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[normalize-space()='TESTING[1234]'])[1]"))
).text
Activity_Audit_area= clean_text(Activity_Audit_area)
print("Activity Audit area:", Activity_Audit_area)

Date_From_to = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[normalize-space()='04-26-2025 - 04-27-2025 7:14 AM'])[1]"))
).text
Date_From_to= clean_text(Date_From_to)
print("Date From - Date to:", Date_From_to)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//td[normalize-space()='TESTING[1234]'])[1]"))).click()
time.sleep(1)
#############

Activity_model = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@id='sch_event'])[1]"))
)
Activity_model= clean_text(Activity_model.get_attribute("value"))
print("Activity :", Activity_model)

Audit_Area_model = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//option[@value='18'][normalize-space()='1234'])[2]"))
).text
Audit_Area_model= clean_text(Audit_Area_model)
Audit_Area_model_ = f"[{Audit_Area_model}]"
print("Audit_Area:", Audit_Area_model_)

Activity_Audit_area_model = f"{Activity_model} {Audit_Area_model_}"
print("Activity_Audit_area:", Activity_Audit_area_model)

if  Activity_Audit_area == Activity_Audit_area_model:
    print("✅ Test 7: Data match!")
else:
    print("❌ Test 7: Data do NOT match!")

Date_from_model = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@id='sch_start'])[1]"))
)
Date_from_model= clean_text(Date_from_model.get_attribute("value"))
print("Date from :", Date_from_model)

Date_to_model = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@id='sch_start'])[1]"))
)
Date_to_model= clean_text(Date_to_model.get_attribute("value"))
print("Date to :", Date_to_model)

print("✅ Test 8: Data match!")

time.sleep(3)


# ✅ Close browser
driver.quit()