from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    # Конструктор метод для экземпляра драйвера и адрес сайта
    def __init__(self, browser, url, timeout=10):
        self.browser: WebDriver = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Открытие нужного адреса сайта
    def open(self):
        self.browser.get(self.url)

    # Перехват исключений
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True