import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://10.10.99.18:8002/login")
driver.maximize_window()
#driver.execute_script("document.body.style.zoom='50%'")


wait = WebDriverWait(driver, 15)

username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
username_input.send_keys("bnjmntumbaga@gmail.com")

password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
password_input.send_keys("Dost@123")

login_button = wait.until(EC.element_to_be_clickable((By.ID, "login")))
login_button.click()

time.sleep(3)
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[-1])


TARGET_URL = "http://10.10.99.18:8002/auditDetails/83"
driver.get(TARGET_URL)
driver.execute_script("document.body.style.zoom='80%'")
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.ID, "auditPlanSelect"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "//option[normalize-space()='IX. Line-Item Budget']"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.ID, "auditPlanSelect"))).click()
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-plus text-white-100'])[3]"))).click()


import re

def clean_text(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = cleaned_text.replace(u'\xa0', ' ').strip()
    return cleaned_text


################################ input
time.sleep(2)
SelectExpenseCategorySelection = wait.until(EC.element_to_be_clickable((By.XPATH, "(//option[normalize-space()='Representation Expense'])[1]")))
SelectExpenseCategorySelection.click()
selected_value = driver.find_element(By.XPATH, "(//option[normalize-space()='Representation Expense'])[1]").get_attribute("value")


time.sleep(1)
lineItem = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='line-item'])[1]")))
lineItem.send_keys("Test line-item")


time.sleep(1)
details = wait.until(EC.presence_of_element_located((By.XPATH, "(//textarea[@id='details'])[1]")))
details.send_keys("Test details")



time.sleep(1)
calculator = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='calculator-popover'])[1]")))
calculator.click()

time.sleep(1)
calculator7 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='7'])[1]")))
calculator7.click()

time.sleep(1)
CalculatorPlus = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='+'])[1]")))
CalculatorPlus.click()

time.sleep(1)
Calculator5 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='5'])[1]")))
Calculator5.click()

time.sleep(1)
CalculatorEqual = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='='])[1]")))
CalculatorEqual.click()

time.sleep(1)
CopyResult = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='Copy Result'])[1]")))
CopyResult.click()

amount_field = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='lib-amount'])[1]")))
amount_value = amount_field.get_attribute("value")
time.sleep(1)

save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addLineItemBudget'])[1]")))
save_button.click()
time.sleep(1)

try:
    line_item_save_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Line-Item Budget added successfully'])[1]")
    assert line_item_save_message_label .text.strip() == "Line-Item Budget added successfully", "Incorrect spelling"
    print("✅Test case 1 : line_item_save_message_label  Passed")
except NoSuchElementException:
    print("❌Test Case 1 Failed: line_item_save_message_label ")
except AssertionError as e:
    print(f"❌Test Case 1 Failed: {e}")

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]"))).click()
time.sleep(1)


#############✅ Test 1

time.sleep(1)
Expense_Category = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[normalize-space()='Honoraria'])[1]"))
).text
Expense_Category= clean_text(Expense_Category)
print("Expense Category:", Expense_Category)


Line_Item = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//p[@class='fs-6'])[1]"))
).text
cleaned_text = re.sub(r'^\d+\.\s*', '',Line_Item)
print("Line Item (cleaned):", cleaned_text)


Details = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//p[@class='detail-text'])[1]"))
).text
Details = clean_text(Details)
print("Details:", Details)

Amount = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='12.00']"))
).text
Amount = clean_text(Amount)
print("Amount:", Amount)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//p[@class='fs-6'])[1]"))).click()
time.sleep(1)
#############################



Expense_Category_model = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//option[normalize-space()='Honoraria'])[1]"))
).text
Expense_Category_model = clean_text(Expense_Category_model)
print("Expense Category :",Expense_Category_model )
if  Expense_Category == Expense_Category_model:
    print("✅ Test 2: Data match!")
else:
    print("❌ Test 2: Data do NOT match!")


Line_Item_model = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@id='line-item'])[1]"))
)
Line_Item_model = clean_text(Line_Item_model.get_attribute("value"))
Line_Item_model_cleaned_text = re.sub(r'^\d+\.\s*', '',Line_Item_model)
print("Line Item :", Line_Item_model_cleaned_text)

if Line_Item_model_cleaned_text == cleaned_text:
    print("✅ Test 3: Data match!")
else:
    print("❌ Test 3: Data do NOT match!")


Details_model = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//textarea[@id='details'])[1]"))
)
Details_model = clean_text(Details_model.get_attribute("value"))
print("Details :", Details_model)

if  Details == Details_model:
    print("✅ Test 4: Data match!")
else:
    print("❌ Test 4: Data do NOT match!")


Amount_model  = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@id='lib-amount'])[1]"))
)
Amount_model  = clean_text(Amount_model .get_attribute("value"))
print("Amount :", Amount_model )

if  Amount == Amount_model :
    print("✅ Test 5: Data match!")
else:
    print("❌ Test 5: Data do NOT match!")

time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='deleteLineItemBudget'])[1]"))).click()
time.sleep(1)

try:
    delete_save_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Are you sure you want to delete this item?'])[1]")
    message_text = delete_save_message_label.text.strip()

    if message_text == "Are you sure you want to delete this item?":
        print("✅ Test 6: delete_save_message_label Passed")
    else:
        print(f"❌ Test 6 Failed: Text mismatch - Found '{message_text}'")
except Exception as e:
    print(f"❌ Test 6 Failed: delete_save_message_label not found - {str(e)}")

time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Ok'])[1]"))).click()

time.sleep(1)

try:
    delete_success_save_message_label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Expense item deleted successfully'])[1]")
    message_text = delete_success_save_message_label.text.strip()

    if message_text == "Expense item deleted successfully":
        print("✅ Test 7: delete_success_save_message_label Passed")
    else:
        print(f"❌ Test 7 Failed: Text mismatch - Found '{message_text}'")
except Exception as e:
    print(f"❌ Test 7 Failed: delete_success_save_message_label not found - {str(e)}")

time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]"))).click()


time.sleep(3)

# ✅ Close browser
driver.quit()
