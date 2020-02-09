from sound_cloud import fetch_soundcloud
from youtube import fetch_youtube


def get_all_soundcloud():
    """ Define what you want to fetch from SoundCloud """

    # Customize:
    streaming_user = "szedl-k-m-t"
    fetch_soundcloud(streaming_user, "soft-mixes")
    fetch_soundcloud(streaming_user, "melodic-mixes")
    fetch_soundcloud(streaming_user, "liquid-chill")
    fetch_soundcloud(streaming_user, "liked")
    fetch_soundcloud(streaming_user, "weird-stuff")


def get_all_youtube():
    """ Define what you want to fetch from YouTube """

    # Customize:
    fetch_youtube("PLtiS4u-DD2u8d-vaEacIxqMsLvUpH0vyc")


""" Start fetching your music lists: """
get_all_youtube()
# get_all_soundcloud()
