import time

from selenium import webdriver

from fetch_list import fetch_streamer
from write_output import write_to_file

soundcloud_target_xpath = '//*[@id="content"]//li//*[contains(@class, "trackItem__content")]'


def soundcloud_url(user, album):
    return "https://soundcloud.com/%s/sets/%s" % (user, album)


def fetch_soundcloud(user, album):
    url = soundcloud_url(user, album)
    output_file_name = "soundcloud_%s_%s.txt" % (user, album)

    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(8)
    time.sleep(2)

    titles = fetch_streamer(driver, soundcloud_target_xpath)

    write_to_file(output_file_name, titles)
