from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    target_cell = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#DataTables_Table_1 > tbody > tr:nth-child(3) > td:nth-child(2)")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_cell)
    time.sleep(0.5)
    try:
        target_cell.click()
    except:
        driver.execute_script("arguments[0].click();", target_cell)

    dropdown_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#dropdownMenuLink > i")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown_icon)
    time.sleep(0.5)
    try:
        dropdown_icon.click()
    except:
        driver.execute_script("arguments[0].click();", dropdown_icon)

    try:
        time.sleep(1.5)
        secretary_directive = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#secretaryDirective")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", secretary_directive)
        time.sleep(0.3)
        try:
            secretary_directive.click()
        except:
            driver.execute_script("arguments[0].click();", secretary_directive)
    except Exception as e:
        pass

    try:
        time.sleep(1)
        select2_container = driver.execute_script("return document.querySelector('#select2-tpl_name-container')")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", select2_container)
        time.sleep(0.5)
        select2_container.click()

        time.sleep(1)
        communication_letter_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//ul[@id='select2-tpl_name-results']/li[contains(text(), 'Communication Letter')]")
        ))
        communication_letter_option.click()

        time.sleep(1)
        update_btn = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#addOrUpdateEmailTemplate")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", update_btn)
        update_btn.click()

    except Exception as e:
        pass

finally:
    time.sleep(3)
    driver.quit()
