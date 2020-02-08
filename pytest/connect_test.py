class TestConnection(object):
    def test_connection(self, driver):
        driver.get("http://www.google.com")
        assert driver.title == "Google"

    def test_connection_youtube(self, driver):
        driver.get("https://www.youtube.com/")
        assert driver.title == "YouTube"
