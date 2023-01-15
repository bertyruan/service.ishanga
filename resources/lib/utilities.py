import xbmc

def log(file, text):
    xbmc.log(f"{file}: {text}", xbmc.LOGINFO)

class KodiWindowId:
    screensaver_window = 11200
    audio_screensaver_window = 11201
    video_window = 12005
    video_nav_window = 10025

class IshangaWindowId:
    screensaver_window = 1200
    audio_screensaver_window = 1201