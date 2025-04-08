from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://10.10.99.18:8002/login")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password = driver.find_element(By.NAME, "password")
    username.send_keys("Superadmin@gmail.com")
    password.send_keys("Dost@123")
    password.send_keys(Keys.RETURN)

    wait.until(EC.url_contains("/dashboard"))

    driver.get("http://10.10.99.18:8002/audit")

    cell = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#DataTables_Table_1 > tbody > tr:nth-child(3) > td:nth-child(5)")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cell)
    time.sleep(0.5)

    try:
        cell.click()
    except:
        driver.execute_script("arguments[0].click();", cell)

    button = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR,
        "#content > div.container-fluid > div.row > div.col-md-12.mb-5 > div.d-flex.justify-content-between.mb-2 > div.float-end.mr-3 > button"
    )))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    time.sleep(0.5)
    try:
        button.click()
    except:
        driver.execute_script("arguments[0].click();", button)

    aue_agn_id_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#aue_agn_id")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", aue_agn_id_element)
    time.sleep(0.5)
    aue_agn_id_element.click()
    aue_agn_id_element.send_keys("New value for aue_agn_id")

    aur_id_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#aue_aur_id")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", aur_id_element)
    time.sleep(0.5)
    aur_id_element.send_keys("Some value here")

    aue_remarks_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#aue_remarks")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", aue_remarks_element)
    time.sleep(0.5)
    aue_remarks_element.clear()
    aue_remarks_element.send_keys("THIS IS SAMPLE REMARKS ONLY")

    add_auditee_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#addAuditee")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_auditee_button)
    time.sleep(0.5)
    try:
        add_auditee_button.click()
    except:
        driver.execute_script("arguments[0].click();", add_auditee_button)

    time.sleep(3)

finally:
    driver.quit()
