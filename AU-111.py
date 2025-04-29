from LOGIN import AuditLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

login_bot = AuditLogin()

try:
    login_bot.login()
    login_bot.go_to_audit_page()

    wait = login_bot.wait
    driver = login_bot.driver

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

    add_action_plan_button = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, "button.btn.btn-primary.btn-sm.add-action-plan-button"
    )))
    try:
        add_action_plan_button.click()
    except Exception:
        driver.execute_script("arguments[0].click();", add_action_plan_button)

    new_action_plan_textarea = wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "#actionPlansEntry > div.row.align-items-center.mb-3.entry-field.add-entry > div.col-md-9 > textarea"
    )))
    driver.execute_script("arguments[0].value = arguments[1];", new_action_plan_textarea, "THIS IS SAMPLE ACTION ONLY")

    time.sleep(2)

    add_audit_objective_button = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, "#addAuditObjective"
    )))
    driver.execute_script("arguments[0].click();", add_audit_objective_button)

    time.sleep(2)

finally:
    login_bot.quit()
