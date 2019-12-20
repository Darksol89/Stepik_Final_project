import time
import traceback
import Locators
import random
import os
import json
import argparse

from overload import *
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
screen = './screens/'+str(random.random())+'.png'

import Consts

__author__ = 'ichistov'
"""
# Config JSON file with path to browsers WebDriver
json_browser_config = r'browser_config.json'
try:
    with open(json_browser_config) as driver_config:
        json_data = json.load(driver_config)
except FileNotFoundError:
    print("JSON file wasn't found on specified location")
    exit(-1)

chrome_driver = json_data['chromeDriver']

# Possible CL arguments for parser
parser = argparse.ArgumentParser(add_help=True,
                                description='Arguments for script')
parser.add_argument('-chrm', '--chrome',
                        default=chrome_driver,
                        type=str,
                        help='path to Chrome WebDriver')

args = parser.parse_args()
"""

def set_up(browser='chrome', implicitly_wait_timeout=20, page_load_timeout=60, fp=None):
    """
    Setting up webdriver.

    :type browser: str
    :type implicitly_wait_timeout: float
    :type page_load_timeout: float
    :param fp: firefox profile address

    :return: WebDriver
    """
    if browser == 'firefox':
        driver = webdriver.Firefox(firefox_profile=fp)
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'ie':
        driver = webdriver.Ie()
    else:
        print("Wrong browser value passed in.")

    driver.implicitly_wait_timeout = implicitly_wait_timeout
    driver.implicitly_wait(implicitly_wait_timeout)
    driver.set_page_load_timeout(page_load_timeout)
    driver.maximize_window()

    return driver

def set_up_remote(browser='firefox', implicitly_wait_timeout=20, page_load_timeout=60, fp=None):
    """
    Setting up remote webdriver from Docker.

    :type browser: str
    :type implicitly_wait_timeout: float
    :type page_load_timeout: float

    :return: WebDriver
    """

    if browser == 'firefox':
        capabilities = {
            "browserName": "firefox",
            "version": "67.0",
            "enableVNC": True,
            "enableVideo": False
        }
        driver = webdriver.Remote(
            command_executor="http://192.168.50.106:4444/wd/hub",
            desired_capabilities=capabilities, browser_profile=fp)
    elif browser == 'chrome':
        capabilities = {
            "browserName": "chrome",
            "version": "76.0",
            "enableVNC": True,
            "enableVideo": False
        }
        driver = webdriver.Remote(
            command_executor="http://192.168.50.106:4444/wd/hub",
            desired_capabilities=capabilities)
    elif browser == 'opera':
        capabilities = {
            "browserName": "opera",
            "version": "62.0",
            "enableVNC": True,
            "enableVideo": False
        }
        driver = webdriver.Remote(
            command_executor="http://192.168.50.106:4444/wd/hub",
            desired_capabilities=capabilities)
    else:
        print("Wrong browser value passed in.")

    driver.implicitly_wait_timeout = implicitly_wait_timeout
    driver.implicitly_wait(implicitly_wait_timeout)
    driver.set_page_load_timeout(page_load_timeout)
    driver.maximize_window()

    return driver

def click(driver, locator, sleep_time=3, expl_wait=20):
    """
    Wait until element will be shown and clickable, then send 'click' to it.
    TimeoutException will be generated if something's wrong (NOT NoSuchElementException).

    :type driver: WebDriver
    :type locator: tuple
    :param sleep_time: delay before click
    :param expl_wait: explicit waiting time for presence of element will found
    :type sleep_time: float
    :type expl_wait: float
    """

    time.sleep(sleep_time)
    try:
        driver.implicitly_wait(5)
        WebDriverWait(driver, expl_wait, ignored_exceptions=StaleElementReferenceException).until(
            ec.presence_of_element_located(locator))
    except (NoSuchElementException, TimeoutException, ElementNotInteractableException, StaleElementReferenceException):
        # additional check were deleted, cause of some unexpected timeout exceptions on it
        driver.implicitly_wait(5)
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable(locator))
    wait_for_loading(driver)
    driver.find_element(*locator).click()
    wait_for_loading(driver)

def send_keys(driver, keys, locator, sleep_time=0):
    """
    Send keys to specified locator. Keys can mean str and/or Key-object.
    TimeoutException will be generated if something's wrong (NOT NoSuchElementException).

    :type driver: WebDriver
    :type keys: str
    :type locator: tuple
    :type sleep_time: float
    """

    (WebDriverWait(driver, 10, ignored_exceptions=StaleElementReferenceException).until
     (ec.presence_of_element_located(locator)))
    time.sleep(sleep_time)
    driver.find_element(*locator).send_keys(keys)


