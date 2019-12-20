import pytest
from pages.login_page import LoginPage
from pages.base_page import BasePage

url = 'https://piexpertonline.power.com/site/login'
username = 'pietest0066@piexpert.com'
password = '@piexpert'

@pytest.mark.skip
def test_user_open_login_page(browser):
    """
    Open target site and checking current url
    """
    start_page = BasePage(browser, url)
    start_page.open_url_page()
    login_page = LoginPage(browser, url)
    login_page.should_be_login_url()

def test_user_logged_in_to_site(browser):
    """
    User open target site and login. Logout button is visible.
    """
    start_page = BasePage(browser, url)
    start_page.open_url_page()
    start_page.waiting_loading_element(browser)
    # Login to site. Input username and password
    start_page.login_to_site(username, password)
    login_page = LoginPage(browser, url)
    start_page.waiting_loading_element(browser)
    login_page.user_should_be_logged_to_site()
