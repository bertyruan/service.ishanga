import xbmc
import xbmcgui
from . import utilities as util

ishanga = "Ishanga Player Service: "
AudioExtensions = ['.mp3']

class MediaType:
    NONE = 0
    VIDEO = 1
    AUDIO = 2

def parse_media_type(filename):
    idx = filename.rfind('.')
    file_ext = filename[idx:]
    
    util.log(ishanga, file_ext)

    if AudioExtensions.count(file_ext):
        util.log(ishanga, "AN AUDIO FILE IS PLAYING")
        return MediaType.AUDIO
    return MediaType.VIDEO

def activate_window(window_id, media_type):
    if media_type == MediaType.AUDIO:
        xbmc.executebuiltin('Dialog.Close(all, true)')
        xbmc.executebuiltin(f'ActivateWindow({util.IshangaWindowId.screensaver_window})')
        return

    if not xbmcgui.getCurrentWindowId() == window_id: 
        xbmc.executebuiltin('Dialog.Close(all, true)')
        xbmc.executebuiltin(f'ActivateWindow({window_id})')



class XBMCPlayer(xbmc.Player):
    def __init__(self):
        super().__init__()
        self.media_type = MediaType.NONE

    def onPlayBackStarted(self):
        util.log(ishanga, "PLAYBACK STARTED")
        filename = xbmc.Player().getPlayingFile()
        self.media_type = parse_media_type(filename)
        activate_window(util.IshangaWindowId.screensaver_window, self.media_type)
        xbmc.Player.pause(self)     

    def onPlayBackPaused(self):
        activate_window(util.IshangaWindowId.screensaver_window, self.media_type)
        util.log(ishanga, "VIDEO IS PAUSED. SCREENSAVER ON")

    def onPlayBackResumed(self):
        activate_window(util.KodiWindowId.video_window, self.media_type)

    def onPlayBackSeek(self, time, seekOffset):
        # xbmc.Player.pause(self)
        util.log(ishanga, "PLAYBACK SEEK")
        activate_window(util.KodiWindowId.video_window, self.media_type)

XBMCPlayer()