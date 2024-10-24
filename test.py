from logout_module import Logout
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from credential import LoginCred
from login_page import LoginPage
from driver import driver

class TestAllUser:
    def test_standard_user(self, driver):
        print(f"Start test")
        user_list = [
            LoginCred.standard_user,
            LoginCred.locked_out_user,
            LoginCred.problem_user,
            LoginCred.performance_glitch_user,
            LoginCred.error_user,
            LoginCred.visual_user
        ]

        password = LoginCred.password

        login = LoginPage(driver)
        logout = Logout(driver)
        for user in user_list:
            try:
                login.auth(login_name=user, login_password=password)
                print(f" Ввожу логин {user} и пароль {password}")
                title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//span[@class="title"]'))).text
                assert title == 'Products', f"Ошибка, название титула {title}"
                print(f"Успешно вошел в систему под логином {user}")
                logout.log_out(user)
            except:
                if WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//h3[@data-test="error"]'))):
                    print(f"Появилась ошибка, перезагружаю страницу")
                    driver.refresh()
                else:
                    continue
        print(f"Test over")