def clear(driver, locator, sleep_time=0):
    """
    Clear field by specified locator.
    TimeoutException will be generated if something's wrong (NOT NoSuchElementException).

    :type driver: WebDriver
    :type locator: tuple
    :type sleep_time: float
    """

    (WebDriverWait(driver, 10, ignored_exceptions=StaleElementReferenceException).until
     (ec.presence_of_element_located(locator)))
    time.sleep(sleep_time)
    driver.find_element(*locator).clear()


@overload
def hover_element(driver, elem: WebElement, sleep_time=0):
    """
    Hovering an element on specified locator.

    :type driver: WebDriver
    :type elem: WebElement
    :type sleep_time: float
    """

    time.sleep(sleep_time)
    hover = ActionChains(driver).move_to_element(elem)
    hover.perform()


@hover_element.add
def hover_element(driver, locator, sleep_time=0):
    """
    Hovering an element on specified locator.

    :type driver: WebDriver
    :type locator: tuple
    :type sleep_time: float
    """

    time.sleep(sleep_time)
    (WebDriverWait(driver, 20, ignored_exceptions=StaleElementReferenceException).until
     (ec.presence_of_element_located(locator)))
    element_to_hover = driver.find_element(*locator)
    hover = ActionChains(driver).move_to_element(element_to_hover)
    hover.perform()


@overload
def selecting_by_visible_text(_, elem: WebElement, text, sleep_time=0):
    """
    Selecting element contains specified text.

    :type elem: WebElement
    :type text: str
    :type sleep_time: int
    """

    time.sleep(sleep_time)
    select = Select(elem)
    select.select_by_visible_text(text)


@selecting_by_visible_text.add
def selecting_by_visible_text(driver, locator, text, sleep_time=0):
    """
    Selecting element located by locator parameter and contains specified text.

    :type driver: WebDriver
    :type locator: tuple
    :type text: str
    :type sleep_time: int
    """

    time.sleep(sleep_time)
    select = Select(driver.find_element(*locator))
    wait_for_loading(driver, 1.5)
    select.select_by_visible_text(text)
    wait_for_loading(driver, 1.5)


def login(driver,
          site="https://piexpertonline.power.com/site/login",
          user="pietest0062@piexpert.com",
          password="@piexpert"):
    """
    Log in to specified site.

    :type driver: WebDriver
    :type site: str
    """

    driver.get(site)
    send_keys(driver, user, Locators.Login.LOGIN_FIELD)
    wait_for_loading(driver)
    send_keys(driver, password, Locators.Login.PASSWORD_FIELD)
    wait_for_loading(driver)
    click(driver, Locators.Login.SUBMIT_LOGIN)
    try:
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.Login.CONTINUE_LOGIN))
        click(driver, Locators.Login.CONTINUE_LOGIN)
    except (NoSuchElementException, TimeoutException):
        pass



def delete_all_designs(driver, apply_deletion=True, download_before=False):
    """
    Delete all designs from file manager.

    :type driver: WebDriver
    """

    click(driver, Locators.IndexPage.OPEN_DESIGN)
    wait_for_loading(driver)
    click(driver, Locators.FileManager.SELECT_ALL)
    wait_for_loading(driver)
    while driver.find_element(*Locators.FileManager.DOWNLOAD).is_enabled():

        if download_before:
            click(driver, Locators.FileManager.DOWNLOAD)
            try:
                WebDriverWait(driver, 1).until(ec.presence_of_element_located(
                    Locators.FileManager.Navigation.NEXT_HIDDEN))
                break
            except TimeoutException:
                pass
            if not apply_deletion:
                try:
                    click(driver, Locators.FileManager.Navigation.NEXT)
                    click(driver, Locators.FileManager.SELECT_ALL)
                    continue
                except TimeoutException:
                    break

        if apply_deletion:
            first_row = driver.find_element(By.XPATH, "//table[@class='items']/tbody/tr/td[2]")
            click(driver, Locators.FileManager.DELETE)
            click(driver, Locators.FileManager.DIALOG_SUBMIT)
            wait_for_staleness(driver, first_row, expl_time=5)
        click(driver, Locators.FileManager.SELECT_ALL)

