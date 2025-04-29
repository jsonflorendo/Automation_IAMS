from LOGIN import AuditLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

login_bot = AuditLogin()

try:
    login_bot.login()
    login_bot.go_to_audit_page()

    wait = login_bot.wait
    driver = login_bot.driver

    target_cell = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#DataTables_Table_1 > tbody > tr:nth-child(3) > td:nth-child(2)")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_cell)
    try:
        target_cell.click()
    except:
        driver.execute_script("arguments[0].click();", target_cell)

    dropdown_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#dropdownMenuLink > i")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown_icon)
    try:
        dropdown_icon.click()
    except:
        driver.execute_script("arguments[0].click();", dropdown_icon)

    try:
        secretary_directive = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#secretaryDirective")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", secretary_directive)
        try:
            secretary_directive.click()
        except:
            driver.execute_script("arguments[0].click();", secretary_directive)
    except:
        pass

    try:
        tpl_name_container = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select2-tpl_name-container")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tpl_name_container)
        tpl_name_container.click()

        search_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.select2-search__field")))
        search_input.send_keys("SAMPLE SUBJECT TEMPLATE")

        sample_subject_option = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//ul[@id='select2-tpl_name-results']/li[contains(text(), 'SAMPLE SUBJECT TEMPLATE')]"
        )))
        sample_subject_option.click()
    except:
        pass

    try:
        subject_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#subject")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", subject_input)
        subject_input.clear()
        subject_input.send_keys("SAMPLE SUBJECT TEMPLATE")
    except:
        pass

    try:
        add_tpl_attachment_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#addTplAttachment")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_tpl_attachment_button)
        add_tpl_attachment_button.click()

        file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
        file_input.send_keys(r"C:\Users\Acer\OneDrive\2016-Succession-Q-A_092046.pdf")

    except:
        pass
    try:
        add_or_update_email_template_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#addOrUpdateEmailTemplate")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_or_update_email_template_button)
        add_or_update_email_template_button.click()

        time.sleep(9)
    except:
        pass

finally:
    login_bot.quit()
