import time

from selenium import webdriver


def fetch_soundcloud(user, album):
    SOUNDCLOUD_TARGET_XPATH = '//*[@id="content"]//li//*[contains(@class, "trackItem__content")]'
    go_down = 15
    default_scroll_down_px = 10000
    album_url = "https://soundcloud.com/%s/sets/%s" % (user, album)

    driver = webdriver.Chrome()
    driver.get(album_url)
    driver.implicitly_wait(3)
    time.sleep(1)
    for loop_scroll in range(go_down):
        init_num_of_titles = len(driver.find_elements_by_xpath(SOUNDCLOUD_TARGET_XPATH))
        driver.execute_script("window.scrollBy(0 ,%i)" % default_scroll_down_px)
        time.sleep(1)

        new_num_of_titles = len(driver.find_elements_by_xpath(SOUNDCLOUD_TARGET_XPATH))

        if new_num_of_titles == init_num_of_titles:
            break

    titles = driver.find_elements_by_xpath(SOUNDCLOUD_TARGET_XPATH)

    output_file_name = "soundcloud_%s_%s.txt" % (user, album)

    with open(output_file_name, 'w') as result_file:
        print('\n\n\nOutput: %s\nNumber of found musics:%i\n\n' % (output_file_name, len(titles)))
        result_file.write('Number of found musics:%i\n\n' % len(titles))

        for title in titles:
            print(title.text)
            result_file.write(title.text + "\n")

    driver.close()


streaming_user = "szedl-k-m-t"
streaming_album = "soft-mixes"

fetch_soundcloud(streaming_user, "soft-mixes")
fetch_soundcloud(streaming_user, "melodic-mixes")
fetch_soundcloud(streaming_user, "liquid-chill")
fetch_soundcloud(streaming_user, "liked")
fetch_soundcloud(streaming_user, "weird-stuff")
