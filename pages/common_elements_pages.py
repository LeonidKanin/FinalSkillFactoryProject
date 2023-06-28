from pages.locators import *


class CommonPageElements(object):
    def __init__(self, driver):
        self.driver = driver

    def app_header_id(self):
        return self.driver.find_element(*HeaderLocators.App_Header)

    def header_logo(self):
        return self.driver.find_element(*HeaderLocators.Header_Logo)

    def left_section_id(self):
        return self.driver.find_element(*LeftSectionLocators.Left_Section_Id)

    def left_container_logo(self):
        return self.driver.find_element(*LeftSectionLocators.Left_Container_Logo)

    def left_title(self):
        return self.driver.find_element(*LeftSectionLocators.Left_Title)

    def left_desc(self):
        return self.driver.find_element(*LeftSectionLocators.Left_Desc)

    def right_section_id(self):
        return self.driver.find_element(*RightSectionLocators.Right_Section_Id)

    def header_input(self):
        return self.driver.find_element(*RightSectionLocators.Header_Input)

    def footer_id(self):
        return self.driver.find_element(*FooterLocators.Footer_Page_Id)

    def footer_copyright(self):
        return self.driver.find_element(*FooterLocators.Footer_Copyright)

    def footer_links_item(self):
        return self.driver.find_element(*FooterLocators.Footer_Links_Item)

    def footer_link_cookie(self):
        return self.driver.find_element(*FooterLocators.Link_Cookie)

    def footer_cookie_tooltip(self):
        return self.driver.find_element(*FooterLocators.Cookie_Tooltip)

    def footer_cookie_tooltip_close(self):
        return self.driver.find_element(*FooterLocators.Cookie_Tooltip_Close)

    def footer_cookie_tooltip_title(self):
        return self.driver.find_element(*FooterLocators.Cookie_Tooltip_Title)

    def footer_cookie_tooltip_desc(self):
        return self.driver.find_elements(*FooterLocators.Cookie_Tooltip_Desc)

    def footer_title_phone_support(self):
        return self.driver.find_element(*FooterLocators.Title_Phone_Support)

    def footer_phone_support(self):
        return self.driver.find_element(*FooterLocators.Phone_Support)

    def footer_link_agreements(self):
        return self.driver.find_elements(*FooterLocators.Link_Agreements)

    def phone_tab(self):
        return self.driver.find_element(*InputContainerLocators.Phone_Input)

    def mail_tab(self):
        return self.driver.find_element(*InputContainerLocators.Mail_Input)

    def login_tab(self):
        return self.driver.find_element(*InputContainerLocators.Login_Input)

    def LS_tab(self):
        return self.driver.find_element(*InputContainerLocators.LS_Input)

    def tab_type(self):
        return self.driver.find_element(*InputContainerLocators.Tab_Type)

    def user_data_input(self):
        return self.driver.find_element(*InputContainerLocators.User_Data_Input)

    def user_data_text(self):
        return self.driver.find_element(*InputContainerLocators.User_Data_Text)

    def user_data_placeholder(self):
        return self.driver.find_element(*InputContainerLocators.User_Data_Placeholder)

    def user_data_error(self):
        return self.driver.find_element(*InputContainerLocators.Error_User_Data_Input)

    def pass_input(self):
        return self.driver.find_element(*PassInputLocators.Pass_Input)

    def pass_input_actions(self):
        return self.driver.find_element(*PassInputLocators.Pass_Input_Actions)

    def pass_placeholder(self):
        return self.driver.find_element(*PassInputLocators.Pass_Input_Placeholder)

    def pass_input_text(self):
        return self.driver.find_element(*PassInputLocators.Pass_Text)

    def password_error(self):
        return self.driver.find_element(*PassInputLocators.Error_Pass_Input)

    def captcha_id(self):
        return self.driver.find_element(*CaptchaLocators.Captcha_Id)

    def captcha_reload(self):
        return self.driver.find_element(*CaptchaLocators.Captcha_Reload)

    def captcha_input(self):
        return self.driver.find_element(*CaptchaLocators.Captcha_Input)

    def captcha_input_text(self):
        return self.driver.find_element(*CaptchaLocators.Captcha_Input_Text)

    def form_error(self):
        return self.driver.find_element(*ErrorForm.Error_Form)

    def header_new_page(self):
        return self.driver.find_element(*NewPage.Header_Page)