def open_design(driver, index):
    """
    Open existing design on index

    :type driver: WebDriver
    :type index: int
    """

    click(driver, Locators.IndexPage.OPEN_DESIGN)
    wait_for_loading(driver)
    try:
        click(driver, (By.XPATH, "//div[@id='fileManagerTable']/table/tbody/tr[{num}]/td[2]/a".format(num=index)))
    except TimeoutException:
        print('There\'s no design with such index on page')
        pass

def design_creation(driver, family, design_type, pdp=[(20)], va_list=[(12, 2)], dimming=False, opt=True, package=None):
    """
    Create design of specified family. Kind of design to generate depends on design_type parameter.

    :type driver: WebDriver
    :type family: str
    :type design_type: str
    """

    click(driver, Locators.IndexPage.NEW_DESIGN)
    wait_for_loading(driver)
    click(driver, (By.XPATH, ''.join(['//', Consts.FAMILY_NAME_DICT[family]])), sleep_time=2)
    wait_for_loading(driver)
    if design_type == 'pixls':
        click(driver, Locators.DesignCreation.PIXLS)
        wait_for_loading(driver)

    elif design_type == 'piexpert':
        click(driver, Locators.DesignCreation.PIEXPERT)
        wait_for_loading(driver)
        create_piexpert(driver, pdp, va_list, dimming, opt, package)
        wait_for_loading(driver)

def design_wizard_cp_pro(driver, family, charger_mode=None):
    '''
    Open design wizard dialog of specified family.

    :param driver: WebDriver
    :param family: str
    :param pdp: pdp value
    '''

    click(driver, Locators.IndexPage.NEW_DESIGN)
    wait_for_loading(driver)
    click(driver, (By.XPATH, ''.join(['//', Consts.FAMILY_NAME_DICT[family]])), sleep_time=2)
    wait_for_loading(driver)
    click(driver, Locators.DesignCreation.PIEXPERT)
    wait_for_loading(driver)
    # Select Charger Mode
    if charger_mode:
        selecting_by_visible_text(driver, (By.XPATH, '//select[@id = "2207"]'), charger_mode)
    # Next -> Next
    click(driver, (By.XPATH, '//button[@id="dlgNextWizardPage1"]'))
    wait_for_loading(driver)
    click(driver, (By.XPATH, '//button[@id="dlgNextWizardPage2"]'))
    wait_for_loading(driver)

