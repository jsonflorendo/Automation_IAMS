from LOGIN import AuditLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

login_bot = AuditLogin()

try:
    login_bot.login()
    login_bot.go_to_audit_page()

    wait = login_bot.wait
    driver = login_bot.driver

    audit_cell = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[text()='Annual Compliance Audit']")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", audit_cell)
    driver.execute_script("arguments[0].click();", audit_cell)
    time.sleep(2)

    select_element = wait.until(EC.presence_of_element_located((By.ID, "auditPlanSelect")))
    select = Select(select_element)
    select.select_by_visible_text("VII. Audit Timeline")
    time.sleep(2)

    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe#aud_timeline_ifr")))
    driver.switch_to.frame(iframe)

    body = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))
    body.clear()
    body.send_keys("THIS IS SAMPLE TIMELINE ONLY")

    driver.switch_to.default_content()
    time.sleep(2)

    target_element = wait.until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[4]/div/div/div[7]/section/div[3]/div/div/div[1]/div/div/div[1]/div[4]"
    )))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_element)
    driver.execute_script("arguments[0].click();", target_element)
    time.sleep(2)

    try:
        textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[starts-with(@id, 'input_')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", textarea)
        textarea.clear()
        textarea.send_keys("SAMPLE TASK")
        time.sleep(2)
    except Exception:
        pass

    try:
        driver.switch_to.default_content()

        days_dropdown = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//select[contains(@aria-label, 'Days')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", days_dropdown)

        days_select = Select(days_dropdown)
        days_select.select_by_visible_text("5")  # Halimbawa: piliin ang 5

        time.sleep(2)
    except Exception:
        pass

    try:
        months_dropdown = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//select[contains(@aria-label, 'Months')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", months_dropdown)

        months_select = Select(months_dropdown)
        months_select.select_by_visible_text("June")  # Halimbawa: piliin ang June

        time.sleep(2)
    except Exception:
        pass

    try:
        years_dropdown = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//select[contains(@aria-label, 'Years')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", years_dropdown)

        years_select = Select(years_dropdown)
        years_select.select_by_visible_text("2026")  # Halimbawa: piliin ang 2026

        time.sleep(2)
    except Exception:
        pass

    try:
        plus_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input.gantt_duration_inc"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", plus_button)
        plus_button.click()
        time.sleep(2)
    except Exception:
        pass

    try:
        save_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#main-body > div.gantt_cal_cover > div > div.gantt_cal_lcontrols > div.gantt_btn_set.gantt_left_btn_set.gantt_save_btn_set > div:nth-child(2)"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
        save_button.click()
        time.sleep(2)
    except Exception:
        pass
    try:
        confirm_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal2-confirm.swal2-styled"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", confirm_button)
        confirm_button.click()
        time.sleep(2)
    except Exception:
        pass

    try:
        export_pdf_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#export-pdf-btn"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", export_pdf_button)
        export_pdf_button.click()
        time.sleep(5)
    except Exception:
        pass

finally:
    login_bot.quit()
