Итоговый проект по автоматизации тестирования.
Объект тестирования: страницы входа в Личный кабинет сайта ПАО "Ростелеком".
В проекте тестируется UI объекта. Выполняется 60 автотестов.

Проект реализован без использования готовых библиотек для полного понимания всех особенностей написания кода.

Проект реализован с использованием паттерна PageObject основным преимуществом которого является удобство обновления кода
 при изменениии объекта тестирования.
Код проекта написан по методологии Объектно-ориентированного-программирования (ООП).

Область тестирования: страницы с формами "Авторизация" (с помощью номера телефона/почты/логина/номера лицевого счета),
 "Восстановление пароля", "Регистрация".
Страницы "Авторизация по коду", "Ввод кода подтверждения" не тестируются, т.к. требуют создания действующего аккаунта клиента "Ростелеком".

Проводится функциональное тестирование всех элементов области тестирования, как постоянных, так и открывающихся по ходу тестирования 
(сообщения об ошибках, выпадающие меню, тултипы и т.д.).

Тесты написаны с использованием техники серого ящика, подразумевающей частичное знание внутреннего устройства объекта (HTML-код).

Наборы предварительно подготовленных данных для параметризации тестов созданы с использование таких техник тестдизайна,
как разбиение на классы эквивалентности и граничные значения.

Структура проекта:
- в директориии pages находятся объекты области тестирования в виде классов страниц, наследующие от базового класса страницы BasePage 
и класса общих элементов CommonPageElements (присутствующих на нескольких страницах), а так же локаторы всех элементов;
- в директории prepare находятся предварительно подготовленные данные;
- в директориию screenshots сохраняются скриншоты дефектов;
- в директории tests находятся тесты каждой страницы, тесты общих элементов реализованы в виде отдельных функций в common_to_multiple_pages
 к которым обращаются тесты конкретной страницы.
- в корне проекта: chromedriver.exe(Chrome 114), conftest(с фикстурой получения имени теста), pytest.ini(с регистрацией маркеров)
 и requirement.txt(зависимости).

Команды для запуска в виде комментария, в начале каждого тестового файла.