def create_piexpert(driver, pdp=None, va_list=[(12, 2)], dimming=False, opt=True, package=None):
    """
    Function started in case of creation of PIExpert design

    :type driver: WebDriver
    :param va_list: list of outputs' values:
        va_list[0] : voltage value;
        va_list[1] : currency value.
    :param pdp: pdp value
    :param dimming: dimming on/off flag
    :param opt: optimization after creation flag
    :param package: package changing on creation
    :param download: download new created design
    """

    if pdp is None:
        pdp = [20]
    if package:
        selecting_by_visible_text(driver, (By.XPATH, '//select[@id = "159"]'), package)
    # Next -> Next
    click(driver, (By.XPATH, '//button[@id="dlgNextWizardPage1"]'))
    if dimming:
        click(driver, (By.XPATH, '//input[@name="DIMMING_FLAG"]'))
        wait_for_loading(driver)

    wait_for_loading(driver)
    click(driver, (By.XPATH, '//button[@id="dlgNextWizardPage2"]'))
    wait_for_loading(driver)
    try:
        if driver.find_element(By.XPATH, '//button[@id="outAddBtn"]'):
            wait_for_loading(driver)
            for num, item in enumerate(va_list):
                # adding output voltage and current
                click(driver, (By.XPATH, '//button[@id="outAddBtn"]'))
                wait_for_loading(driver)
                click(driver, (By.XPATH, '//input[@id="6_{num}"]'.format(num=num)))
                wait_for_loading(driver)
                v_field = driver.find_element(By.XPATH, '//input[@id="6_{num}"]'.format(num=num))
                wait_for_loading(driver)
                clear(driver, (By.XPATH, '//input[@id="6_{num}"]'.format(num=num)))
                wait_for_staleness(driver, v_field)
                send_keys(driver, str(item[0]), (By.XPATH, '//input[@id="6_{num}"]'.format(num=num)))
                wait_for_loading(driver)
                click(driver, (By.XPATH, '//input[@id="241_{num}"]'.format(num=num)))
                wait_for_loading(driver)
                v_field = driver.find_element(By.XPATH, '//input[@id="6_{num}"]'.format(num=num))
                wait_for_loading(driver)
                clear(driver, (By.XPATH, '//input[@id="241_{num}"]'.format(num=num)))
                wait_for_staleness(driver, v_field)
                send_keys(driver, str(item[1]), (By.XPATH, '//input[@id="241_{num}"]'.format(num=num)))
                wait_for_loading(driver)
                click(driver, (By.XPATH, '//input[@id="6_{num}"]'.format(num=num)))
                wait_for_loading(driver)
                click(driver, (By.XPATH, '//button[@id = "dlgOK105"]'))
                wait_for_loading(driver)

    except (NoSuchElementException, TimeoutException):
        if driver.find_element(By.XPATH, "//div/input[@id='2465']"):
            wait_for_loading(driver, 1.5)
            pdp_field = driver.find_element(By.XPATH, '//div/input[@id="2465"]')
            wait_for_loading(driver)
            click(driver, (By.XPATH, '//div/input[@id="2465"]'))
            wait_for_loading(driver)
            pdp_field.send_keys(Keys.CONTROL + 'a')
            wait_for_loading(driver)
            pdp_field.send_keys(Keys.BACKSPACE)
            wait_for_loading(driver)
            send_keys(driver, str(pdp), (By.XPATH, '//div/input[@id="2465"]'))
            wait_for_loading(driver, 1.5)
            pdp_field.send_keys(Keys.ENTER)
            wait_for_loading(driver, 1.5)

    # Next -> Finish -> OK -> OK
    wait_for_loading(driver)
    click(driver, (By.XPATH, '//button[@id="dlgNextWizardPage31"]'))
    wait_for_loading(driver)
    click(driver, (By.XPATH, '//button[@id="dlgFinishtWizard"]'))
    wait_for_loading(driver, 1.5)
    if opt:
        wait_for_loading(driver)
        click(driver, (By.XPATH, '//button[@id="dlgOKSolFlt"]'))
        wait_for_loading(driver)
        click(driver, (By.XPATH, '//button[@id="closedlgOptSolSel"]'))
        wait_for_loading(driver)
    else:
        wait_for_loading(driver)
        click(driver, (By.XPATH, '//button[@id="dlgCancel155"]'))

    wait_for_loading(driver, 1.5)

def table_cell_elem(driver, row, column):
    """
    Get element from PIXls table by row and column.

    :type driver: WebDriver
    :type row: int
    :type column: int
    :return: WebElement
    """

    return driver.find_element(By.XPATH, "//div[@class='pixls']/table/tbody/tr[{row}]/td[{column}]".format(row=row, column=column))

def design_results_elem(driver, field_change_name, value, hard_search=False):
    """
    Function change field value to specified one via sending keys to it.

    :type driver: WebDriver
    :type field_change_name: str
    """
    # Field to change getting
    field_to_change = driver.find_element(By.XPATH,
                                          '//td[contains(text(), "{name}")]/../td/input'.format(name=field_change_name))

    click(driver, (By.XPATH, '//td[contains(text(), "{name}")]/../td/input'.format(name=field_change_name)))
    wait_for_loading(driver)


    # Field to change getting
    if hard_search:
        field_to_change = driver.find_element(By.XPATH,
                                              '//td[text()="{name}"]/../td/input'.format(name=field_change_name))
    else:
        field_to_change = driver.find_element(By.XPATH,
                                              '//td[contains(text(), "{name}")]/../td/input'.format(name=field_change_name))
    # Send new value to it
    #field_to_change.clear()
    field_to_change.send_keys((Keys.CONTROL + 'a'))
    field_to_change.send_keys(str(value))
    field_to_change.send_keys(Keys.ENTER)
    wait_for_loading(driver)
    try:
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.Errors.ERROR_TEXT))
        click(driver, Locators.Errors.ERROR_OK)
    except (NoSuchElementException, TimeoutException):
        pass
    wait_for_loading(driver)
    wait_for_staleness(driver, field_to_change)


def table_cell_locator(row, column):
    """
    Get locator from PIXls table by row and column.

    :type row: int
    :type column: int
    """

    return By.XPATH, "//div[@class='pixls']/table/tbody/tr[{row}]/td[{column}]".format(row=row, column=column)


def design_dialog_locator(dialog_family, sub_dialog):
    """
    Get locator for PIExpert's dialog.

    :type dialog_family: str
    :type sub_dialog: str
    """

    return By.XPATH, "//span[contains(text(), '{dialog_family}')]/..//a[contains(text(), '{sub_dialog}')]".format(
        dialog_family=dialog_family, sub_dialog=sub_dialog)


