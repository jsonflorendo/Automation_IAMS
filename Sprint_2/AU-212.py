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
time.sleep(1)

Documents_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@aria-label='Documents'])[1]")))
Documents_button.click()
time.sleep(1)

type_Documents_input = wait.until(EC.element_to_be_clickable((By.XPATH, "(//select[@id='fle_doc_typ_id'])[1]")))
type_Documents_input.click()
time.sleep(1)
driver.find_element(By.XPATH, "(//option[@value='13'][normalize-space()='Audit Report'])[2]").click()

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
    document_save_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Documentary requirement added successfully'])[1]")
    assert document_save_message_label.text.strip() == "Documentary requirement added successfully", "Incorrect spelling"
    print("✅test case 1 : document_save_message_label Passed")
except NoSuchElementException:
    print("❌Test Case 1 Failed: document_save_message_label")
except AssertionError as e:
    print(f"❌Test Case 1 Failed: {e}")
time.sleep(1)
driver.find_element(By.XPATH, "(//button[normalize-space()='OK'])[1]").click()

time.sleep(1)

Documents_table = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody//tr//td[2]")))
Documents_table.click()
time.sleep(1)

Documents_delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-times'])[3]")))
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
    document_success_delete_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Documentary requirement deleted successfully'])[1]")
    assert document_success_delete_message_label.text.strip() == "Documentary requirement deleted successfully", "Incorrect spelling"
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

Documents_close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Close'])[9]")))
Documents_close_button.click()

time.sleep(5)


# ✅ Close browser
driver.quit()
