from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

# * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать

class MainPage(BasePage):

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"