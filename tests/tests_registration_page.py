# команды для запуска в PyCharm
# """pytest -v --driver Chrome --driver-path chromedriver.exe tests/tests_registration_page.py"""
# """pytest -v -m 'negative' --driver Chrome --driver-path chromedriver.exe tests/tests_registration_page.py"""
# """pytest -v -m 'positive' --driver Chrome --driver-path chromedriver.exe tests/tests_registration_page.py"""
# """pytest -v -m 'func' --driver Chrome --driver-path chromedriver.exe tests/tests_registration_page.py"""
# """pytest -v -m 'script' --driver Chrome --driver-path chromedriver.exe tests/tests_registration_page.py"""

import pytest

from pages.locators import SelectRegionLocators
from pages.registration_page import RegistrationPage
from prepare.for_registration_page import *
from tests.common_to_multiple_pages import *


@pytest.mark.structure
def test_page_structure(name_test, driver):
    page_structure(name_test, RegistrationPage(driver))


@pytest.mark.structure
def test_header_page(name_test, driver):
    header_page(name_test, RegistrationPage(driver))


@pytest.mark.structure
def test_left_section_page(name_test, driver):
    left_section_page(name_test, RegistrationPage(driver))


@pytest.mark.structure
def test_right_section_page(name_test, driver):
    right_section_page(name_test, RegistrationPage(driver))


@pytest.mark.structure
@pytest.mark.func
def test_footer_page(driver):
    footer_page(RegistrationPage(driver), driver)


