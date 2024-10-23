from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

login_check = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="login_logo"]')))
text = login_check.text
print(text)
