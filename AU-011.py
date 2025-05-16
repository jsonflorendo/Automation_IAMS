import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time
from selenium.webdriver.common.keys import Keys
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

Documents_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@aria-label='Documents'])[1]")))
Documents_button.click()
time.sleep(1)

type_Documents_input = wait.until(EC.element_to_be_clickable((By.XPATH, "(//select[@id='fle_doc_typ_id'])[1]")))
type_Documents_input.click()
time.sleep(1)
driver.find_element(By.XPATH, "(//option[@value='3'][normalize-space()='Memorandum Circular'])[1]").click()

time.sleep(1)
Name_document_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='fle_desc'])[1]")))
Name_document_input.send_keys("Name Test")

time.sleep(1)
file_input = wait.until(EC.presence_of_element_located((By.ID, "fle_name")))
driver.execute_script("arguments[0].style.display = 'block';", file_input)
document_path = r"C:\Users\KalingaInnovationHub\Downloads\Curriculum Vitae.pdf"
file_input.send_keys(document_path)

time.sleep(1)
try:
    document_save_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Document attachment added successfully'])[1]")
    assert document_save_message_label.text.strip() == "Document attachment added successfully", "Incorrect spelling"
    print("✅test case 1 : document_save_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 1 Failed: document_save_message_label")
except AssertionError as e:
    print(f"❌Test Case 1 Failed: {e}")
time.sleep(1)
driver.find_element(By.XPATH, "(//button[normalize-space()='OK'])[1]").click()

time.sleep(1)

Documents_table = wait.until(EC.element_to_be_clickable((By.XPATH, "(//tbody)[65]")))
Documents_table.click()
time.sleep(1)

Documents_delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[contains(@class,'fas fa-times')])[2]")))
Documents_delete_button.click()
time.sleep(1)

try:
    document_delete_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Are you sure you want to delete this item?'])[1]")
    assert document_delete_message_label.text.strip() == "Are you sure you want to delete this item?", "Incorrect spelling"
    print("✅test case 2 : document_delete_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 2 Failed: document_delete_message_label")
except AssertionError as e:
    print(f"❌Test Case 2 Failed: {e}")

time.sleep(1)
document_delete_ok_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='swal2-actions']//button[normalize-space()='OK' or normalize-space()='Ok']"))
)
document_delete_ok_button.click()
time.sleep(1)
try:
    document_success_delete_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Document attachment deleted successfully'])[1]")
    assert document_success_delete_message_label.text.strip() == "Document attachment deleted successfully", "Incorrect spelling"
    print("✅test case 3 : document_success_delete_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 3 Failed: document_success_delete_message_label")
except AssertionError as e:
    print(f"❌Test Case 3 Failed: {e}")

time.sleep(1)
document_ok_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='swal2-actions']//button[normalize-space()='OK' or normalize-space()='Ok']"))
)
document_ok_button.click()
time.sleep(1)

Documents_close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(@aria-label,'Close')])[7]")))
Documents_close_button.click()
time.sleep(1)

#################################### email notification

Print_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@aria-label='Print'])[1]")))
Print_button.click()
time.sleep(1)

driver.find_element(By.XPATH, "(//a[normalize-space()='Amendment to SO'])[1]").click()
time.sleep(1)

email_save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addOrUpdateEmailTemplate'])[1]")))
email_save_button.click()
time.sleep(1)

#emai_send_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Send'])[1]")))
#emai_send_button.click()
#time.sleep(1)

#try:
#    email_Recipient_message_label = driver.find_element(By.XPATH, "(//span[@id='error-aue_email_recipient'])[1]")
#    assert email_Recipient_message_label.text.strip() == "This field is required.", "Incorrect spelling"
#    print("✅Test case 4 : Required Recipient_message_label Passed")
#except NoSuchElementException:
#    print("❌Test Case 4 Failed: Required Recipient_message_label")
#except AssertionError as e:
#   print(f"❌Test Case 4 Failed: {e}")

try:
    email_Subject_message_label = driver.find_element(By.XPATH, "(//span[@id='error-tpl_name'])[1]")
    assert email_Subject_message_label.text.strip() == "This field is required.", "Incorrect spelling"
    print("✅Test case 4 : Required Recipient_Subject_label Passed")
except NoSuchElementException:
    print("❌Test Case 4 Failed: Required Recipient_Subject_label")
except AssertionError as e:
    print(f"❌Test Case 4 Failed: {e}")

