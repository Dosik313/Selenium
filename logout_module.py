import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Logout:
    def __init__(self,driver):
        self.driver = driver

    def log_out(self,user):
        time.sleep(3)
        hide_menu = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//button[@id="react-burger-menu-btn"]')))
        hide_menu.click()

        logout = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="logout_sidebar_link"]')))
        logout.click()

        logout_check = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="login_logo"]')))
        text_login = logout_check.text
        assert text_login == 'Swag Labs', f"Ошибка, текст лого: {text_login}"
        print(f"Пользователь {user} успешно вышел из системы")
