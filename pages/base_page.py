from selenium.webdriver.remote.webdriver import WebDriver

class BasePage():
    # Конструктор метод для экземпляра драйвера и адрес сайта
    def __init__(self, browser, url):
        self.browser: WebDriver = browser
        self.url = url
    # Открытие нужного адреса сайта
    def open(self):
        self.browser.get(self.url)