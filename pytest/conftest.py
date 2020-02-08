from selenium import webdriver

import pytest
from pytest.secret import secrets

desired_cap = {
    'browser': 'Chrome',
    'browser_version': '80.0 beta',
    'os': 'Windows',
    'os_version': '10',
    'resolution': '2048x1536',
    'name': 'Bstack-[Python] Sample Test'
}


@pytest.fixture(scope="module")
def driver():
    web_driver = webdriver.Remote(
        command_executor=secrets.command_executor,
        desired_capabilities=desired_cap)

    def fin():
        print("close connection")
        web_driver.quit()

    return web_driver
