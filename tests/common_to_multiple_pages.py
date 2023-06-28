import pytest

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import NewPage, InputContainerLocators
from prepare.for_common_elem import DataInput


def page_structure(test_name, page):
    """ Функция проверяет наличие на странице: шапки, левой и правой секций, подвала,
    т.к. баг определяется визуално - создание скриншота, в случае ошибки"""
    bag = False
    name_screen = ''
    try:
        # последовательное обращение к id шапки, левой и правой секций, подвала страницы
        page.app_header_id()
        page.left_section_id()
        page.right_section_id()
        page.footer_id()
    except NoSuchElementException:  # перехват исключения при отсутствии какого-либо элемента страницы
        bag = True
        name_screen = page.create_screenshot_bag(test_name)  # сохранение скриншота
    if bag:
        raise AssertionError(f'Скриншот бага в файле: {name_screen}')  # имя скриншота в комментарии


def header_page(test_name, page):
    """ Функция проверяет наличие шапки страницы и логотипа в ней,
    т.к. баг определяется визуално - создание скриншота, в случае ошибки"""
    bag = False
    name_screen = ''
    try:
        page.app_header_id()
        assert page.header_logo().get_attribute('class') == 'rt-logo main-header__logo'
    except NoSuchElementException:  # перехват исключения при отсутствии шапки страницы
        bag = True
        name_screen = page.create_screenshot_bag(test_name)
    except AssertionError:  # перехват исключения при отсутствии логотипа в шапке
        bag = True
        name_screen = page.create_screenshot_bag(test_name)  # сохранение скриншота
    if bag:
        raise AssertionError(f'Скриншот бага в файле: {name_screen}')  # имя скриншота в комментарии


def left_section_page(test_name, page):
    """ Функция проверяет наличие левой секции страницы и логотипа, заголовка и продуктового слогана в ней,
    т.к. баг определяется визуално - создание скриншота, в случае ошибки"""
    bag = False
    name_screen = ''
    try:
        page.left_section_id()  # обращение к левой секции
        page.left_container_logo()  # обращение к логотипу
        assert page.left_title().text == 'Личный кабинет'  # проверка заголовка
        # проверка продуктового слогана
        assert page.left_desc().text == 'Персональный помощник в цифровом мире Ростелекома'
    except NoSuchElementException:  # перехват исключения при отсутствии левой секции или логотипа
        bag = True
        name_screen = page.create_screenshot_bag(test_name)
    except AssertionError:  # перехват исключения при несоответствии заголовка или продуктового слогана
        bag = True
        name_screen = page.create_screenshot_bag(test_name)  # сохранение скриншота
    if bag:
        raise AssertionError(f'Скриншот бага в файле: {name_screen}')  # имя скриншота в комментарии


def right_section_page(test_name, page):
    """ Функция проверяет наличие правой секции страницы и заголовка в ней,
    т.к. баг определяется визуално - создание скриншота, в случае ошибки"""
    bag = False
    name_screen = ''
    try:
        page.right_section_id()  # обращение к правой секции
        # проверка заголовка
        assert page.header_input().get_attribute('innerText') == "Авторизация" or "Восстановление пароля" \
               or "Регистрация"
    except NoSuchElementException:  # перехват исключения при отсутствии правой секции
        bag = True
        name_screen = page.create_screenshot_bag(test_name)
    except AssertionError:  # перехват исключения при несоответствии заголовка
        bag = True
        name_screen = page.create_screenshot_bag(test_name)  # сохранение скриншота
    if bag:
        raise AssertionError(f'Скриншот бага в файле: {name_screen}')  # имя скриншота в комментарии


