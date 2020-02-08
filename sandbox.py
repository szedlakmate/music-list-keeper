from sound_cloud import fetch_soundcloud
from youtube import fetch_youtube

# streaming_user = "szedl-k-m-t"
# streaming_album = "soft-mixes"
#
# fetch_soundcloud(streaming_user, "soft-mixes")
# fetch_soundcloud(streaming_user, "melodic-mixes")
# fetch_soundcloud(streaming_user, "liquid-chill")
# fetch_soundcloud(streaming_user, "liked")
# fetch_soundcloud(streaming_user, "weird-stuff")

roland_youtube = [
    "FL7V-5I1nDCFkxNOW9_KBZtg",
    "PLF0DA38DF2286ABBF"
]

fetch_youtube(roland_youtube[0])
fetch_youtube(roland_youtube[1])
