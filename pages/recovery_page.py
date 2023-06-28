from pages.common_elements_pages import CommonPageElements
from pages.base_page import BasePage
from pages.locators import RecoveryLocators


class RecoveryPage(BasePage, CommonPageElements):

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        url = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials"
        driver.get(url)

        self.driver = driver

        # создаем нужные элементы страницы
        self.recovery_btn = driver.find_element(*RecoveryLocators.Recovery_Btn)
        self.return_btn = driver.find_element(*RecoveryLocators.Return_Btn)

    def error_input_message(self):
        error = self.driver.find_element(*RecoveryLocators.Error_Input_Form)
        return error.text
