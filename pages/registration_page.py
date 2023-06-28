from pages.common_elements_pages import CommonPageElements
from pages.base_page import BasePage
from pages.locators import RegisterLocators, SelectRegionLocators


class RegistrationPage(BasePage, CommonPageElements):

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        url = "https://b2c.passport.rt.ru"
        driver.get(url)
        driver.find_element(*RegisterLocators.Registration_Btn).click()

        self.driver = driver

        # создаем нужные элементы страницы
        self.name_input = driver.find_element(*RegisterLocators.Name_Input)
        self.name_placeholder = driver.find_element(*RegisterLocators.Name_Placeholder)
        self.name_text = driver.find_element(*RegisterLocators.Name_Text)
        self.surname_input = driver.find_element(*RegisterLocators.Surname_Input)
        self.surname_placeholder = driver.find_element(*RegisterLocators.Surname_Placeholder)
        self.surname_text = driver.find_element(*RegisterLocators.Surname_Text)
        self.region_input = driver.find_element(*RegisterLocators.Region_Input)
        self.region_input_actions = driver.find_element(*RegisterLocators.Region_Input_Actions)
        self.region_text = driver.find_element(*RegisterLocators.Region_Text)
        self.mail_phone_input = driver.find_element(*RegisterLocators.Mail_Phone_Input)
        self.mail_phone_placeholder = driver.find_element(*RegisterLocators.Mail_Phone_Placeholder)
        self.mail_phone_text = driver.find_element(*RegisterLocators.Mail_Phone_Text)
        self.pass_confirm_input = driver.find_element(*RegisterLocators.Pass_Confirm_Input)
        self.pass_confirm_input_action = driver.find_element(*RegisterLocators.Pass_Confirm_Input_Actions)
        self.pass_confirm_placeholder = driver.find_element(*RegisterLocators.Pass_Confirm_Placeholder)
        self.pass_confirm_text = driver.find_element(*RegisterLocators.Pass_Confirm_Text)
        self.register_btn = driver.find_element(*RegisterLocators.Register_Btn)
        self.auth_policy = driver.find_element(*RegisterLocators.Auth_Policy)

    def name_error(self):
        return self.driver.find_element(*RegisterLocators.Error_Name_Input)

    def surname_error(self):
        return self.driver.find_element(*RegisterLocators.Error_Surname_Input)

    def mail_phone_error(self):
        return self.driver.find_element(*RegisterLocators.Error_Mail_Phone_Input)

    def password_confirm_error(self):
        return self.driver.find_element(*RegisterLocators.Error_Pass_Confirm_Input)

    def select_region(self):
        return self.driver.find_elements(*SelectRegionLocators.Select_Region)

    def select_input_value(self, value):
        self.driver.find_element(*SelectRegionLocators.Select_Input).send_keys(value)

    def error_name_input(self):
        return self.driver.find_element(*RegisterLocators.Error_Name_Input)

    def get_attributes(self, element) -> dict:
        return self.driver.execute_script(
            """
            let attr = arguments[0].attributes;
            let items = {}; 
            for (let i = 0; i < attr.length; i++) {
                items[attr[i].name] = attr[i].value;
            }
            return items;
            """,
            element
        )
