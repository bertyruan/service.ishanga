import xbmc
import xbmcgui
import sys 


# file:///D:/berty/isha-foundation/kodi/docs/html/df/dce/group__python__xbmcgui.html#gadb269db9ee11dfa03817f1585b0b1895

# from my code's side the screensaver skin's window id is 1200
# from kodi's internal system, the window id is 11200
# ¯\_(ツ)_/¯
screensaver_window = 1200
video_window = 12005
AudioExtensions = ['.mp3']
ishanga = 'Ishanga Service:'

class MediaType:
    NONE = 0
    VIDEO = 1
    AUDIO = 2

def log(file, text):
    xbmc.log(f"{file}: {text}", xbmc.LOGINFO)

def parse_media_type(filename):
    idx = filename.rfind('.')
    file_ext = filename[idx:]
    
    log(ishanga, file_ext)

    if AudioExtensions.count(file_ext):
        log(ishanga, "AN AUDIO FILE IS PLAYING")
        return MediaType.AUDIO
    return MediaType.VIDEO

def activate_window(window_id, media_type):
    if media_type == MediaType.AUDIO:
        xbmc.executebuiltin('Dialog.Close(all, true)')
        xbmc.executebuiltin(f'ActivateWindow({screensaver_window})')
        return

    if not xbmcgui.getCurrentWindowId() == window_id: 
        xbmc.executebuiltin('Dialog.Close(all, true)')
        xbmc.executebuiltin(f'ActivateWindow({window_id})')



class XBMCPlayer(xbmc.Player):
    def __init__(self):
        super().__init__()
        self.media_type = MediaType.NONE

    def onPlayBackStarted(self):
        log(ishanga, "PLAYBACK STARTED")
        filename = xbmc.Player().getPlayingFile()
        self.media_type = parse_media_type(filename)
        activate_window(screensaver_window, self.media_type)
        xbmc.Player.pause(self)     

    def onPlayBackPaused(self):
        activate_window(screensaver_window, self.media_type)
        log(ishanga, "VIDEO IS PAUSED. SCREENSAVER ON")

    def onPlayBackResumed(self):
        activate_window(video_window, self.media_type)

    def onPlayBackSeek(self, time, seekOffset):
        # xbmc.Player.pause(self)
        log(ishanga, "PLAYBACK SEEK")
        activate_window(video_window, self.media_type)

        
if __name__ == '__main__':
    log(ishanga,  "SUCCESSFULLY BOOTED")
    xbmc.executebuiltin('InhibitScreensaver(true)')
    xbmc.executebuiltin('InhibitIdleShutdown(true)')

    player = XBMCPlayer()
    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        if monitor.waitForAbort(1):
            log(ishanga, "SHUTTING DOWN")
