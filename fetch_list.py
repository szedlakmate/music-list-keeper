import time


def get_text(element):
    return element.text


def fetch_streamer(driver, target_xpath, wait_for_new_elements=1):
    go_down = 15
    default_scroll_down_px = 10000

    for loop_scroll in range(go_down):
        init_num_of_titles = len(driver.find_elements_by_xpath(target_xpath))
        driver.execute_script("window.scrollBy(0 ,%i)" % default_scroll_down_px)
        time.sleep(1)

        new_item_found = False

        for i in range(wait_for_new_elements):
            new_num_of_titles = len(driver.find_elements_by_xpath(target_xpath))

            if new_num_of_titles > init_num_of_titles:
                new_item_found = True
                break
            else:
                time.sleep(1)

        if not new_item_found:
            break

    time.sleep(1)
    title_elements = driver.find_elements_by_xpath(target_xpath)
    print('Number of found musics:%i\n\n' % len(title_elements))

    return list(map(get_text, title_elements))
