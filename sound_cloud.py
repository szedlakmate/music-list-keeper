from fetch_list import fetch_streamer

def fetch_soundcloud(user, album):
    SOUNDCLOUD_TARGET_XPATH = '//*[@id="content"]//li//*[contains(@class, "trackItem__content")]'
    album_url = "https://soundcloud.com/%s/sets/%s" % (user, album)
    output_file_name = "soundcloud_%s_%s.txt" % (user, album)

    fetch_streamer(album_url, SOUNDCLOUD_TARGET_XPATH, output_file_name)
