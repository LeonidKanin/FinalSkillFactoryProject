from selenium.webdriver.common.by import By


class HeaderLocators:
    App_Header = (By.ID, "app-header")
    Header_Logo = (By.CSS_SELECTOR, ".main-header__logo-container>svg")


class LeftSectionLocators:
    Left_Section_Id = (By.ID, "page-left")
    Left_Container_Logo = (By.CSS_SELECTOR, ".what-is-container__logo-container")
    Left_Title = (By.CSS_SELECTOR, ".what-is__title")
    Left_Desc = (By.CSS_SELECTOR, ".what-is__desc")


class RightSectionLocators:
    Right_Section_Id = (By.ID, "page-right")
    Header_Input = (By.TAG_NAME, "h1")
    Error_Input_Form = (By.ID, "form-error-message")  # explicit wait


class FooterLocators:
    Footer_Page_Id = (By.ID, "app-footer")
    Footer_Copyright = (By.CSS_SELECTOR, ".rt-footer-left__item.rt-footer-copyright")
    Footer_Links_Item = (By.XPATH, "//div[@class='rt-footer-left__item']")
    Link_Cookie = (By.ID, "cookies-tip-open")
    Cookie_Tooltip = (By.CLASS_NAME, "rt-tooltip")
    Cookie_Tooltip_Close = (By.CLASS_NAME, "rt-tooltip__close")
    Cookie_Tooltip_Title = (By.CLASS_NAME, "rt-tooltip__title")
    Cookie_Tooltip_Desc = (By.CLASS_NAME, "rt-cookies-tip__desc")
    Link_Agreements = (By.CSS_SELECTOR, "#rt-footer-agreement-link>span")
    Title_Phone_Support = (By.CLASS_NAME, "rt-footer-right")
    Phone_Support = (By.CLASS_NAME, "rt-footer-right__support-phone")


class InputContainerLocators:
    Phone_Input = (By.ID, "t-btn-tab-phone")
    Mail_Input = (By.ID, "t-btn-tab-mail")
    Login_Input = (By.ID, "t-btn-tab-login")
    LS_Input = (By.ID, "t-btn-tab-ls")
    Tab_Type = (By.XPATH, "//input[@name='tab_type']")
    User_Data_Input = (By.ID, "username")
    User_Data_Text = (By.XPATH, "//input[@name='username']")
    User_Data_Placeholder = (By.CLASS_NAME, "rt-input__placeholder")
    Error_User_Data_Input = (By.CSS_SELECTOR, "span.rt-input-container__meta.rt-input-container__meta--error")


class LinksLocators:
    Link_VK = (By.CSS_SELECTOR, "#oidc_vk>svg")
    Link_OK = (By.CSS_SELECTOR, "#oidc_ok>svg")
    Link_Mail = (By.CSS_SELECTOR, "#oidc_mail>svg")
    Link_YA = (By.CSS_SELECTOR, "#oidc_ya>svg")


class CaptchaLocators:
    Captcha_Id = (By.ID, "captcha_id")
    Captcha_Img = (By.CSS_SELECTOR, ".rt-captcha__image")
    Captcha_Reload = (By.CSS_SELECTOR, ".rt-captcha__reload-con > svg")
    Captcha_Input = (By.ID, "captcha")
    Captcha_Input_Text = (By.XPATH, "//input[@id='captcha']/../span/span[@class='rt-input__mask-start']")


class RegistrationBtnLocator:
    Registration_Btn = (By.ID, "kc-register")


class SelectRegionLocators:
    Select_Dropdown = (By.CLASS_NAME, 'div.rt-select__list-wrapper.rt-select__list-wrapper--rounded')
    Select_Input = (By.CSS_SELECTOR, "input[name='region']")
    Select_Region = (By.CSS_SELECTOR, '.rt-select__list-item')


