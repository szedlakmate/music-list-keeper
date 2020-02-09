from tools import fetch_streamer, get_driver, write_to_file

youtube_target_xpath = '//ytd-playlist-video-renderer//*[@id="meta"]'


def fetch_youtube(album):
    url = youtube_url(album)

    driver = get_driver()
    driver.get(url)

    list_name = driver.find_element_by_id('title')
    output_file_name = "youtube_%s_%s.txt" % (list_name.text, album)
    titles = fetch_streamer(driver, youtube_target_xpath, 0)

    driver.quit()

    write_to_file(output_file_name, titles)


def youtube_url(album):
    url = "https://www.youtube.com/playlist?list=%s" % album
    return url
