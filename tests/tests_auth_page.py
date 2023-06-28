# команда для запуска в PyCharm
# pytest -v --driver Chrome --driver-path chromedriver.exe tests/tests_auth_page.py

import pytest

from pages.auth_page import AuthPage
from prepare.for_common_elem import InputWithoutRestrictions
from tests.common_to_multiple_pages import *
from selenium.common import NoSuchElementException


@pytest.mark.structure
def test_page_structure(name_test, driver):
    page_structure(name_test, AuthPage(driver))


@pytest.mark.structure
def test_header_page(name_test, driver):
    header_page(name_test, AuthPage(driver))


@pytest.mark.structure
def test_left_section_page(name_test, driver):
    left_section_page(name_test, AuthPage(driver))


@pytest.mark.structure
def test_right_section_page(name_test, driver):
    right_section_page(name_test, AuthPage(driver))


@pytest.mark.structure
@pytest.mark.func
def test_footer_page(driver):
    footer_page(AuthPage(driver), driver)


@pytest.mark.func
def test_user_data_choice_tab(name_test, driver):
    input_container_choice_tab(name_test, AuthPage(driver), driver)


@pytest.mark.func
def test_user_data_auto_select_tab(driver):
    input_container_auto_select_tab(AuthPage(driver))


@pytest.mark.func
def test_user_data_auto_substitution_phone(driver):
    input_container_auto_substitution_phone(AuthPage(driver))


@pytest.mark.func
def test_user_data_phone_number_error(driver):
    input_container_phone_number_error(AuthPage(driver))


@pytest.mark.func
def test_user_data_lower_name_email(driver):
    input_container_lower_name_email(AuthPage(driver))


@pytest.mark.func
def test_user_data_login(driver):
    input_container_login(AuthPage(driver))


@pytest.mark.func
def test_user_data_LS(driver):
    input_container_LS(AuthPage(driver))


@pytest.mark.func
def test_password_input(driver):

    page = AuthPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Авторизация'

    password = InputWithoutRestrictions.input_data

    assert page.header_input().get_attribute('innerText') == 'Авторизация'
    assert page.pass_placeholder().text == 'Пароль'

    assert page.pass_input().get_attribute('type') == 'password'
    page.pass_input_actions().click()
    assert page.pass_input().get_attribute('type') == 'text'

    page.pass_input().send_keys(password)

    assert page.pass_input_text().get_attribute('innerText') == password

    page.pass_input_actions().click()
    page.pass_input().click()

    right_border_text(page.pass_input(), len(password))
    clear_text(page.pass_input(), len(password))

    assert page.pass_input().get_attribute('type') == 'password'
    assert page.pass_input_text().get_attribute('innerText') == ''


@pytest.mark.func
def test_remember_checkbox(driver):

    page = AuthPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Авторизация'

    assert page.remember_checkbox_text.text == 'Запомнить меня'
    assert page.remember_checkbox_sign()

    page.remember_checkbox_text.click()
    try:
        page.remember_checkbox_sign()
    except NoSuchElementException:
        pass
    else:
        raise AssertionError('Выбор чекбокса не снят')

    page.remember_checkbox.click()
    assert page.remember_checkbox_sign(), 'Чекбокс не выбран'


@pytest.mark.func
def test_forgot_password(driver):

    page = AuthPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Авторизация'

    page.forgot_password.click()
    assert page.header_input().get_attribute('innerText') == 'Восстановление пароля'


@pytest.mark.func
def test_auth_btn(driver):

    page = AuthPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Авторизация'

    assert page.user_data_placeholder().text == 'Мобильный телефон'
    page.auth_btn.click()
    assert page.user_data_error().text == 'Введите номер телефона'


@pytest.mark.func
def test_auth_policy(driver):

    page = AuthPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Авторизация'

    page.auth_policy.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(NewPage.Header_Page))
    window_before, window_after = page.driver.window_handles[0], page.driver.window_handles[1]
    page.driver.switch_to.window(window_after)
    assert page.header_new_page().get_attribute('innerText').find('соглашени') != -1, \
        'Открылась страница не о Пользовательском соглашении'
    page.driver.close()
    page.driver.switch_to.window(window_before)


@pytest.mark.func
def test_social_login_links(driver):

    page = AuthPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Авторизация'

    page.link_vk.click()
    assert page.get_netloc_url() == 'id.vk.com'
    page = AuthPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Авторизация'

    page.link_ok.click()
    assert page.get_netloc_url() == 'connect.ok.ru'
    page = AuthPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Авторизация'

    page.link_mail.click()
    assert page.get_netloc_url() == 'connect.mail.ru'
    page = AuthPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Авторизация'


@pytest.mark.func
def test_registration_btn(driver):

    page = AuthPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Авторизация'

    page.registration_btn.click()
    assert page.header_input().get_attribute('innerText') == 'Регистрация'
