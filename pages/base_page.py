from urllib.parse import urlparse
from datetime import datetime


class BasePage(object):
    # конструктор класса - специальный метод с ключевым словом __init__
    # Нам нужны объект веб-драйвера, адрес страницы и время ожидания элементов

    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def get_netloc_url(self):
        url = urlparse(self.driver.current_url)
        return url.netloc

    def come_back(self):
        self.driver.back()

    def create_screenshot_bag(self, name_test):
        name_screenshot = 'screenshots/' + name_test + '_' + \
                          str(datetime.now()).replace(' ', '_').replace(':', '-').replace('.', '-')[0:21] + '.png'
        self.driver.save_screenshot(name_screenshot)
        index = name_screenshot.rfind('%')
        return name_screenshot[index + 1:]