def time_string():
    """
    Return string with current time

    :return: String, formatted as 'Time: HH:MM:SS DD/MM/YYYY'
    """
    return 'Time: {time.tm_hour:02d}:{time.tm_min:02d}:{time.tm_sec:02d} {time.tm_mday:02d}/{time.tm_mon:02d}/{time.tm_year}'.format(
        time=time.localtime())


def rerunner(func):
    """
    Decorator, try to call func, and refresh browser, if fails

    :param func: function to decorate
    """
    def wrapper():
        try:
            func()
        except:
            pass

    return wrapper


def wait_for_loading(driver, implicitly_wait_timeout=6):
    """
    Waiting for loading-element disappearing

    :type implicitly_wait_timeout: float
    :type driver: WebDriver
    """

    try:
        driver.implicitly_wait(implicitly_wait_timeout)
        WebDriverWait(driver, 6).until(
            ec.staleness_of(driver.find_element(By.ID, "loading")))
        driver.implicitly_wait(implicitly_wait_timeout)

    except NoSuchElementException:
        driver.implicitly_wait(implicitly_wait_timeout)
        pass

    except TimeoutException:
        driver.implicitly_wait(implicitly_wait_timeout)
        print('Timeout exception while loading')
        #traceback.print_exc()
        # driver.quit()



def wait_for_loading_decorator(function):
    """
    Decorator for function, which is checking for an loading-element appearing and wait while its disappear.
    Should be added to a function if:
    - we know, that often there's a possibility of loading-element to be present after it's execution;
    - driver is an exactly first parameter in this function.

    :param function: function to decorate
    """

    def loading_waiter(*args, **kwargs):
        function(*args, **kwargs)
        wait_for_loading(args[0])

    return loading_waiter


def resistor_changing(driver, field_name, value, ok_button_id="commitdlg113"):
    """
    Function change resistors parameter on resistor's dialog

    :type driver: WebDriver
    :type field_name: str
    """
    # Unlock user overwrite
    click(driver,
          (By.XPATH, '//form[@id="form113"]//div/span'))
    wait_for_loading(driver)
    #click(driver, element)
    # Field to change getting
    field_to_change = driver.find_element(
        By.XPATH, '//form[@id="form113"]//label[contains(text(), "{name}")]/../select'.format(name=field_name))
    wait_for_loading(driver)
    # selecting required value
    selecting_by_visible_text(driver, field_to_change, str(value))
    wait_for_loading(driver)
    wait_for_staleness(driver, field_to_change)
    # click OK button
    click(driver, (By.ID, ok_button_id))
    wait_for_loading(driver)
    try:
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.Errors.ERROR_TEXT))
        click(driver, Locators.Errors.ERROR_OK)
    except (NoSuchElementException, TimeoutException):
        pass
    wait_for_loading(driver)


def field_param_setting(driver, field_change_name, value, hard_search=False):
    """
    Function change field value to specified one via sending keys to it.

    :type driver: WebDriver
    :type field_change_name: str
    :type hard_search: bool
    """

    # Field to change getting
    field_to_change = driver.find_element(By.XPATH,
                                          '//label[contains(text(), "{name}")]/../input'.format(name=field_change_name))
    wait_for_loading(driver)
    # Click on user overwrite button
    click(driver, (By.XPATH, '//label[contains(text(), "{name}")]/../span'.format(name=field_change_name)))
    wait_for_loading(driver)
    wait_for_staleness(driver, field_to_change)

    # Field to change getting
    if hard_search:
        field_to_change = driver.find_element(By.XPATH,
                                              '//label[text()="{name}"]/../input'.format(name=field_change_name))
        wait_for_loading(driver)
    else:
        field_to_change = driver.find_element(By.XPATH,
                                              '//label[contains(text(), "{name}")]/../input'.format(name=field_change_name))
        wait_for_loading(driver)
    # Send new value to it
    #wait_for_loading(driver)
    field_to_change.send_keys(Keys.CONTROL + "a")
    wait_for_loading(driver)
    field_to_change.send_keys(str(value))
    wait_for_loading(driver)
    field_to_change.send_keys(Keys.ENTER)
    wait_for_loading(driver)
    try:
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.Errors.ERROR_TEXT))
        click(driver, Locators.Errors.ERROR_OK)
    except (NoSuchElementException, TimeoutException):
        pass
    wait_for_loading(driver)
    wait_for_staleness(driver, field_to_change)


