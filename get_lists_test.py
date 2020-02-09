from sound_cloud import soundcloud_target_xpath, soundcloud_url
from tools import fetch_streamer
from youtube import youtube_url, youtube_target_xpath


class TestConnection(object):
    def test_connection(self, driver):
        print('\nGoing to Google')
        driver.get("http://www.google.com")
        print('Reading title')
        assert driver.title == "Google"


class TestYouTube(object):
    def test_connection_youtube(self, driver):
        print('\nGoing to Youtube')
        driver.get("https://www.youtube.com/")
        print('Reading title')
        assert driver.title == "YouTube"

    def test_youtube_list(self, driver):
        print('\ntest_youtube_list')

        driver.get(youtube_url("PLtiS4u-DD2u8d-vaEacIxqMsLvUpH0vyc"))
        expected_result = "Cafe De Anatolia - Deep House Selection 2 (Mix by Ferha"

        print('Looking for %s' % expected_result)
        titles = fetch_streamer(driver, youtube_target_xpath)
        assert titles[0][0: len(expected_result)] == expected_result
        assert len(titles) >= 9


class TestSoundCloud(object):
    def test_connection_soundcloud(self, driver):
        print('\nGoing to Soundcloud')
        driver.get("https://soundcloud.com/")  # "SoundCloud – Listen to free music and podcasts on SoundCloud"
        print('Reading title')
        assert driver.title.split(' ')[0] == "SoundCloud"

    def test_soundcloud_list(self, driver):
        print('\ntest_soundcloud_list')

        album = "soft-mixes"
        user = "szedl-k-m-t"
        expected_result = "3LAU — Lean Away (3LAU Mashup) - Fetty Wap vs Daya vs Major Lazer"

        driver.get(soundcloud_url(user, album))

        print('Looking for %s' % expected_result)
        titles = fetch_streamer(driver, soundcloud_target_xpath)
        assert titles[0] == expected_result
        assert len(titles) >= 132
