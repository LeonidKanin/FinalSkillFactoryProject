from pages.base_page import BasePage
from pages.common_elements_pages import CommonPageElements
from pages.locators import AuthLocators


class AuthPage(BasePage, CommonPageElements):

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        url = "https://b2c.passport.rt.ru"
        driver.get(url)

        self.driver = driver

        # создаем нужные элементы страницы
        self.remember_checkbox = driver.find_element(*AuthLocators.Remember_Checkbox)
        self.remember_checkbox_text = driver.find_element(*AuthLocators.Remember_Checkbox_Text)
        self.forgot_password = driver.find_element(*AuthLocators.Forgot_Password)
        self.auth_btn = driver.find_element(*AuthLocators.Auth_Btn)
        self.auth_policy = driver.find_element(*AuthLocators.Auth_Policy)
        self.link_vk = driver.find_element(*AuthLocators.Link_VK)
        self.link_ok = driver.find_element(*AuthLocators.Link_OK)
        self.link_mail = driver.find_element(*AuthLocators.Link_Mail)
        self.link_ya = driver.find_element(*AuthLocators.Link_YA)
        self.registration_btn = driver.find_element(*AuthLocators.Registration_Btn)

    def remember_checkbox_sign(self):
        return self.driver.find_element(*AuthLocators.Remember_Checkbox_Sign)

    def error_input_message(self):
        error = self.driver.find_element(*AuthLocators.Error_Input_Form)
        return error.text

    def error_input_phone(self):
        error = self.driver.find_element(*AuthLocators.Error_User_Data_Input)
        return error.text