def footer_page(page, driver):
    """ Функция проверяет информацию в подвале страницы и переходы по ссылкам"""
    # проверка информации в подвале страницы
    assert page.footer_copyright().text == '© 2023 ПАО «Ростелеком». 18+'
    assert page.footer_title_phone_support().get_attribute('innerText') == 'Служба поддержки\n8 800 100 0 800'
    assert page.footer_links_item().get_attribute('innerText') == \
           'Продолжая использовать наш сайт, вы даете согласие на обработку файлов \nCookies\n и других ' \
           'пользовательских данных, в соответствии с Политикой конфиденциальности и Пользовательским соглашением'

    page.footer_link_cookie().click()
    try:
        page.footer_cookie_tooltip()  # открытие тултипа
    except NoSuchElementException:
        raise AssertionError('Не открылся тултип, после нажатия на "Cookie"')
    # проверка информации в тултипе
    assert page.footer_cookie_tooltip_title().text == 'Мы используем Cookie', 'Несоответствие текста'
    assert page.footer_cookie_tooltip_desc()[0].get_attribute('innerText') == \
           'Ку́ки (англ. cookie) — небольшой фрагмент данных, отправленный веб-сервером и хранимый на компьютере ' \
           'пользователя. Веб-клиент (обычно веб-браузер) всякий раз при попытке открыть страницу соответствующего ' \
           'сайта пересылает этот фрагмент данных веб-серверу в составе HTTP-запроса.', 'Несоответствие текста'
    assert page.footer_cookie_tooltip_desc()[1].get_attribute('innerText') == \
           'Большинство современных браузеров позволяет пользователям выбрать — принимать куки или нет, но их ' \
           'отключение делает невозможной корректную работу с нашим сайтом.', 'Несоответствие текста'

    # закрытие тултипа и проверка этого
    page.footer_cookie_tooltip_close().click()
    try:
        page.footer_cookie_tooltip()
    except NoSuchElementException:
        pass
    else:
        raise AssertionError('Не закрылся тултип, после нажатия на "Х"')

    # проверка текста ссылок
    assert page.footer_link_agreements()[0].get_attribute('innerText') == 'Политикой конфиденциальности ', \
        'Несоответствие текста'
    assert page.footer_link_agreements()[1].get_attribute('innerText') == 'Пользовательским соглашением', \
        'Несоответствие текста'

    # проверка перехода по внешней ссылке о Пользовательском соглашении
    page.footer_link_agreements()[1].click()
    # явное ожидание открытия новой страницы
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(NewPage.Header_Page))
    # получение идентификаторов открытых окон
    window_before, window_after = page.driver.window_handles[0], page.driver.window_handles[1]
    page.driver.switch_to.window(window_after)  # переключение на новое окно
    # проверка заголовка нового окна
    assert page.header_new_page().get_attribute('innerText').find('соглашени') != -1, \
        'Открылась страница не о Пользовательском соглашении'
    page.driver.close()  # закрытие нового окна
    page.driver.switch_to.window(window_before)  # переключение на первоначальное окно

    # проверка перехода по внешней ссылке о Политике конфиденциальности
    page.footer_link_agreements()[0].click()
    # явное ожидание открытия новой страницы
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(NewPage.Header_Page))
    # получение идентификаторов открытых окон
    window_before, window_after = page.driver.window_handles[0], page.driver.window_handles[1]
    page.driver.switch_to.window(window_after)  # переключение на новое окно
    # проверка заголовка нового окна
    assert page.header_new_page().get_attribute('innerText').find('политик') != -1 or \
           page.header_new_page().get_attribute('innerText').find('Политик') != -1, \
            'Открылась страница не о Политике конфиденциальности'
    page.driver.close()  # закрытие нового окна
    page.driver.switch_to.window(window_before)  # переключение на первоначальное окно