class PassInputLocators:
    Pass_Input = (By.ID, "password")
    Pass_Input_Actions = (By.XPATH, "//input[@id='password']/../div[@class='rt-input__action']")
    Pass_Input_Placeholder = (By.XPATH, "//input[@id='password']/../span[@class='rt-input__placeholder']")
    Pass_Text = (By.XPATH, "//input[@id='password']/..//span[@class='rt-input__mask-start']")
    Error_Pass_Input = (By.XPATH, "//input[@id='password']/../../span")  # explicit wait


class ErrorForm:
    Error_Form = (By.ID, "form-error-message")


class AuthLocators(RightSectionLocators, InputContainerLocators, PassInputLocators, CaptchaLocators, LinksLocators,
                   RegistrationBtnLocator, ErrorForm):
    Remember_Checkbox = (By.CSS_SELECTOR, ".rt-checkbox__shape")
    Remember_Checkbox_Sign = (By.CSS_SELECTOR, ".rt-checkbox__shape>svg")
    Remember_Checkbox_Text = (By.XPATH, "//span[text()='Запомнить меня']")
    Forgot_Password = (By.ID, "forgot_password")
    Auth_Policy = (By.CSS_SELECTOR, ".auth-policy")
    Auth_Btn = (By.ID, "kc-login")


class RecoveryLocators(RightSectionLocators, InputContainerLocators, CaptchaLocators, ErrorForm):
    Recovery_Btn = (By.ID, "reset")
    Return_Btn = (By.ID, "reset-back")


class RegisterLocators(RightSectionLocators, PassInputLocators, RegistrationBtnLocator, SelectRegionLocators,
                       ErrorForm):
    Name_Input = (By.CSS_SELECTOR, ".rt-input__input[name='firstName']")
    Name_Text = (By.XPATH, "//span[text()='Имя']/..//span[@class='rt-input__mask-start']")
    Name_Placeholder = (By.XPATH, "//input[@name='firstName']/../span[@class='rt-input__placeholder']")
    Error_Name_Input = (By.XPATH, "//span[text()='Имя']/../../span")  # explicit wait
    Surname_Input = (By.CSS_SELECTOR, ".rt-input__input[name='lastName']")
    Surname_Text = (By.XPATH, "//span[text()='Фамилия']/..//span[@class='rt-input__mask-start']")
    Surname_Placeholder = (By.XPATH, "//input[@name='lastName']/../span[@class='rt-input__placeholder']")
    Error_Surname_Input = (By.XPATH, "//span[text()='Фамилия']/../../span")  # explicit wait
    Region_Input = (By.XPATH, "//span[text()='Регион']/..//input")
    Region_Input_Actions = (By.XPATH, "//span[text()='Регион']/../div[@class='rt-input__action']")
    Region_Text = (By.XPATH, "//span[text()='Регион']/..//span[@class='rt-input__mask-start']")
    Mail_Phone_Input = (By.ID, 'address')
    Mail_Phone_Text = (By.NAME, 'address')
    Mail_Phone_Placeholder = (By.XPATH, "//input[@id='address']/../span[@class='rt-input__placeholder']")
    Error_Mail_Phone_Input = (By.XPATH, "//input[@id='address']/../../span")  # explicit wait
    Pass_Confirm_Input = (By.ID, "password-confirm")
    Pass_Confirm_Input_Actions = (By.XPATH, "//input[@id='password-confirm']/../div[@class='rt-input__action']")
    Pass_Confirm_Placeholder = (By.XPATH, "//input[@id='password-confirm']/../span[@class='rt-input__placeholder']")
    Pass_Confirm_Text = (By.XPATH, "//input[@id='password-confirm']/..//span[@class='rt-input__mask-start']")
    Error_Pass_Confirm_Input = (By.XPATH, "//input[@id='password-confirm']/../../span")  # explicit wait
    Register_Btn = (By.CLASS_NAME, "register-form__reg-btn")
    Auth_Policy = (By.CSS_SELECTOR, ".rt-link")


class NewPage:
    Header_Page = (By.CSS_SELECTOR, "h1")
