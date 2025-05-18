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


driver.get("http://10.10.99.18:8002/audit")

import re

def clean_text(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = cleaned_text.replace(u'\xa0', ' ').strip()
    return cleaned_text

driver.get("http://10.10.99.18:8002/auditDetails/73")
time.sleep(1)
Auditee = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//td[contains(text(),'NHS')])[1]"))).text
Auditee = clean_text(Auditee)


driver.get("http://10.10.99.18:8002/auditeeDetails/76")
time.sleep(1)
Auditee_model = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "aue-no-with-agn-acronym"))).text
Auditee_model = clean_text(Auditee_model)
Auditee_model = Auditee_model.split()[-1]

print("Auditee:", Auditee)
print("Auditee:", Auditee_model)

if Auditee == Auditee_model:
    print("✅ Test 1: Data match!")
else:
    print("❌ Test 1: Data do NOT match!")

print("\n")

time.sleep(1)

# Get the details from the displayed page

Agency_Name = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//span[@class='agn-name'])[1]"))
).text
Name = clean_text(Agency_Name)

Agency_Head = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//span[@class='agn-head-position'])[1]"))
).text
Head = clean_text(Agency_Head)

Address = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//span[@class='agn-address'])[1]"))
).text
Address = clean_text(Address)

Contact_Details = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//span[@class='agn-contact-details'])[1]"))
).text
Contact_Details = clean_text(Contact_Details)


# Get the details from the modal

WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//i[@aria-label='Edit'])[1]"))).click()
time.sleep(1)

Agency_Name_label_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@id='agn_name'])[1]"))
).get_attribute("value")
Agency_Name_label_input = clean_text(Agency_Name_label_input)

Agency_Head_Name_label_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@id='agn_head_name'])[1]"))
).get_attribute("value")
Agency_Head_Name_label_input = clean_text(Agency_Head_Name_label_input)

Agency_Head_Position_label_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@id='agn_head_position'])[1]"))
).get_attribute("value")
Agency_Head_Position_label_input = clean_text(Agency_Head_Position_label_input)

Agency_Head_label_input = f"{Agency_Head_Name_label_input}, {Agency_Head_Position_label_input}"
Agency_Head_label_input = clean_text(Agency_Head_label_input)

Address_label_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//textarea[@id='agn_address'])[1]"))
).get_attribute("value")
Address_label_input = clean_text(Address_label_input)

Contact_Details_label_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//textarea[@id='agn_contact_details'])[1]"))
).get_attribute("value")
Contact_Details_label_input = clean_text(Contact_Details_label_input)


print("Agency Name:", Name)
print("Head of Agency:", Head)
print("Address:", Address)
print("Contact Details:", Contact_Details)

print("\n")

print("Agency Name:", Name)
print("Name:", Agency_Name_label_input)

if Name == Agency_Name_label_input:
    print("✅ Test 2: Data match!")
else:
    print("❌ Test 2: Data do NOT match!")

print("\n")

print("Head of Agency:", Head)
print("Head of Agency:", Agency_Head_label_input)

if Head == Agency_Head_label_input:
    print("✅ Test 3: Data match!")
else:
    print("❌ Test 3: Data do NOT match!")

print("\n")

print("Address:", Address)
print("Address:", Address_label_input)

if Address == Address_label_input:
    print("✅ Test 4: Data match!")
else:
    print("❌ Test 4: Data do NOT match!")

print("\n")

print("Contact Details:", Contact_Details)
print("Contact Details:", Contact_Details_label_input)

if Contact_Details == Contact_Details_label_input:
    print("✅ Test 5: Data match!")
else:
    print("❌ Test 5: Data do NOT match!")

print("\n")

WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(@aria-label,'Close')])[10]"))).click()
time.sleep(1)

WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//i[contains(@class,'fas fa-edit')])[2]"))).click()
time.sleep(1)

WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='clearAueBckgrnd'])[1]"))).click()
time.sleep(1)


background_input = "Test backgorund"
driver.find_element(By.XPATH,"//iframe[@id='aue_bckgrnd_ifr']").send_keys(background_input)

WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addAueBckgrnd'])[1]"))).click()
time.sleep(1)

try:
    Background_save_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Auditee Background updated successfully'])[1]")
    completion_message = Background_save_message_label.text.strip()

    if completion_message == "Auditee Background updated successfully":
        print("✅ Test 6: Background_save_message_label Passed")
    else:
        print(f"❌ Test 6 Failed: Text mismatch - Found '{completion_message}'")
except Exception as e:
    print(f"❌ Test  6 Failed: Background_save_message_label not found - {str(e)}")

WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]"))).click()

time.sleep(3)

# Close browser
driver.quit()
