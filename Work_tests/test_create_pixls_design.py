import pytest
import allure
from allure_commons.types import AttachmentType
from pages.base_page import BasePage
from pages.main_menu_page import MainMenuPage

__author__ = 'ichistov'

url = 'https://piexpertonline.power.com/site/login'
username = 'pietest0066@piexpert.com'
password = '@piexpert'
inno3_block = ['InnoSwitch3-CE Flyback', 'InnoSwitch3-CP Flyback', 'InnoSwitch3-EP Flyback', 'InnoSwitch3-Pro Flyback']

@allure.feature('Create Inno3_CE pixls design')
def test_create_inno3_CE_pixls(browser):
    """
    Creating Inno3-CE design and compare spreadsheet name
    """
    # Start browser and webdriver and go to link
    start_page = BasePage(browser, url)
    start_page.open_url_page()
    start_page.waiting_loading_element(browser)
    # Login to site.
    start_page.login_to_site(username, password)
    start_page.waiting_loading_element(browser)
    # Create new pixls design
    main_menu_page = MainMenuPage(browser, url)
    main_menu_page.create_pixls_design(inno3_block[0])
    start_page.waiting_loading_element(browser)

#@pytest.mark.skip
@allure.feature('Create Inno3_CP pixls design')
def test_create_inno3_CP_pixls(browser):
    """
        Creating Inno3-CP design and compare spreadsheet name
        """
    # Start browser and webdriver and go to link
    start_page = BasePage(browser, url)
    start_page.open_url_page()
    start_page.waiting_loading_element(browser)
    # Login to site.
    start_page.login_to_site(username, password)
    start_page.waiting_loading_element(browser)
    # Create new pixls design
    main_menu_page = MainMenuPage(browser, url)
    main_menu_page.create_pixls_design(inno3_block[1])
    start_page.waiting_loading_element(browser)

@allure.feature('Create Inno3_EP pixls design')
def test_create_inno3_EP_pixls(browser):
    """
        Creating Inno3-EP design and compare spreadsheet name
        """
    # Start browser and webdriver and go to link
    start_page = BasePage(browser, url)
    start_page.open_url_page()
    start_page.waiting_loading_element(browser)
    # Login to site.
    start_page.login_to_site(username, password)
    start_page.waiting_loading_element(browser)
    # Create new pixls design
    main_menu_page = MainMenuPage(browser, url)
    main_menu_page.create_pixls_design(inno3_block[2])
    start_page.waiting_loading_element(browser)

@allure.feature('Create Inno3_Pro pixls design')
def test_create_inno3_Pro_pixls(browser):
    """
        Creating Inno3-Pro design and compare spreadsheet name
        """
    # Start browser and webdriver and go to link
    start_page = BasePage(browser, url)
    start_page.open_url_page()
    start_page.waiting_loading_element(browser)
    # Login to site.
    start_page.login_to_site(username, password)
    start_page.waiting_loading_element(browser)
    # Create new pixls design
    main_menu_page = MainMenuPage(browser, url)
    main_menu_page.create_pixls_design(inno3_block[3])
    start_page.waiting_loading_element(browser)