import xbmc
import xbmcgui
import sys 

ishanga = 'Ishanga Service:'
# file:///D:/berty/isha-foundation/kodi/docs/html/df/dce/group__python__xbmcgui.html#gadb269db9ee11dfa03817f1585b0b1895

# from my code's side the screensaver skin's window id is 1200
# from kodi's internal system, the window id is 11200
# ¯\_(ツ)_/¯
screensaver_window = 1200
video_window = 12005

def log(file, text):
    xbmc.log(f"{file}: {text}", xbmc.LOGINFO)

def activate_window(window_id):
    if not xbmcgui.getCurrentWindowId() == window_id: 
        xbmc.executebuiltin('Dialog.Close(all, true)')
        xbmc.executebuiltin(f'ActivateWindow({window_id})')

class XBMCPlayer(xbmc.Player):
    def onPlayBackStarted(self):
        log(ishanga, f"playlist id {xbmc.PlayList(xbmc.PLAYLIST_VIDEO).getPlayListId()}") 
        log(ishanga, "PLAYBACK STARTED")
        activate_window(screensaver_window)
        xbmc.Player.pause(self)     

    def onPlayBackPaused(self):
        activate_window(screensaver_window)
        log(ishanga, "VIDEO IS PAUSED. SCREENSAVER ON")

    def onPlayBackResumed(self):
        activate_window(video_window)

    def onPlayBackSeek(self, time, seekOffset):
        # xbmc.Player.pause(self)
        log(ishanga, "PLAYBACK SEEK")
        activate_window(video_window)

        
if __name__ == '__main__':
    log(ishanga,  "SUCCESSFULLY BOOTED")
    xbmc.executebuiltin('InhibitScreensaver(true)')
    xbmc.executebuiltin('InhibitIdleShutdown(true)')
    
    # base_url = sys.argv[0]
    # addon_handle = int(sys.argv[1])
    # args =  sys.argv[2]
    # log(ishanga, f"{base_url}, {addon_handle}, {args}")
    log(ishanga, sys.argv)
    player = XBMCPlayer()
    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        if monitor.waitForAbort(1):
            log(ishanga, "SHUTTING DOWN")
