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

    time.sleep(2)

    audit_cell = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[text()='Annual Compliance Audit']")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", audit_cell)
    wait.until(EC.visibility_of(audit_cell))
    driver.execute_script("arguments[0].click();", audit_cell)

    time.sleep(2)

    select_element = wait.until(EC.presence_of_element_located((By.ID, "auditPlanSelect")))
    select = Select(select_element)
    select.select_by_visible_text("I. Rationale")

    time.sleep(2)

    iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(iframe)

    rich_text_area = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))
    driver.execute_script("arguments[0].innerHTML = 'THIS IS SAMPLE ONLY';", rich_text_area)

    driver.switch_to.default_content()

    textarea = wait.until(EC.presence_of_element_located((By.ID, "aud_rationale_fnote")))
    textarea.clear()
    textarea.send_keys("THIS IS SAMPLE ONLY")

    time.sleep(2)

finally:
    login_bot.quit()