def input_container_choice_tab(test_name, page, driver):
    """ Функция проверяет переключения табов аутентификации поля ввода данных пользователя,
    т.к. баги определяются визуално - создание скриншотов, в случае ошибок"""
    # проверка нахождения на страницах, где присутсвует поле ввода данных пользователя
    assert page.header_input().get_attribute('innerText') == "Авторизация" or "Восстановление пароля"
    count_bags = 0
    screenshot_bags = ''

    choice_item('mail', page)  # выбор таба Почта
    # явное ожидание переключения вида данных
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value(InputContainerLocators.Tab_Type, 'EMAIL'))

    try:  # проверка переключения на аутентификацию Электронная почта
        assert page.user_data_placeholder().text == 'Электронная почта'
    except AssertionError:  # перехват исключения, если переключения не произошло
        count_bags += 1
        name_screen = page.create_screenshot_bag(test_name)  # сохранение скриншота
        if count_bags == 1:
            screenshot_bags = name_screen

    choice_item('login', page)  # выбор таба Логин
    # явное ожидание переключения вида данных
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value(InputContainerLocators.Tab_Type, 'LOGIN'))

    try:  # проверка переключения на аутентификацию Логин
        assert page.user_data_placeholder().text == 'Логин'
    except AssertionError:  # перехват исключения, если переключения не произошло
        count_bags += 1
        name_screen = page.create_screenshot_bag(test_name)  # сохранение скриншота
        if count_bags == 1:
            screenshot_bags = name_screen

    choice_item('LS', page)  # выбор таба Лицевой счет
    # явное ожидание переключения вида данных
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value(InputContainerLocators.Tab_Type, 'LS'))

    try:  # проверка переключения на аутентификацию Лицевой счет
        assert page.user_data_placeholder().text == 'Лицевой счёт'
    except AssertionError:  # перехват исключения, если переключения не произошло
        count_bags += 1
        name_screen = page.create_screenshot_bag(test_name)  # сохранение скриншота
        if count_bags == 1:
            screenshot_bags = name_screen

    choice_item('phone', page)  # выбор таба Телефон
    # явное ожидание переключения вида данных
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value(InputContainerLocators.Tab_Type, 'PHONE'))

    try:  # проверка переключения на аутентификацию Мобильный телефон
        assert page.user_data_placeholder().text == 'Мобильный телефон'
    except AssertionError:  # перехват исключения, если переключения не произошло
        count_bags += 1
        name_screen = page.create_screenshot_bag(test_name)  # сохранение скриншота
        if count_bags == 1:
            screenshot_bags = name_screen

    # т.к. багов м.б. несколько и все имена не поместятся в комментарии, то формируем сообщение о кол-ве и первом адресе
    if count_bags != 0:
        raise AssertionError(f'Скриншот(ы) бага(ов) в {count_bags} файле(ах), начиная с: {screenshot_bags}')


def input_container_auto_select_tab(page):
    """ Функция проверяет автоматическое переключения табов аутентификации поля ввода данных пользователя"""
    # проверка нахождения на страницах, где присутсвует поле ввода данных пользователя
    assert page.header_input().get_attribute('innerText') == "Авторизация" or "Восстановление пароля"

    # параметризация данных в виде цикла, т.к. параметризация фикстурой существенно замедляет тестирования
    # из-за многократного открытия страницы
    for i in range(len(DataInput.auto_select)):
        # получение из подготовленных данных начального таба, данных ввода и ожидаемого таба после автопереключения
        tab, data, exception_tab = DataInput.auto_select[i]

        choice_item(tab, page)  # выбор первоначального таба
        page.user_data_input().send_keys(data)  # ввод данных
        page.header_input().click()  # клик на другой элемент для срабатывания автопереключения

        # проверка автопереключения таба аутентификации
        assert page.tab_type().get_attribute('value') == exception_tab, \
            f'Нет ожидаемого переключения таба из {tab} в {exception_tab}, при вводе {data}.'


def input_container_auto_substitution_phone(page):
    """ Функция проверяет автоматическую подстановку телефонных кодов (7-Россия и 375-Белоруссия)
    при вводе номера телефона"""
    # проверка нахождения на страницах, где присутсвует поле ввода данных пользователя
    assert page.header_input().get_attribute('innerText') == "Авторизация" or "Восстановление пароля"

    choice_item('phone', page)  # выбор таба Телефон
    # проверка переключения на аутентификацию Телефон
    assert page.user_data_placeholder().text == 'Мобильный телефон', 'Нет переключения на таб Мобильный телефон'

    # параметризация данных в виде цикла, т.к. параметризация фикстурой существенно замедляет тестирования
    # из-за многократного открытия страницы
    for number in DataInput.auto_substitution:
        page.user_data_input().send_keys(number)  # ввод номера

        if not number.startswith('3'):  # если первая цифра номера не тройка (375-Белоруссия)
            # автоподстановка кода России 7 на первую позицию
            assert page.user_data_text().get_attribute('value')[0] == '7', \
                'Нет автоподстановки кода России 7 на первую позицию'
        else:  # если первая цифра номера тройка (375-Белоруссия)
            if number == '3' or number == '37':
                # при вводе только 3 или 37 автоподстановка еще не производится
                assert page.user_data_text().get_attribute('value') == '3' \
                       or page.user_data_text().get_attribute('value') == '37'
            else:
                # при вводе 3 и любой кроме 7 - автоподстановка кода 375 на первую позицию
                assert page.user_data_text().get_attribute('value').find('375') == 0, \
                    'Нет автоподстановки кода Белоруссии 375 на первую позицию'

        page.user_data_input().click()  # установка курсора в конец номера
        # очистка поля ввода с учетом максимального кол-ва цифр (Белоруссия), после форматирования номера
        clear_text(page.user_data_input(), 15)


