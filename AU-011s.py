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

    auditees_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#auditees-tab")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", auditees_tab)
    time.sleep(0.5)
    auditees_tab.click()

    time.sleep(2)

    target_cell = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "#DataTables_Table_0 > tbody > tr:nth-child(13) > td:nth-child(2)"
    )))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_cell)
    time.sleep(0.5)
    target_cell.click()

    email_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#emailNotification > i")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", email_icon)
    time.sleep(0.5)
    email_icon.click()

    select2_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#aueEmailRecipientDiv .select2-container")))
    select2_box.click()

    search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".select2-search__field")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", search_box)
    time.sleep(0.5)

    driver.execute_script("arguments[0].value = 'lewnuyda@gmail.com';", search_box)
    driver.execute_script(""" 
        let event = new Event('input', {bubbles: true});
        arguments[0].dispatchEvent(event);
        let keyupEvent = new KeyboardEvent('keyup', {bubbles: true, key: 'Enter'});
        arguments[0].dispatchEvent(keyupEvent);
    """, search_box)

    time.sleep(1)

    email_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//li[contains(@class, 'select2-results__option') and text()='lewnuyda@gmail.com']"
    )))
    email_option.click()

    tpl_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='select2-tpl_name-container']")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tpl_dropdown)
    tpl_dropdown.click()

    tpl_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//li[contains(@class, 'select2-results__option') and normalize-space(text())='Communication Letter']"
    )))
    tpl_option.click()

    add_tpl_attachment_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#addTplAttachment")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_tpl_attachment_button)
    add_tpl_attachment_button.click()

    file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
    file_input.send_keys(r"C:\Users\Acer\OneDrive\2016-Succession-Q-A_092046.pdf")

    send_email_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sendEmailTemplate")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", send_email_button)
    send_email_button.click()

    time.sleep(7)
    time.sleep(3)

except Exception as e:
    pass

finally:
    login_bot.quit()
