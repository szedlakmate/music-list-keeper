from selenium import webdriver

from fetch_list import fetch_streamer
from write_output import write_to_file


def fetch_youtube(album):
    youtube_target_xpath = '//ytd-playlist-video-renderer//*[@id="meta"]'

    url = "https://www.youtube.com/playlist?list=%s" % album

    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(8)

    list_name = driver.find_element_by_id('title')

    output_file_name = "youtube_%s_%s.txt" % (list_name.text, album)

    titles = fetch_streamer(driver, youtube_target_xpath)

    write_to_file(output_file_name, titles)

