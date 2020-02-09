from sound_cloud import fetch_soundcloud
from youtube import fetch_youtube


def get_all_soundcloud():
    """ Define what you want to fetch from SoundCloud """

    # Customize:
    # Example target URL: https://soundcloud.com/szedl-k-m-t/sets/soft-mixes
    streaming_user = "szedl-k-m-t"
    fetch_soundcloud(streaming_user, "soft-mixes")

    # Example #2: https://soundcloud.com/szedl-k-m-t/sets/melodic-mixes
    fetch_soundcloud(streaming_user, "melodic-mixes")
    fetch_soundcloud(streaming_user, "liquid-chill")
    fetch_soundcloud(streaming_user, "liked")
    fetch_soundcloud(streaming_user, "weird-stuff")


def get_all_youtube():
    """ Define what you want to fetch from YouTube """

    # Customize:
    # Example target URL: https://www.youtube.com/playlist?list=PLtiS4u-DD2u8d-vaEacIxqMsLvUpH0vyc
    fetch_youtube("PLtiS4u-DD2u8d-vaEacIxqMsLvUpH0vyc")

########################
#   GET MUSIC LISTS:   #
########################

get_all_youtube()
# get_all_soundcloud()