@pytest.mark.func
@pytest.mark.positive
def test_name_input_positive(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'
    assert page.name_placeholder.text == 'Имя'

    for name in NameInputTesting.positive_name:
        page.name_input.send_keys(name)
        page.surname_input.click()
        assert page.name_text.get_attribute('innerText').istitle() is True
        assert page.name_text.get_attribute('innerText') == name.title().strip()
        try:
            page.name_error()
        except NoSuchElementException:
            pass
        else:
            raise AssertionError(f'Выдается сообщение об ошибке при корректном вводе: {name}.')
        page.name_input.click()
        clear_text(page.name_input, len(name))


@pytest.mark.func
@pytest.mark.negative
def test_name_input_negative(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'
    assert page.name_placeholder.text == 'Имя'

    for name in NameInputTesting.negative_name:
        page.name_input.send_keys(name)
        page.surname_input.click()
        try:
            assert page.name_error().text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        except NoSuchElementException:
            raise AssertionError(f'Не выдается сообщение об ошибке при некорректном вводе: {name}.')

        page.name_input.click()
        clear_text(page.name_input, len(name))


@pytest.mark.func
@pytest.mark.positive
def test_surname_input_positive(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'
    assert page.surname_placeholder.text == 'Фамилия'

    for surname in NameInputTesting.positive_name:
        page.surname_input.send_keys(surname)
        page.name_input.click()
        assert page.surname_text.get_attribute('innerText').istitle() is True
        assert page.surname_text.get_attribute('innerText') == surname.title().strip()
        try:
            page.surname_error()
        except NoSuchElementException:
            pass
        else:
            raise AssertionError(f'Выдается сообщение об ошибке при корректном вводе: {surname}.')
        page.surname_input.click()
        clear_text(page.surname_input, len(surname))


@pytest.mark.func
@pytest.mark.negative
def test_surname_input_negative(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'
    assert page.surname_placeholder.text == 'Фамилия'

    for surname in NameInputTesting.negative_name:
        page.surname_input.send_keys(surname)
        page.name_input.click()
        try:
            assert page.surname_error().text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        except NoSuchElementException:
            raise AssertionError(f'Не выдается сообщение об ошибке при некорректном вводе: {surname}.')

        page.surname_input.click()
        clear_text(page.surname_input, len(surname))


@pytest.mark.func
@pytest.mark.positive
def test_region_dropdown(name_test, driver):
    """Выбор региона из выпадающего меню"""
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'

    count_bags = 0
    screenshot_bag = ''
    for subject in RegionTesting.list_subjects:
        page.region_input.click()
        page.region_input.send_keys(subject)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SelectRegionLocators.Select_Region))
        try:
            if len(page.select_region()) > 1:
                res = False
                for i in range(len(page.select_region()) - 1):
                    if page.select_region()[i].text == subject:
                        res = True
                        page.select_region()[i].click()
                assert res  #
            elif len(page.select_region()) == 1:
                assert page.select_region()[0].text.find(subject) != -1
                page.select_region()[0].click()
            else:
                raise Exception(f'Некоррректный ввод названия региона: {subject}')

        except AssertionError:
            count_bags += 1
            name_screen = page.create_screenshot_bag(name_test)
            if count_bags == 1:
                screenshot_bag = name_screen
        page.name_input.click()

    if count_bags != 0:
        raise AssertionError(f'Скриншот(ы) бага(ов) в {count_bags} файле(ах), начиная с: {screenshot_bag}')


@pytest.mark.func
@pytest.mark.positive
def test_mail_phone_input_positive(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'
    assert page.mail_phone_placeholder.text == 'E-mail или мобильный телефон'

    for data in MailPhoneInputTesting.positive_data:
        page.mail_phone_input.send_keys(data)
        page.pass_input().click()
        try:
            page.mail_phone_error()
        except NoSuchElementException:
            pass
        else:
            raise AssertionError(f'Выдается сообщение об ошибке при корректном вводе: {data}.')
        page.mail_phone_input.click()
        clear_text(page.mail_phone_input, len(data) + 5)


@pytest.mark.func
@pytest.mark.negative
def test_mail_phone_input_negative(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'
    assert page.mail_phone_placeholder.text == 'E-mail или мобильный телефон'

    for data in MailPhoneInputTesting.negative_data:
        page.mail_phone_input.send_keys(data)
        page.pass_input().click()
        try:
            assert page.mail_phone_error().text == \
                   'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
        except NoSuchElementException:
            raise AssertionError(f'Не выдается сообщение об ошибке при некорректном вводе: {data}.')
        page.mail_phone_input.click()
        clear_text(page.mail_phone_input, len(data) + 5)


@pytest.mark.func
@pytest.mark.positive
def test_password_input_positive(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'
    assert page.pass_placeholder().text == 'Пароль'

    assert page.pass_input().get_attribute('type') == 'password'
    page.pass_input_actions().click()
    assert page.pass_input().get_attribute('type') == 'text'

    for password in PasswordInputTesting.positive_pass:
        page.pass_input().send_keys(password)
        page.pass_confirm_input.click()

        try:
            page.password_error()
        except NoSuchElementException:
            pass
        else:
            raise AssertionError(f'Выдается сообщение об ошибке при корректном вводе: {password}.')

        page.pass_input().click()
        right_border_text(page.pass_input(), len(password))
        clear_text(page.pass_input(), len(password))

        assert page.pass_input_text().get_attribute('innerText') == ''


@pytest.mark.func
@pytest.mark.negative
def test_password_input_negative(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'
    assert page.pass_placeholder().text == 'Пароль'

    assert page.pass_input().get_attribute('type') == 'password'
    page.pass_input_actions().click()
    assert page.pass_input().get_attribute('type') == 'text'

    for password in PasswordInputTesting.negative_pass:
        page.pass_input().send_keys(password)
        page.pass_confirm_input.click()

        try:
            assert page.password_error().text == 'Длина пароля должна быть не менее 8 символов.' or \
                   'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' or \
                   'Пароль должен содержать только латинские буквы' or \
                   'Длина пароля должна быть не более 20 символов' or \
                   'Пароль должен содержать хотя бы одну заглавную букву'
        except NoSuchElementException:
            raise AssertionError(f'Не выдается сообщение об ошибке при некорректном вводе: {password}.')

        page.pass_input().click()
        right_border_text(page.pass_input(), len(password))
        clear_text(page.pass_input(), len(password))

        assert page.pass_input_text().get_attribute('innerText') == ''


@pytest.mark.func
@pytest.mark.positive
def test_password_confirm_input_positive(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'
    assert page.pass_confirm_placeholder.text == 'Подтверждение пароля'

    assert page.pass_confirm_input.get_attribute('type') == 'password'
    page.pass_confirm_input_action.click()
    assert page.pass_confirm_input.get_attribute('type') == 'text'

    for password in PasswordInputTesting.positive_pass:
        page.pass_confirm_input.send_keys(password)
        page.pass_input().click()

        try:
            page.password_confirm_error()
        except NoSuchElementException:
            pass
        else:
            raise AssertionError(f'Выдается сообщение об ошибке при корректном вводе: {password}.')
        page.pass_confirm_input.click()
        clear_text(page.pass_confirm_input, len(password))


@pytest.mark.func
@pytest.mark.negative
def test_password_confirm_input_negative(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'
    assert page.pass_confirm_placeholder.text == 'Подтверждение пароля'

    assert page.pass_confirm_input.get_attribute('type') == 'password'
    page.pass_confirm_input_action.click()
    assert page.pass_confirm_input.get_attribute('type') == 'text'

    for password in PasswordInputTesting.negative_pass:
        page.pass_confirm_input.send_keys(password)
        page.pass_input().click()
        try:
            assert page.password_confirm_error().text == 'Длина пароля должна быть не менее 8 символов.' or \
                   'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' or \
                   'Пароль должен содержать только латинские буквы' or \
                   'Длина пароля должна быть не более 20 символов' or \
                   'Пароль должен содержать хотя бы одну заглавную букву'
        except NoSuchElementException:
            raise AssertionError(f'Не выдается сообщение об ошибке при некорректном вводе: {password}.')

        page.pass_confirm_input.click()
        clear_text(page.pass_confirm_input, len(password))


@pytest.mark.script
@pytest.mark.positive
def test_registration_form_with_email_positive(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'

    page.name_input.send_keys('Иван')
    page.surname_input.send_keys('Иванов')

    page.region_input.click()
    page.region_input.send_keys('Кемеровская')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SelectRegionLocators.Select_Region))
    page.select_region()[0].click()

    page.mail_phone_input.send_keys('ga@ga.ga')
    page.pass_input().send_keys('Fa123456789')
    page.pass_confirm_input.send_keys('Fa123456789')

    page.register_btn.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(NewPage.Header_Page))
    assert page.header_new_page().text == 'Подтверждение email'


@pytest.mark.script
@pytest.mark.positive
def test_registration_form_with_phone(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'

    page.name_input.send_keys('Иван')
    page.surname_input.send_keys('Иванов')

    page.region_input.click()
    page.region_input.send_keys('Кемеровская')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SelectRegionLocators.Select_Region))
    page.select_region()[0].click()

    page.mail_phone_input.send_keys('+79059056666')
    page.pass_input().send_keys('Fa123456789')
    page.pass_confirm_input.send_keys('Fa123456789')

    page.register_btn.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(NewPage.Header_Page))
    assert page.header_new_page().text == 'Подтверждение телефона'


@pytest.mark.script
@pytest.mark.negative
def test_registration_form_with_different_passwords(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'

    page.name_input.send_keys('Иван')
    page.surname_input.send_keys('Иванов')

    page.region_input.click()
    page.region_input.send_keys('Кемеровская')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SelectRegionLocators.Select_Region))
    page.select_region()[0].click()

    page.mail_phone_input.send_keys('+79059056666')
    page.pass_input().send_keys('Fa123456789')
    page.pass_confirm_input.send_keys('Af123456789')

    page.register_btn.click()
    assert page.password_confirm_error().text == 'Пароли не совпадают'


@pytest.mark.script
@pytest.mark.negative
def test_registration_form_with_weak_password(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'

    page.name_input.send_keys('Иван')
    page.surname_input.send_keys('Иванов')

    page.region_input.click()
    page.region_input.send_keys('Кемеровская')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SelectRegionLocators.Select_Region))
    page.select_region()[0].click()

    page.mail_phone_input.send_keys('+79059056666')
    page.pass_input().send_keys('Aa123456789')
    page.pass_confirm_input.send_keys('Aa123456789')

    page.register_btn.click()
    assert page.form_error().text == 'Пароль ненадежный. Необходимо придумать более сложный пароль.'


@pytest.mark.script
@pytest.mark.negative
def test_registration_form_no_name(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'

    page.surname_input.send_keys('Иванов')

    page.region_input.click()
    page.region_input.send_keys('Кемеровская')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SelectRegionLocators.Select_Region))
    page.select_region()[0].click()

    page.mail_phone_input.send_keys('+79059056666')
    page.pass_input().send_keys('Aa123456789')
    page.pass_confirm_input.send_keys('Aa123456789')

    page.register_btn.click()
    assert page.name_error().text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


@pytest.mark.script
@pytest.mark.negative
def test_registration_form_no_surname(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'

    page.name_input.send_keys('Иван')

    page.region_input.click()
    page.region_input.send_keys('Кемеровская')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SelectRegionLocators.Select_Region))
    page.select_region()[0].click()

    page.mail_phone_input.send_keys('+79059056666')
    page.pass_input().send_keys('Aa123456789')
    page.pass_confirm_input.send_keys('Aa123456789')

    page.register_btn.click()
    assert page.surname_error().text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


