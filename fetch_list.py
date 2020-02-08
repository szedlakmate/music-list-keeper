import time

from selenium import webdriver


def fetch_streamer(url, target_xpath, output_file_name):
    go_down = 15
    default_scroll_down_px = 10000

    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(3)
    time.sleep(1)
    for loop_scroll in range(go_down):
        init_num_of_titles = len(driver.find_elements_by_xpath(target_xpath))
        driver.execute_script("window.scrollBy(0 ,%i)" % default_scroll_down_px)
        time.sleep(1)

        new_num_of_titles = len(driver.find_elements_by_xpath(target_xpath))

        if new_num_of_titles == init_num_of_titles:
            break

    titles = driver.find_elements_by_xpath(target_xpath)

    with open(output_file_name, 'w') as result_file:
        print('\n\n\nOutput: %s\nNumber of found musics:%i\n\n' % (output_file_name, len(titles)))
        result_file.write('Number of found musics:%i\n\n' % len(titles))

        for title in titles:
            print(title.text)
            result_file.write(title.text + "\n")

    driver.close()
