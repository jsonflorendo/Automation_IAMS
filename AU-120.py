from LOGIN import AuditLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

login_bot = AuditLogin()

try:
    login_bot.login()
    login_bot.go_to_audit_page()

    driver = login_bot.driver
    wait = login_bot.wait

    target_cell = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#DataTables_Table_1 > tbody > tr:nth-child(2) > td:nth-child(2)")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_cell)
    target_cell.click()

    audit_plan_select_element = wait.until(
        EC.presence_of_element_located((By.ID, "auditPlanSelect"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", audit_plan_select_element)

    select = Select(audit_plan_select_element)
    select.select_by_visible_text("VI. Audit Criteria")
    time.sleep(1)

    section6_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#section6 > div.mb-3 > div > div.col-auto > button"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", section6_button)
    section6_button.click()

    time.sleep(1)

    audit_area_criteria_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#auditAreaCriteriaForm > div.mt-3 > button > i"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", audit_area_criteria_button)
    audit_area_criteria_button.click()

    time.sleep(1)

    criteria_name_input = wait.until(
        EC.element_to_be_clickable((By.ID, "cra_name"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", criteria_name_input)
    criteria_name_input.clear()
    criteria_name_input.send_keys("THIS IS SAMPLES CRITERIA NAME")

    select_element_span = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#audit-criteria-form > div:nth-child(4) > div.input-group > span > span.selection > span"))
    )
    select_element_span.click()

    time.sleep(2)

    select_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//li[text()='ABC-00-12345']"))
    )
    select_option.click()

    add_audit_criteria_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#addAuditCriteria"))
    )
    add_audit_criteria_button.click()

    time.sleep(2)

    close_modal_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#AuditCriteriaModal > div > div > div.modal-header > button"))
    )
    driver.execute_script("arguments[0].click();", close_modal_button)

    time.sleep(2)

    close_audit_area_criteria_modal_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#AuditAreaCriteriaModal > div > div > div.modal-header > button"))
    )
    driver.execute_script("arguments[0].click();", close_audit_area_criteria_modal_button)

    time.sleep(2)

    target_cell_table_2 = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#DataTables_Table_2 > tbody > tr:nth-child(1) > td:nth-child(2) > div")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_cell_table_2)
    target_cell_table_2.click()

    time.sleep(2)

    third_link_element = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#DataTables_Table_2 > tbody > tr:nth-child(1) > td:nth-child(2) > div > div > a:nth-child(3)")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", third_link_element)
    third_link_element.click()

    time.sleep(5)

finally:
    login_bot.quit()