def input_container_phone_number_error(page):
    """ Функция проверяет сообщение об ошибке при вводе недостаточного кол-ва цифр номера телефона"""
    # проверка нахождения на страницах, где присутсвует поле ввода данных пользователя
    assert page.header_input().get_attribute('innerText') == "Авторизация" or "Восстановление пароля"
    # получение заранее подготовленных данных
    data = DataInput.phone_number_formatting

    choice_item('phone', page)  # выбор таба Телефон
    assert page.tab_type().get_attribute('value') == 'PHONE', 'Нет переключения на таб Мобильный телефон'

    # параметризация данных в виде цикла, т.к. параметризация фикстурой существенно замедляет тестирования
    # из-за многократного открытия страницы
    for number in data:
        page.user_data_input().send_keys(number)  # ввод номера
        page.header_input().click()  # клик на сторонний элемент для валидации введенного номера

        # проверка недостаточности кол-ва введенных цифр номера, с учетом автоподстановки кодов Росии и Белоруссии
        if ((number.startswith('7') or number.startswith('8')) and len(number) < 11) \
                or (number.startswith('375') and len(number) < 12) \
                or ((number.startswith('37') or number.startswith('35')) and len(number) < 11) \
                or (number.startswith('3') and len(number) < 10) \
                or ((number[0] != 3 and number[0] != 7 and number[0] != 8) and len(number)) < 10:
            # проверка наличия сообщения об ошибке при недостаточности кол-ва введенных цифр номера
            assert page.user_data_error().text == 'Неверный формат телефона', \
                'Текст сообщения об ошибке не соответствует ожидаемому'

        page.user_data_input().click()  # установка курсора в конец номера
        # очистка поля ввода с учетом максимального кол-ва цифр (Белоруссия), после форматирования номера
        clear_text(page.user_data_input(), 15)


def input_container_lower_name_email(page):
    """ Функция проверяет перевод вводимых букв в нижний регистр при вводе адреса электронной почты"""
    # проверка нахождения на страницах, где присутсвует поле ввода данных пользователя
    assert page.header_input().get_attribute('innerText') == "Авторизация" or "Восстановление пароля"
    # получение заранее подготовленных данных
    data = DataInput.email_address_lower

    choice_item('mail', page)  # выбор таба Почта
    assert page.user_data_placeholder().text == 'Электронная почта', 'Нет переключения на таб Электронная почта'

    # параметризация данных в виде цикла, т.к. параметризация фикстурой существенно замедляет тестирования
    # из-за многократного открытия страницы
    for address in data:
        page.user_data_input().send_keys(address)  # ввод адреса
        # page.header_input().click()
        # проверка ввода букв в нижнем регистре при вводе адреса электронной почты
        assert page.user_data_text().get_attribute('value') == address.lower(), 'Не вводятся буквы в нижнем регистре'

        clear_text(page.user_data_input(), len(address))  # очистка поля ввода


def input_container_login(page):
    """ Функция проверяет ввод букв с учетом регистра при вводе логина"""
    # проверка нахождения на страницах, где присутсвует поле ввода данных пользователя
    assert page.header_input().get_attribute('innerText') == "Авторизация" or "Восстановление пароля"

    # получение заранее подготовленных данных
    data = DataInput.login_data

    choice_item('login', page)  # выбор таба Логин
    assert page.user_data_placeholder().text == 'Логин', 'Нет переключения на таб Электронная почта'

    # параметризация данных в виде цикла, т.к. параметризация фикстурой существенно замедляет тестирования
    # из-за многократного открытия страницы
    for login in data:
        page.user_data_input().send_keys(login)  # ввод логина
        # проверка ввода букв с учетом регистра при вводе логина
        assert page.user_data_text().get_attribute('value') == login, \
            f'При вводе логина: "{login}", не вводятся заглавные буквы: ' \
            f'"{page.user_data_text().get_attribute("value")}"'

        clear_text(page.user_data_input(), len(login))  # очистка поля ввода


