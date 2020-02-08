from selenium import webdriver

import pytest

command_executor = ""
try:
    from pytest.secret import secrets
    command_executor = secrets.command_executor
finally:
    command_executor = BROWSERSTACK_KEY

desired_cap = {
    'browser': 'Chrome',
    'browser_version': '80.0 beta',
    'os': 'Windows',
    'os_version': '10',
    'resolution': '2048x1536',
    'name': 'Bstack-[Python] Sample Test'
}

web_driver = webdriver.Remote(
        command_executor=secrets.command_executor,
        desired_capabilities=desired_cap)


@pytest.fixture(scope="module")
def driver():
    """ Provides a webDriver for the tests through BrowserStack """
    yield web_driver

    web_driver.quit()
