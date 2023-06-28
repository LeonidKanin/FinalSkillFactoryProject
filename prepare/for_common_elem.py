# from pages.auth_page import AuthPage
# from pages.recovery_page import RecoveryPage
# from pages.registration_page import RegistrationPage


# class PagesForParameterization:
#     pages_for_parameterization = [AuthPage, RecoveryPage, RegistrationPage]
#
#     pages_for_parameterization_with_header = [(AuthPage, 'Авторизация'), (RecoveryPage, 'Восстановление пароля'),
#                                               (RegistrationPage, 'Регистрация')]
#
#     pages_for_input_container_parameterization = [AuthPage, RecoveryPage]
#
#     pages_for_link_auth_policy_parametrization = [AuthPage, RegistrationPage]


class DataInput:
    auto_select = [
        # данные для проверки автовыбора таба при активном табе Телефон
        # автопереключения на таб Личный счет нет, т.к. любое кол-во цифр форматируются в телефонный номер
        ['phone', 'fDsgF15652', 'LOGIN'], ['phone', 'плоПРПЛР13№;:*"', 'LOGIN'], ['phone', '!@#$%^&*)_+;:><~', 'LOGIN'],
        ['phone', 'Ga@ga.Ga', 'EMAIL'], ['phone', 'Ga@ga.Ga.gf', 'EMAIL'],

        # данные для проверки автовыбора таба при активном табе Почта
        ['mail', 'плоПРЛ13№;:*"', 'LOGIN'], ['mail', 'Ga@ga.Ga.3636.', 'LOGIN'], ['mail', '!@#$%^&*)_+;:><~', 'LOGIN'],
        ['mail', '79998887766', 'PHONE'], ['mail', '89998887766', 'PHONE'],
        ['mail', '375999888777', 'LS'],

        # данные для проверки автовыбора таба при активном табе Логин
        # автопереключения на таб Телефон нет, т.к. любое кол-во цифр кроме 12 воспринимается как логин
        ['login', 'Ga@ga.Ga', 'EMAIL'], ['login', 'Ga@ga.Ga.gf', 'EMAIL'],
        ['login', '375999888777', 'LS'],

        # автопереключения при активном табе Личный счет нет, т.к. символы кроме цифр не вводятся
    ]

    auto_substitution = [
        # данные для проверки автоподстановки в номере телефона: "375" при вводе первого числа "3"
        # и "7" при вводе любого числа, кроме "3"
        '3', '37', '31', '35', '374', '359', '3549841877798798465165498454959854116518', '8',
        '12', '234', '4567', '56789', '678901', '91234567', '54984251954951954195195419851959814'
    ]

    phone_number_formatting = [
        # данные для проверки сообщения об ошибке при вводе недостаточного количества цифр
        '7111111111', '8222222222', '37511111111', '3722222222', '3533333333', '344444444', '123456789', '213456789',
        '412356789', '512346789', '612345789', '912345678', '0', '12345'
    ]

    email_address_lower = ['GA@GA.GA', 'aG@asDf.HGFhgf', 'HG123@gHGh78687.kjhHhjgg']

    login_data = ['1254375437', 'dfgf4524#^&&(*&8@$#*^', 'оавып1564екнншщзж56"№;%::??', 'TeSt']

    check_data = ['0', '01', '123456789', '123456789000', '1234567890001234566', '0fj2BH3@#$%45роп6РОП7',
                  'ad1UG2@#%$345роп67890РНПЛОЗ123456']


class InputWithoutRestrictions:
    # слово длиной 567 символов с английскими и русскими, заглавными и строчными буквами, цифрами и спецсимволами
    input_data = '14jYuZsGlJjYxOYdPTJebhuJgGgWuaYBpUbxEtxKEhGtXiuBkyCIufWQqTAbaXlAQzaZOEvvxRgGaMKTFLduRaouihOuXjxHq' \
                 'PXqbjzkjPSCYbtFaqiDBnzNcJymvCsPTAEWlFBofUqdhmSpOihjBumquPfqWXkmEUSvsXGQAVBwZZsSXsXQYnYPrCbCGoZRoJ' \
                 'IBOgSRJpePQWGBlPCnrIlkOdYobRLcXFgbwxRmwySAvfHLiBVyhIudSNenbvyjzZxraJzMKupefOTeKoNiIiAfiEKIejvoABM' \
                 'dFYcUWsibgfmcsDnExHGpozUFTetzoCTSdTGckvgJicwngwV7EKIoBeGuYLCouOGOSZWMSPpPFCVSagjiXZIayxvZVWkdomVw' \
                 'MjxvOxpCotcTxAsVdQSTEujFqccMxVtWQayFdFDrDOrWMsRLymSNYлопгекРШГш64нагол737смщлррорШПЕЩШп@#$%^&*(<>!~'
