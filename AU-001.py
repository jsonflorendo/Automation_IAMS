from LOGIN import AuditLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

login_bot = AuditLogin()

try:
    login_bot.login()
    login_bot.go_to_audit_page()

    wait = login_bot.wait
    driver = login_bot.driver

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

except Exception as e:
    pass

finally:
    login_bot.quit()
