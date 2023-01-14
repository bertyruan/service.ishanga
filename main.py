import xbmc
import xbmcgui

from resources.lib import utilities as util
from resources.lib import XBMCPlayer


# file:///D:/berty/isha-foundation/kodi/docs/html/df/dce/group__python__xbmcgui.html#gadb269db9ee11dfa03817f1585b0b1895

ishanga = 'Ishanga Service:'


util.log(ishanga,  "SUCCESSFULLY BOOTED")
xbmc.executebuiltin('InhibitIdleShutdown(true)')

player = XBMCPlayer()
monitor = xbmc.Monitor()

xbmc.executebuiltin(f'ActivateWindow({util.KodiWindowId.screensaver_window})')
while not monitor.abortRequested():
    if monitor.waitForAbort(1):
        # del player
        util.log(ishanga, "SHUTTING DOWN")
