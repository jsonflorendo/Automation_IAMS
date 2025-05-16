from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://10.10.99.18:8002/login")
  
# Login function
def login():

    try: 
            
        username_input = "bnjmntumbaga@gmail.com"
        password_input = "Dost@123"

        time.sleep(1)
        driver.find_element(By.ID,"username").send_keys(username_input)

        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys(password_input)

        time.sleep(1)
        driver.find_element(By.ID,"login").click()

    except Exception as e:
    
        print("Error", str(e))