import time


def get_text(element):
    return element.text


def fetch_streamer(driver, target_xpath):
    go_down = 15
    default_scroll_down_px = 10000

    for loop_scroll in range(go_down):
        init_num_of_titles = len(driver.find_elements_by_xpath(target_xpath))
        driver.execute_script("window.scrollBy(0 ,%i)" % default_scroll_down_px)
        time.sleep(1)

        new_num_of_titles = len(driver.find_elements_by_xpath(target_xpath))

        if new_num_of_titles == init_num_of_titles:
            break

    title_elements = driver.find_elements_by_xpath(target_xpath)

    titles = list(map(get_text, title_elements))

    driver.close()

    return titles
