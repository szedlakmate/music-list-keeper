import pytest


class TestConnection(object):
    def test_connection(self, driver):
        driver.get("http://www.google.com")

        assert driver.title == "Google"
        driver.quit()



