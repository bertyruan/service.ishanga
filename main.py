import xbmc
import xbmcgui

log_info = xbmc.LOGINFO
ishanga = 'Ishanga Service:'

# try ActivateWindow(1200) for custom window, InhibitScreensaver(true/false)
# try xbmcgui.Window(10025).onAction(self, action)

class XBMCPlayer(xbmc.Player):
    def onPlayBackStarted(self):
        xbmc.log(f"{ishanga} PLAYBACK STARTED", log_info)
        xbmc.Player.pause(self)
        xbmc.executebuiltin('ActivateScreensaver')

    def onPlayBackPaused(self):
        # xbmcgui.Dialog().textviewer("", "")
        xbmc.executebuiltin('ActivateScreensaver')
        xbmc.log(f"{ishanga} VIDEO IS PAUSED. SCREENSAVER ON", log_info)

        
if __name__ == '__main__':
    xbmc.log(f"{ishanga} SUCCESSFULLY BOOTED", log_info)
    player = XBMCPlayer()
    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        if monitor.waitForAbort(1):
            xbmc.log(f"{ishanga} SHUTTING DOWN", log_info)