def input_container_LS(page):
    """ Функция проверяет, что при вводе номера лицевого счета, иные символы кроме цифр
    и числа длиной более 12 цифр не принимаются, при длине номера менее 12 - сообщение об ошибке"""
    # проверка нахождения на страницах, где присутсвует поле ввода данных пользователя
    assert page.header_input().get_attribute('innerText') == "Авторизация" or "Восстановление пароля"
    # получение заранее подготовленных данных
    data = DataInput.check_data

    choice_item('LS', page)  # выбор таба Логин
    assert page.user_data_placeholder().text == 'Лицевой счёт', 'Нет переключения на таб Лицевой счёт'

    # параметризация данных в виде цикла, т.к. параметризация фикстурой существенно замедляет тестирования
    # из-за многократного открытия страницы
    for ls in data:
        page.user_data_input().send_keys(ls)  # ввод номера лицевого счета
        page.header_input().click()  # клик на сторонний элемент для валидации введенного номера лицевого счета
        if ls.isdigit():  # если номер состоит только из цифр
            if len(ls) > 12:  # при длине номера больше 12 цифр остальные цифры (больше 12) не вводятся
                assert page.user_data_text().get_attribute('value') == ls[:12], 'Вводится номер длиннее 12 цифр'
            elif len(ls) == 12:  # при длине номера 12 цифр номер принимается
                assert page.user_data_text().get_attribute('value') == ls, 'Ошибка ввода'
            else:   # при длине номера меньше 12 цифр - сообщение об ошибке
                assert page.user_data_text().get_attribute('value') == ls, 'Ошибка ввода'
                assert page.user_data_error().text == 'Проверьте, пожалуйста, номер лицевого счета', \
                    'Текст сообщения об ошибке не соответствует ожидаемому'
        else:   # в поле вводятся только цифры, другие символы игнорируются
            if len(line_cleaning(ls)) > 12:
                # при длине больше 12 цифр, после удаления других символов, остальные цифры (больше 12) не вводятся
                assert page.user_data_text().get_attribute('value') == line_cleaning(ls)[:12], \
                    'Вводится номер длиннее 12 цифр'
            elif len(line_cleaning(ls)) == 12:
                # при длине номера 12 цифр, после удаления других символов, номер принимается
                assert page.user_data_text().get_attribute('value') == line_cleaning(ls), 'Ошибка ввода'
            else:  # при длине номера меньше 12 цифр, после удаления других символов, - сообщение об ошибке
                assert page.user_data_text().get_attribute('value') == line_cleaning(ls), 'Ошибка ввода'
                assert page.user_data_error().text == 'Проверьте, пожалуйста, номер лицевого счета', \
                    'Текст сообщения об ошибке не соответствует ожидаемому'

        clear_text(page.user_data_input(), len(ls))  # очистка поля ввода


def choice_item(item, page):
    # выбор таба аутентификации
    """ """
    if item == 'phone':
        page.phone_tab().click()
    elif item == 'mail':
        page.mail_tab().click()
    elif item == 'login':
        page.login_tab().click()
    elif item == 'LS':
        page.LS_tab().click()
    else:
        raise 'Некорректное название таба'


def get_attributes(element, driver) -> dict:
    # получение всех атрибутов элемента
    return driver.execute_script(
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


def right_border_text(elem, len_text):
    # перевод курсора в конец данных в поле, для длинных данных, превышающих показываемое полем количество символов
    for i in range(len_text):
        elem.send_keys(Keys.ARROW_RIGHT)


def clear_text(elem, len_text):
    #  очистка поля ввода
    for i in range(len_text):
        elem.send_keys(Keys.BACKSPACE)


def line_cleaning(line):
    # удаление всех символов, кроме цифр
    line_clean = ''
    for i in range(len(line)):
        if line[i] in '1234567890':
            line_clean = line_clean + line[i]
    return line_clean
