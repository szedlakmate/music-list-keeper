from fetch_list import fetch_streamer
from sound_cloud import soundcloud_target_xpath, soundcloud_url


class TestConnection(object):
    def test_connection(self, driver):
        driver.get("http://www.google.com")
        assert driver.title == "Google"

    def test_connection_youtube(self, driver):
        driver.get("https://www.youtube.com/")
        assert driver.title == "YouTube"

    def test_connection_soundcloud(self, driver):
        driver.get("https://soundcloud.com/")  # "SoundCloud – Listen to free music and podcasts on SoundCloud"
        assert driver.title.split(' ')[0] == "SoundCloud"


class TestLists(object):
    # def test_youtube_list(self, driver):
    #     assert driver.title == "Google"

    def test_soundcloud_list(self, driver):
        album = "soft-mixes"
        user = "szedl-k-m-t"

        driver.get(soundcloud_url(user, album))

        titles = fetch_streamer(driver, soundcloud_target_xpath)
        assert titles[0] == "3LAU — Lean Away (3LAU Mashup) - Fetty Wap vs Daya vs Major Lazer"
        assert len(titles) >= 75
