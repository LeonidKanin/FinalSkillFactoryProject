# команда для запуска в PyCharm
# pytest -v --driver Chrome --driver-path chromedriver.exe tests/tests_recovery_page.py

import pytest

from pages.locators import CaptchaLocators
from pages.recovery_page import RecoveryPage
from prepare.for_common_elem import InputWithoutRestrictions
from tests.common_to_multiple_pages import *


@pytest.mark.structure
def test_page_structure(name_test, driver):
    page_structure(name_test, RecoveryPage(driver))


@pytest.mark.structure
def test_header_page(name_test, driver):
    header_page(name_test, RecoveryPage(driver))


@pytest.mark.structure
def test_left_section_page(name_test, driver):
    left_section_page(name_test, RecoveryPage(driver))


@pytest.mark.structure
def test_right_section_page(name_test, driver):
    right_section_page(name_test, RecoveryPage(driver))


@pytest.mark.structure
@pytest.mark.func
def test_footer_page(driver):
    footer_page(RecoveryPage(driver), driver)


@pytest.mark.func
def test_user_data_choice_tab(name_test, driver):
    input_container_choice_tab(name_test, RecoveryPage(driver), driver)


@pytest.mark.func
def test_user_data_auto_select_tab(driver):
    input_container_auto_select_tab(RecoveryPage(driver))


@pytest.mark.func
def test_user_data_auto_substitution_phone(driver):
    input_container_auto_substitution_phone(RecoveryPage(driver))


@pytest.mark.func
def test_user_data_phone_number_error(driver):
    input_container_phone_number_error(RecoveryPage(driver))


@pytest.mark.func
def test_user_data_lower_name_email(driver):
    input_container_lower_name_email(RecoveryPage(driver))


@pytest.mark.func
def test_user_data_login(driver):
    input_container_login(RecoveryPage(driver))


@pytest.mark.func
def test_user_data_LS(driver):
    input_container_LS(RecoveryPage(driver))


@pytest.mark.func
def test_captcha(driver):

    page = RecoveryPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Восстановление пароля'

    text = InputWithoutRestrictions.input_data

    captcha_value = page.captcha_id().get_attribute('value')
    page.captcha_reload().click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CaptchaLocators.Captcha_Img))
    assert page.captcha_id().get_attribute('value') != captcha_value

    page.captcha_input().send_keys(text)
    assert page.captcha_input_text().get_attribute('innerText') == text

    page.captcha_input().click()
    right_border_text(page.captcha_input(), len(text))
    clear_text(page.captcha_input(), len(text))

    assert page.captcha_input_text().get_attribute('innerText') == ''


@pytest.mark.func
def test_recovery_btn(driver):
    page = RecoveryPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Восстановление пароля'
    assert page.user_data_placeholder().text == 'Мобильный телефон'

    page.recovery_btn.click()
    assert page.user_data_error().text == 'Введите номер телефона'


@pytest.mark.func
def test_return_btn(driver):
    page = RecoveryPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Восстановление пароля'

    page.return_btn.click()
    assert page.header_input().get_attribute('innerText') == 'Авторизация'


@pytest.mark.script
def test_incorrect_input_captcha_text(driver):

    page = RecoveryPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Восстановление пароля'

    page.login_tab().click()
    page.user_data_input().send_keys('TestTest')
    page.recovery_btn.click()

    assert page.form_error().text == 'Неверный логин или текст с картинки'
