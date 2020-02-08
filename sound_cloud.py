import time

from selenium import webdriver

from fetch_list import fetch_streamer


def fetch_soundcloud(user, album):
    soundcloud_target_xpath = '//*[@id="content"]//li//*[contains(@class, "trackItem__content")]'
    url = "https://soundcloud.com/%s/sets/%s" % (user, album)
    output_file_name = "soundcloud_%s_%s.txt" % (user, album)

    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(8)
    time.sleep(2)

    fetch_streamer(driver, soundcloud_target_xpath, output_file_name)
