import xbmc
import xbmcgui

log_info = xbmc.LOGINFO
ishanga = 'Ishanga Service:'

# from my code's side the screensaver skin's window id is 1200
# from kodi's internal system, the window id is 11200
# ¯\_(ツ)_/¯
screensaver_window = 1200


class XBMCPlayer(xbmc.Player):
    def onPlayBackStarted(self):
        xbmc.log(f"{ishanga} PLAYBACK STARTED {xbmcgui.getCurrentWindowId()}", log_info)
        xbmc.executebuiltin('Dialog.Close(all, true)')
        xbmc.executebuiltin(f'ActivateWindow({screensaver_window})')
        xbmc.Player.pause(self)     

    def onPlayBackPaused(self):
        xbmc.executebuiltin('Dialog.Close(all, true)')
        xbmc.executebuiltin(f'ActivateWindow({screensaver_window})')
        xbmc.log(f"{ishanga} VIDEO IS PAUSED. SCREENSAVER ON", log_info)

        
if __name__ == '__main__':
    xbmc.log(f"{ishanga} SUCCESSFULLY BOOTED", log_info)
    xbmc.executebuiltin('InhibitScreensaver(true)')
    
    player = XBMCPlayer()
    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        if monitor.waitForAbort(1):
            xbmc.log(f"{ishanga} SHUTTING DOWN", log_info)
