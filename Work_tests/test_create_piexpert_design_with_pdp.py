import pytest
import allure
from allure_commons.types import AttachmentType
from pages.base_page import BasePage
from pages.main_menu_page import MainMenuPage

__author__ = 'ichistov'

url = 'https://piexpertonline.power.com/site/login'
username = 'pietest0066@piexpert.com'
password = '@piexpert'
designs_with_pdp = ['InnoSwitch3-CP Flyback', 'InnoSwitch3-Pro Flyback']

@allure.feature('Create Inno3-CP design without optimization')
@allure.severity('critical')
def test_create_piexpert_inno3_cp_no_optimize(browser):
    """
        Creating PIExpert Inno3-CP design without optimization
    """
    # Start browser and webdriver and go to link
    start_page = BasePage(browser, url)
    start_page.open_url_page()
    start_page.waiting_loading_element(browser)
    # Login to site.
    start_page.login_to_site(username, password)
    start_page.waiting_loading_element(browser)
    # Create new piexpert design
    main_menu_page = MainMenuPage(browser, url)
    main_menu_page.create_piexpert_design_with_pdp(designs_with_pdp[0], pdp=20, optimization=False)
    with allure.step('Take a screenshot after design created'):
        allure.attach(browser.get_screenshot_as_png(), name='Inno3-CP_no_optimize',
                      attachment_type=AttachmentType.PNG)

@allure.feature('Create Inno3-CP design with optimization')
@allure.severity('critical')
def test_create_piexpert_inno3_cp_with_optimize(browser):
    """
            Creating PIExpert Inno3-CP design with optimization
    """
    # Start browser and webdriver and go to link
    start_page = BasePage(browser, url)
    start_page.open_url_page()
    start_page.waiting_loading_element(browser)
    # Login to site.
    start_page.login_to_site(username, password)
    start_page.waiting_loading_element(browser)
    # Create new piexpert design
    main_menu_page = MainMenuPage(browser, url)
    main_menu_page.create_piexpert_design_with_pdp(designs_with_pdp[0], pdp=20, optimization=True)
    with allure.step('Take a screenshot after design created'):
        allure.attach(browser.get_screenshot_as_png(), name='Inno3-CP_optimize',
                      attachment_type=AttachmentType.PNG)

@allure.feature('Create Inno3-Pro design without optimization')
@allure.severity('critical')
def test_create_piexpert_inno3_pro_no_optimize(browser):
    """
        Creating PIExpert Inno3-Pro design without optimization
    """
    # Start browser and webdriver and go to link
    start_page = BasePage(browser, url)
    start_page.open_url_page()
    start_page.waiting_loading_element(browser)
    # Login to site.
    start_page.login_to_site(username, password)
    start_page.waiting_loading_element(browser)
    # Create new piexpert design
    main_menu_page = MainMenuPage(browser, url)
    main_menu_page.create_piexpert_design_with_pdp(designs_with_pdp[1], pdp=20, optimization=False)
    with allure.step('Take a screenshot after design created'):
        allure.attach(browser.get_screenshot_as_png(), name='Inno3-Pro_no_optimize',
                      attachment_type=AttachmentType.PNG)

@allure.feature('Create Inno3-Pro design with optimization')
@allure.severity('critical')
def test_create_piexpert_inno3_pro_with_optimize(browser):
    """
        Creating PIExpert Inno3-Pro design with optimization
    """
    # Start browser and webdriver and go to link
    start_page = BasePage(browser, url)
    start_page.open_url_page()
    start_page.waiting_loading_element(browser)
    # Login to site.
    start_page.login_to_site(username, password)
    start_page.waiting_loading_element(browser)
    # Create new piexpert design
    main_menu_page = MainMenuPage(browser, url)
    main_menu_page.create_piexpert_design_with_pdp(designs_with_pdp[1], pdp=20, optimization=True)
    with allure.step('Take a screenshot after design created'):
        allure.attach(browser.get_screenshot_as_png(), name='Inno3-Pro_optimize',
                      attachment_type=AttachmentType.PNG)