def select_by_part_number(driver, value, ok_button_id="commitdlg113"):
    """
    Function select some device from list by unique id

    :type driver: WebDriver
    :type value: str
    """

    click(driver,
          (By.XPATH, '//td[contains(text(), "{name}")]'.format(name=value)))
    wait_for_loading(driver)
    click(driver, (By.ID, ok_button_id))
    wait_for_loading(driver)
    try:
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.Errors.ERROR_TEXT))
        click(driver, Locators.Errors.ERROR_OK)
    except (NoSuchElementException, TimeoutException):
        pass
    wait_for_loading(driver)


def unlock_with_change(driver, param_name, hard_search=False):
    """
    Unlock user overwrite button and click on 'Change'

    :type driver: WebDriver
    :type param_name: str
    :type hard_search: bool
    """
    if hard_search:
        click(driver, (By.XPATH, '//p[text() = "{name}"]/../../td/map/area[2]'.format(name=param_name)))
        wait_for_loading(driver)
    else:
        click(driver, (By.XPATH, '//p[contains(text(), "{name}")]/../../td/map/area[2]'.format(name=param_name)))
        wait_for_loading(driver)
    click(driver, (By.XPATH, '//ul[contains(@class,"context-menu-list")]/li/span[contains(text(), "Change")]'))
    wait_for_loading(driver)

def unlock_with_default(driver, param_name, hard_search=False):
    """
        Unlock user overwrite button and click on 'Default'

        :type driver: WebDriver
        :type param_name: str
        :type hard_search: bool
        """
    if hard_search:
        click(driver, (By.XPATH, '//p[text() = "{name}"]/../../td/map/area[2]'.format(name=param_name)))
        wait_for_loading(driver)
    else:
        click(driver, (By.XPATH, '//p[contains(text(), "{name}")]/../../td/map/area[2]'.format(name=param_name)))
        wait_for_loading(driver)
    click(driver, (By.XPATH, '//ul[contains(@class,"context-menu-list")]/li/span[contains(text(), "Default")]'))
    wait_for_loading(driver)

def errors_warnings_get(driver):
    """
    Get a list of errors and warnings appeared on current page

    :type driver: WebDriver
    :return: list
    """

    res = []
    ew_elems_list = driver.find_elements_by_xpath('//div[contains(@class, "reportStatusInToolbar")]//tr')
    for elem in ew_elems_list:
        img = elem.find_element(By.XPATH, '//img').get_attribute('src')
        id = elem.find_element(By.XPATH, '//td[contains(@id, "PIEEE_help")]').text

        if 'error' in img:
            ew_type = 'error'
        elif 'info' in img:
            ew_type = 'info'
        else:
            ew_type = 'warning'

        res.append([id, ew_type])
    return res


def errors_warnings_check(driver, check_id, error_type=None):
    """
    Check if the error/warning/info with specified id appeared on webpage

    :type driver: WebDriver
    :type check_id: int
    """

    errors_list = errors_warnings_get(driver)
    ids = [int(elem[0]) for elem in errors_list]
    id_match = True if check_id in ids else False

    if error_type:
        cur_type = [elem[1] for elem in errors_list if elem[0] == check_id]
        type_match = True if cur_type == error_type else False

        return type_match and id_match

    else:
        return id_match


class is_element_stale(object):
    """
    Checks if a webelement is stale.

    """

    def __init__(self, elem):
        """

        :type elem: WebElement
        """
        self.elem = elem

    def __call__(self, driver):
        try:
            self.elem.find_element(By.XPATH, '//')
        except StaleElementReferenceException:
            return True
        return False


def wait_for_staleness(driver, elem, expl_time=20):
    """
    Function waits element to become stale

    :type driver: WebDriver
    :type elem: WebElement
    :type expl_time: int
    """

    WebDriverWait(driver, expl_time).until(is_element_stale(elem))


def get_elem_or_null(driver, locator):
    """
    Return element by specified locator or [] if element wasn't found

    :type driver: WebDriver
    :type locator: tuple
    :return: WebElement
    """

    try:
        return driver.find_element(*locator)
    except NoSuchElementException:
        return []


def get_elems_or_null(driver, locator):
    """
    Return elements by specified locator or [] if no any elements were found

    :type driver: WebDriver
    :type locator: tuple
    :return: WebElement
    """

    try:
        return driver.find_elements(*locator)
    except NoSuchElementException:
        return []
