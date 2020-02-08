import os

from selenium import webdriver

import pytest

command_executor = ""

if os.getenv('BROWSERSTACK_KEY') is None:
    command_executor = os.getenv('BROWSERSTACK_KEY')
else:
    from pytest.secret import secrets
    command_executor = secrets.command_executor

desired_cap = {
    'browser': 'Chrome',
    'browser_version': '80.0 beta',
    'os': 'Windows',
    'os_version': '10',
    'resolution': '2048x1536',
    'name': 'Bstack-[Python] Sample Test'
}

web_driver = webdriver.Remote(
    command_executor=command_executor,
    desired_capabilities=desired_cap)


@pytest.fixture(scope="module")
def driver():
    """ Provides a webDriver for the tests through BrowserStack """
    yield web_driver

    web_driver.quit()
