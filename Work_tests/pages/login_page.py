import Locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()

    # Correct url-address
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'User see wrong url link'

    def user_should_be_logged_to_site(self):
        assert 'Logout' in self.browser.find_element(*Locators.Logout.LOGOUT).text, "User isn't log in"