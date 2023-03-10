import xbmc
import xbmcgui
import xbmcaddon
from resources.lib import utilities as util

ishanga = "Ishanga Player Service: "
AudioExtensions = ['.mp3', '.m4a']

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

def activate_window(window_id):
    xbmc.executebuiltin('Dialog.Close(all, true)')
    xbmc.executebuiltin(f'ActivateWindow({window_id})')

def _activate_window_by_media(window_id, media_type):
    if media_type == MediaType.AUDIO:
        idx = int(xbmcaddon.Addon().getSetting(util.audio_dot))
        window_id = list(util.IshangaWindowId().audio_screensavers.values())[idx]
        activate_window(window_id)
        return

    if not xbmcgui.getCurrentWindowId() == window_id: 
        activate_window(window_id)

# Sometimes kodi just doesn't successfully change window Id....
def activate_window_by_media(window_id, media_type, num=1):
    for _ in range(num):
        _activate_window_by_media(window_id, media_type)

class XBMCPlayer(xbmc.Player):
    def __init__(self):
        super().__init__()
        self.media_type = MediaType.NONE

    def onAVStarted(self):
        util.log(ishanga, "ON AV STARTED")
        activate_window_by_media(util.IshangaWindowId.screensaver_window, self.media_type, 5)

    def onPlayBackStarted(self):
        xbmc.executebuiltin('InhibitScreensaver(true)')
        filename = xbmc.Player().getPlayingFile()
        self.media_type = parse_media_type(filename)
        util.log(ishanga, f"VIDEO PLAYBACK STARTED FOR {filename}")

        activate_window_by_media(util.IshangaWindowId.screensaver_window, self.media_type, 5)
        xbmc.Player.pause(self)     

    def onPlayBackPaused(self):
        util.log(ishanga, "VIDEO IS PAUSED. SCREENSAVER ON")
        activate_window_by_media(util.IshangaWindowId.screensaver_window, self.media_type)

    def onPlayBackResumed(self):
        util.log(ishanga, "VIDEO HAS RESUMED. SCREENSAVER OFF")
        activate_window_by_media(util.KodiWindowId.video_window, self.media_type)

    def onPlayBackSeek(self, time, seekOffset):
        # xbmc.Player.pause(self)
        util.log(ishanga, "VIDEO PLAYBACK SEEK")
        activate_window_by_media(util.KodiWindowId.video_window, self.media_type)

    def onPlayBackEnded(self):
        util.log(ishanga, "VIDEO PLAYBACK ENDED")
        xbmc.executebuiltin(f'ActivateWindow({util.KodiWindowId.screensaver_window})')
        # xbmc.executebuiltin(f'Playlist.Clear()')

        # xbmc.executebuiltin(f'ActivateWindow({util.KodiWindowId.screensaver_window})')
        # xbmc.executebuiltin('Container.Refresh()')
        # xbmc.executebuiltin(f'Action(Stop)')