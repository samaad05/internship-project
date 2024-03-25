

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context, browser='chrome', headless=False):
    """
    :param context: Behave context
    :param browser: String indicating the browser to use (default is 'chrome')
    :param headless: Boolean indicating whether to run in headless mode
    """

    #
    # browser = browser()
    # if browser == 'chrome':
    #     chrome_options = webdriver.ChromeOptions()
    #     if headless:
    #         chrome_options.add_argument("--headless")
    #
    #     driver_path = ChromeDriverManager().install()
    #     service = ChromeService(driver_path)
    #     context.driver = webdriver.Chrome(service=service, options=chrome_options)
    # elif browser == 'firefox':
    #     firefox_options = webdriver.FirefoxOptions()
    #     if headless:
    #         firefox_options.add_argument("--headless")
    #
    #     driver_path = GeckoDriverManager().install()
    #     service = FirefoxService(driver_path)
    #     context.driver = webdriver.Firefox(service=service, options=firefox_options)
    # else:
    #     raise ValueError("Unsupported browser. Please specify 'chrome' or 'firefox'.")

    ###BrowserStack###
    bs_user = 'samaadbronson_Z270dL'
    bs_key = '63t1qDFF5KMCWsw8LKy2'
    url = f'http://{bs_user}:{bs_key}@hub.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'os': 'OS X',
        'osVersion': 'Ventura',
        'browserName': 'Chrome',
        'name': 'verifies user can click on “Connect the company”'
    }
    options.set_capability('bstack_options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, browser='chrome')


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
