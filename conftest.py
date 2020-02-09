import os

import pytest
from selenium import webdriver

from tools import get_driver

web_driver = None

# BrowserStack config
FORCE_REMOTE_TESTING = False
desired_cap = {
    'browser': 'Chrome',
    'browser_version': '80.0 beta',
    'os': 'Windows',
    'os_version': '10',
    'resolution': '2048x1536',
    'name': 'Bstack-[Python] Sample Test'
}

# Determine target browser
if os.getenv('BROWSERSTACK_KEY') is None:
    print('Non-CI test')

    if FORCE_REMOTE_TESTING:
        # noinspection PyUnresolvedReferences
        from pytest.secret import secrets

        command_executor = secrets.command_executor
        web_driver = webdriver.Remote(
            command_executor=command_executor,
            desired_capabilities=desired_cap)
        web_driver.implicitly_wait(8)
    else:
        web_driver = get_driver()

else:
    print('CI test')
    command_executor = os.getenv('BROWSERSTACK_KEY')

    web_driver = webdriver.Remote(
        command_executor=command_executor,
        desired_capabilities=desired_cap)


@pytest.fixture(scope="module", autouse=True)
def driver():
    """ Provides a webDriver for the tests through BrowserStack """
    yield web_driver

    try:
        web_driver.quit()
    finally:
        print('Failed to close web_driver')
