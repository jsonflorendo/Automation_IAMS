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
    except Exception:
        driver.execute_script("arguments[0].click();", target_cell)

    dropdown_element = wait.until(EC.presence_of_element_located((By.ID, "auditPlanSelect")))
    select = Select(dropdown_element)
    select.select_by_visible_text("III. Audit Objectives")

    time.sleep(1)

    button_icon = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, "#section3 > div.mb-3 > div > div.col-auto > button > i"
    )))
    try:
        button_icon.click()
    except Exception:
        driver.execute_script("arguments[0].click();", button_icon)

    time.sleep(1)

    obj_seqnum_input = wait.until(EC.presence_of_element_located((By.ID, "obj_seqnum")))
    obj_seqnum_input.clear()
    obj_seqnum_input.send_keys("1")

    obj_desc_textarea = wait.until(EC.presence_of_element_located((By.ID, "obj_desc")))
    obj_desc_textarea.clear()
    obj_desc_textarea.send_keys("THIS IS SAMPLE OBJECTIVE ONLY")

    action_plans_textarea = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, "#actionPlansEntry > div > div.col-md-9 > textarea"
    )))
    action_plans_textarea.clear()
    action_plans_textarea.send_keys("THIS ACTION PLANS IS SAMPLE ONLY")

    time.sleep(2)

    add_audit_objective_button = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, "#addAuditObjective"
    )))
    try:
        add_audit_objective_button.click()
    except Exception:
        driver.execute_script("arguments[0].click();", add_audit_objective_button)

    time.sleep(2)

except Exception as e:
    pass

finally:
    driver.quit()
