from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("http://10.10.99.18:8002/login")
driver.maximize_window()

wait = WebDriverWait(driver, 20)

try:
    username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password = driver.find_element(By.NAME, "password")

    username.clear()
    username.send_keys("Superadmin@gmail.com")

    password.clear()
    password.send_keys("Dost@123")
    password.send_keys(Keys.RETURN)

    wait.until(EC.url_contains("/dashboard"))

    driver.get("http://10.10.99.18:8002/audit")

    target_cell = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, "#DataTables_Table_1 > tbody > tr:nth-child(3) > td:nth-child(2)"
    )))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_cell)
    time.sleep(0.5)
    try:
        target_cell.click()
    except:
        driver.execute_script("arguments[0].click();", target_cell)

    icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
        "#auditDetailsDiv1 > div > div.col-md-1.text-center > div:nth-child(3) > a > i"
    )))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", icon)
    time.sleep(0.5)
    try:
        icon.click()
    except:
        driver.execute_script("arguments[0].click();", icon)

    dropdown_element = wait.until(EC.visibility_of_element_located((By.ID, "fle_doc_typ_id")))
    driver.execute_script("arguments[0].scrollIntoView();", dropdown_element)
    select = Select(dropdown_element)

    if len(select.options) > 1:
        select.select_by_index(1)
    else:
        driver.quit()
        exit()
    time.sleep(1)

    fle_desc = wait.until(EC.presence_of_element_located((By.ID, "fle_desc")))
    driver.execute_script("arguments[0].scrollIntoView();", fle_desc)
    fle_desc.clear()
    fle_desc.send_keys("SAMPLE")
    time.sleep(1)

    attach_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        "#document-attachment-form > div > div.col-md-8 > div > button > i"
    )))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", attach_button)
    time.sleep(0.5)
    try:
        attach_button.click()
    except:
        driver.execute_script("arguments[0].click();", attach_button)
    time.sleep(2)

    file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
    file_input.send_keys(r"C:\Users\Acer\OneDrive\2016-Succession-Q-A_092046.pdf")
    time.sleep(3)

finally:
    driver.quit()

