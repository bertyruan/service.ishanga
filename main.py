import xbmc
import xbmcgui

log_info = xbmc.LOGINFO
ishanga = 'Ishanga Service:'

# from my code's side the screensaver skin's window id is 1200
# from kodi's internal system, the window id is 11200
# ¯\_(ツ)_/¯
screensaver_window = 1200
video_window = 12005

def activate_window(window_id):
    if not xbmcgui.getCurrentWindowId() == window_id: 
        xbmc.executebuiltin('Dialog.Close(all, true)')
        xbmc.executebuiltin(f'ActivateWindow({window_id})')

class XBMCPlayer(xbmc.Player):
    def onPlayBackStarted(self):
        xbmc.log(f"{ishanga} playlist id {xbmc.PlayList(xbmc.PLAYLIST_VIDEO).getPlayListId()}", log_info)
        xbmc.log(f"{ishanga} PLAYBACK STARTED", log_info)
        activate_window(screensaver_window)
        xbmc.Player.pause(self)     

    def onPlayBackPaused(self):
        activate_window(screensaver_window)
        xbmc.log(f"{ishanga} VIDEO IS PAUSED. SCREENSAVER ON", log_info)

    def onPlayBackResumed(self):
        activate_window(video_window)

    def onPlayBackSeek(self, time, seekOffset):
        # xbmc.Player.pause(self)
        xbmc.log(f"{ishanga} PLAYBACK SEEK", log_info)
        activate_window(video_window)

        
if __name__ == '__main__':
    xbmc.log(f"{ishanga} SUCCESSFULLY BOOTED", log_info)
    xbmc.executebuiltin('InhibitScreensaver(true)')
    xbmc.executebuiltin('InhibitIdleShutdown(true)')
    
    player = XBMCPlayer()
    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        if monitor.waitForAbort(1):
            xbmc.log(f"{ishanga} SHUTTING DOWN", log_info)
