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

Print_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@aria-label='Print'])[1]")))
Print_button.click()
time.sleep(1)

driver.find_element(By.XPATH, "(//a[normalize-space()='Special Order'])[1]").click()
time.sleep(1)

communication_save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addOrUpdateEmailTemplate'])[1]")))
communication_save_button.click()
time.sleep(1)


try:
    communication_Subject_message_label = driver.find_element(By.XPATH, "(//span[@id='error-tpl_name'])[1]")
    assert communication_Subject_message_label.text.strip() == "This field is required.", "Incorrect spelling"
    print("✅Test case 1 : Required communication_Subject_label Passed")
except NoSuchElementException:
    print("❌Test Case 1 Failed: Required communication_Subject_label")
except AssertionError as e:
    print(f"❌Test Case 1 Failed: {e}")

try:
    communication_Content_message_label = driver.find_element(By.XPATH, "(//span[@id='error-tpl_content'])[1]")
    assert communication_Content_message_label.text.strip() == "This field is required.", "Incorrect spelling"
    print("✅Test case 2 : Required communication_Content_label Passed")
except NoSuchElementException:
    print("❌Test Case 2 Failed: Required communication_Content_label")
except AssertionError as e:
    print(f"❌Test Case 2 Failed: {e}")

wait.until(EC.element_to_be_clickable((By.XPATH, "(//b[@role='presentation'])[1]"))).click()
time.sleep(1)
recipient_box= wait.until(EC.presence_of_element_located((By.XPATH, "//input[@role='searchbox']")))
recipient_box .send_keys("bnjmntumbaga@gmail.com")
time.sleep(1)
recipient_box.send_keys(Keys.ENTER)

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
    communication_success_save_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Email template updated successfully'])[1]")
    assert communication_success_save_message_label.text.strip() == "Email template updated successfully", "Incorrect spelling"
    print("✅Test case 3 : communication_success_save_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 3 Failed: communication_success_save_message_label")
except AssertionError as e:
    print(f"❌Test Case 3 Failed: {e}")

time.sleep(1)
driver.find_element(By.XPATH, "(//button[normalize-space()='OK'])[1]").click()
time.sleep(1)

communication_delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='deleteEmailTemplate'])[1]")))
communication_delete_button.click()
time.sleep(1)

try:
    attachment_success_delete_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Are you sure you want to delete this item?'])[1]")
    assert attachment_success_delete_message_label.text.strip() == "Are you sure you want to delete this item?", "Incorrect spelling"
    print("✅Test case 4 : attachment_success_delete_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 4 Failed: attachment_success_delete_message_label")
except AssertionError as e:
    print(f"❌Test Case 4 Failed: {e}")

time.sleep(1)
communication_delete_ok_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='swal2-actions']//button[normalize-space()='OK' or normalize-space()='Ok']"))
)
communication_delete_ok_button.click()
time.sleep(1)
try:
    communication_success_delete_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Email template deleted successfully'])[1]")
    assert communication_success_delete_message_label.text.strip() == "Email template deleted successfully", "Incorrect spelling"
    print("✅Test case 5 : communication_success_delete_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 5 Failed: communication_success_delete_message_label")
except AssertionError as e:
    print(f"❌Test Case 5 Failed: {e}")

time.sleep(1)
communication_success_ok_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='swal2-actions']//button[normalize-space()='OK' or normalize-space()='Ok']"))
)
communication_success_ok_button.click()
time.sleep(1)

communication_close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Close'])[16]")))
communication_close_button.click()


time.sleep(5)

# ✅ Close browser
driver.quit()
