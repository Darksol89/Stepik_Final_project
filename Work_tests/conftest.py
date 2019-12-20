import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help='Choose browser: chrome or firefox')

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        print('\nstart firefox browser for test..')
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    browser.implicitly_wait(20)
    yield browser
    print('\nquit browser..')
    browser.quit()