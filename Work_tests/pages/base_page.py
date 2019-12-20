import Locators
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():

    # Constructor for driver and url
    def __init__(self, browser, url, timeout=20):
        self.browser: WebDriver = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.browser.maximize_window()

    # Waiting for loading-element dissapearing
    def waiting_loading_element(self, browser, wait_timeout=5):
        try:
            browser.implicitly_wait(wait_timeout)
            WebDriverWait(browser, 5).until(ec.staleness_of(browser.find_element(By.ID, 'loading')))
            browser.implicitly_wait(wait_timeout)
        except NoSuchElementException:
            browser.implicitly_wait(wait_timeout)
            pass

        except TimeoutException:
            browser.implicitly_wait(wait_timeout)
            print('Timeout exceptions while loading')

    # Open testing site
    def open_url_page(self):
        self.browser.get(self.url)

    # Log in to site
    def login_to_site(self, username, password):
        # Input username to user field
        user_input = self.browser.find_element(*Locators.Login.LOGIN_FIELD)
        user_input.send_keys(username)
        self.waiting_loading_element(self.browser)

        # input password
        password_input = self.browser.find_element(*Locators.Login.PASSWORD_FIELD)
        password_input.send_keys(password)
        self.waiting_loading_element(self.browser)

        # Submit button
        login_button = self.browser.find_element(*Locators.Login.SUBMIT_LOGIN)
        login_button.click()
        self.waiting_loading_element(self.browser)

        # If user exist in system yet
        try:
            self.waiting_loading_element(self.browser)
            WebDriverWait(self.browser, 6).until(ec.element_to_be_clickable((Locators.Login.CONTINUE_LOGIN)))
            time.sleep(5)
            button_continue = self.browser.find_element(*Locators.Login.CONTINUE_LOGIN)
            self.waiting_loading_element(self.browser)
            button_continue.click()
        except (NoSuchElementException, TimeoutException):
            print('Continue button is not appear')
            pass


