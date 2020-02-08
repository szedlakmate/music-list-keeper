import time

from selenium import webdriver

from fetch_list import fetch_streamer


def fetch_youtube(album):
    youtube_target_xpath = '//ytd-playlist-video-renderer//*[@id="meta"]'

    url = "https://www.youtube.com/playlist?list=%s" % album

    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(8)

    list_name = driver.find_element_by_id('title')

    output_file_name = "youtube_%s_%s.txt" % (list_name.text, album)

    fetch_streamer(driver, youtube_target_xpath, output_file_name)
