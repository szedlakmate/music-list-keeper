import time

from fetch_list import fetch_streamer
from my_lists.generate_webdriver import get_driver
from write_output import write_to_file

soundcloud_target_xpath = '//*[@id="content"]//li//*[contains(@class, "trackItem__content")]'


def soundcloud_url(user, album):
    return "https://soundcloud.com/%s/sets/%s" % (user, album)


def fetch_soundcloud(user, album):
    url = soundcloud_url(user, album)
    output_file_name = "soundcloud_%s_%s.txt" % (user, album)

    driver = get_driver()
    driver.get(url)

    titles = fetch_streamer(driver, soundcloud_target_xpath)

    driver.quit()

    write_to_file(output_file_name, titles)