try:
    email_Content_message_label = driver.find_element(By.XPATH, "(//span[@id='error-tpl_content'])[1]")
    assert email_Content_message_label.text.strip() == "This field is required.", "Incorrect spelling"
    print("✅Test case 5 : Required Recipient_Content_label Passed")
except NoSuchElementException:
    print("❌Test Case 5 Failed: Required Recipient_Content_label")
except AssertionError as e:
    print(f"❌Test Case 5 Failed: {e}")

recipient_box= wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@role='combobox'])[4]")))
recipient_box .send_keys("bnjmntumbaga@gmail.com")
time.sleep(1)
recipient_box.send_keys(Keys.ENTER)

wait.until(EC.element_to_be_clickable((By.XPATH, "//b[@role='presentation']"))).click()
time.sleep(1)
Subject_box= wait.until(EC.presence_of_element_located((By.XPATH, "//input[@role='searchbox']")))
Subject_box .send_keys("test")
time.sleep(1)
Subject_box.send_keys(Keys.ENTER)

time.sleep(1)
background_input= wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='tpl_content_ifr']")))
background_input .send_keys("Test")
time.sleep(1)


driver.find_element(By.ID, "addTplAttachment").click()
time.sleep(2)
pyautogui.write(r"C:\Users\KalingaInnovationHub\Downloads\Curriculum Vitae.pdf")
pyautogui.press("enter")


time.sleep(2)

email_save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addOrUpdateEmailTemplate'])[1]")))
email_save_button.click()
time.sleep(1)

try:
    email_success_save_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Email template updated successfully'])[1]")
    assert email_success_save_message_label.text.strip() == "Email template updated successfully", "Incorrect spelling"
    print("✅Test case 6 : email_success_save_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 6 Failed: email_success_save_message_label")
except AssertionError as e:
    print(f"❌Test Case 6 Failed: {e}")

time.sleep(1)
driver.find_element(By.XPATH, "(//button[normalize-space()='OK'])[1]").click()
time.sleep(1)


wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='fas fa-times']"))).click()
time.sleep(1)
try:
    Attach_delete_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Are you sure you want to delete this item?'])[1]")
    message_text = Attach_delete_message_label.text.strip()

    if message_text == "Are you sure you want to delete this item?":
        print("✅Test Case 7: Attach_delete_message_label Passed")
    else:
        print(f"❌ Test Case 7 Failed: Text mismatch - Found '{message_text}'")
except Exception as e:
    print(f"❌ Test Case 7 Failed: Attach_delete_message_label not found - {str(e)}")

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Ok']"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='sendEmailTemplate']"))).click()
time.sleep(10)

try:
    Email_Notification_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Email notification sent successfully'])[1]")
    message_text = Email_Notification_message_label.text.strip()

    if message_text == "Email notification sent successfully":
        print("✅Test Case 8: Email_Notification_message_label Passed")
    else:
        print(f"❌ Test Case 8 Failed: Text mismatch - Found '{message_text}'")
except Exception as e:
    print(f"❌ Test Case 8 Failed: Email_Notification_message_label not found - {str(e)}")


driver.find_element(By.XPATH, "(//button[normalize-space()='OK'])[1]").click()
time.sleep(1)

email_delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='deleteEmailTemplate'])[1]")))
email_delete_button.click()
time.sleep(1)

try:
    email_delete_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Are you sure you want to delete this item?'])[1]")
    assert email_delete_message_label.text.strip() == "Are you sure you want to delete this item?", "Incorrect spelling"
    print("✅Test case 9 : email_delete_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 9 Failed: email_delete_message_label")
except AssertionError as e:
    print(f"❌Test Case 9 Failed: {e}")

time.sleep(1)
email_delete_ok_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='swal2-actions']//button[normalize-space()='OK' or normalize-space()='Ok']"))
)
email_delete_ok_button.click()
time.sleep(1)
try:
    email_success_delete_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Email template deleted successfully'])[1]")
    assert  email_success_delete_message_label.text.strip() == "Email template deleted successfully", "Incorrect spelling"
    print("✅Test case 10 : email_success_delete_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 10 Failed: email_success_delete_message_label")
except AssertionError as e:
    print(f"❌Test Case 10 Failed: {e}")

time.sleep(1)
email_success_ok_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='swal2-actions']//button[normalize-space()='OK' or normalize-space()='Ok']"))
)
email_success_ok_button.click()
time.sleep(1)

email_close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Close'])[16]")))
email_close_button.click()

time.sleep(3)


# ✅ Close browser
driver.quit()
