from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuditLogin:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://10.10.99.18:8002/login")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def login(self):
        username_str = "Superadmin@gmail.com"
        password_str = "Dost@123"

        username = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password = self.driver.find_element(By.NAME, "password")

        username.clear()
        username.send_keys(username_str)

        password.clear()
        password.send_keys(password_str)
        password.send_keys(Keys.RETURN)

        self.wait.until(EC.url_contains("/dashboard"))

    def go_to_audit_page(self):
        self.driver.get("http://10.10.99.18:8002/audit")

    def quit(self):
        self.driver.quit()
