import xbmc
import xbmcaddon

audio_dot = "audio_dot"

def log(file, text):
    xbmc.log(f"{file}: {text}", xbmc.LOGINFO)

def get_settings(name):
    return xbmcaddon.Addon().getSetting(name)

class KodiWindowId:
    screensaver_window = 11200
    white_audio_screensaver_window = 11201
    grey_audio_screensaver_window = 11202
    video_window = 12005
    video_nav_window = 10025

    def __init__(self):
        self.screensaver_ids = [KodiWindowId.screensaver_window, KodiWindowId.white_audio_screensaver_window, KodiWindowId.grey_audio_screensaver_window]

        
class IshangaWindowId:
    screensaver_window = 1200
    white_audio_screensaver_window = 1201
    grey_audio_screensaver_window = 1202

    def __init__(self):
        self.audio_screensavers = {
            "White": IshangaWindowId.white_audio_screensaver_window,
            "Grey": IshangaWindowId.grey_audio_screensaver_window,
            "Disabled": IshangaWindowId.screensaver_window
        }