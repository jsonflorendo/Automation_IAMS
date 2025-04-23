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

finally:
    driver.quit()