@pytest.mark.script
@pytest.mark.negative
def test_registration_form_no_phone_mail(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'

    page.name_input.send_keys('Иван')
    page.surname_input.send_keys('Иванов')

    page.region_input.click()
    page.region_input.send_keys('Кемеровская')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SelectRegionLocators.Select_Region))
    page.select_region()[0].click()

    page.pass_input().send_keys('Aa123456789')
    page.pass_confirm_input.send_keys('Aa123456789')

    page.register_btn.click()
    assert page.mail_phone_error().text == \
           'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'


@pytest.mark.script
@pytest.mark.negative
def test_registration_form_no_password(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'

    page.name_input.send_keys('Иван')
    page.surname_input.send_keys('Иванов')

    page.region_input.click()
    page.region_input.send_keys('Кемеровская')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SelectRegionLocators.Select_Region))
    page.select_region()[0].click()

    page.mail_phone_input.send_keys('ga@ga.ga')
    page.pass_confirm_input.send_keys('Aa123456789')

    page.register_btn.click()
    assert page.password_error().text == 'Длина пароля должна быть не менее 8 символов'


@pytest.mark.script
@pytest.mark.negative
def test_registration_form_no_password_confirm(driver):
    page = RegistrationPage(driver)
    assert page.header_input().get_attribute('innerText') == 'Регистрация'

    page.name_input.send_keys('Иван')
    page.surname_input.send_keys('Иванов')

    page.region_input.click()
    page.region_input.send_keys('Московская')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SelectRegionLocators.Select_Region))
    page.select_region()[0].click()

    page.mail_phone_input.send_keys('ga@ga.ga')
    page.pass_input().send_keys('Aa123456789')

    page.register_btn.click()
    assert page.password_confirm_error().text == 'Длина пароля должна быть не менее 8 символов'
