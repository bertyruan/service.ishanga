import xbmc
import xbmcgui
import xbmcaddon
from inputs import get_key

addon = xbmcaddon.Addon()
addon_path = addon.getAddonInfo("path")
addon_name = addon.getAddonInfo("name")

monitor = xbmc.Monitor()
log_info = xbmc.LOGINFO
ishanga = 'Ishanga Service:'
# xbmc.executebuiltin('ActivateScreensaver')
# xbmcgui.Dialog().ok(addon_name, "Namaskaram Ishanga")
xbmc.log("Ishanga service successfully booted")


class XBMCPlayer(xbmc.Player):   
    def onPlayBackStarted(self, *file):
        xbmc.Player.pause(self)
        xbmc.executebuiltin('ActivateScreensaver')
        xbmc.log(f"{ishanga} video paused and screensaver is activated", log_info)
    
    # def onPlayBackPaused(self): 
    #     xbmc.log(f"Hello world", log_info)
    #     while 1:
    #         xbmc.log(f"Hello world", log_info)
    #         events = get_key()
    #         if events:
    #             for event in events:
    #                 xbmc.log(f"{ishanga} {event.ev_type}, {event.code}, {event.state}", log_info)

        
        # pressed_key = KeyListener.record_key()
        # if pressed_key == 'VK_SPACE':
        #     xbmc.Player.play(self)
        # exit = False
        # while not exit:
        #     kb = xbmc.Keyboard(line='default', heading='heading', hidden=True)
        #     kb.setDefault('Berty')
        #     kb.setHeading('Hello world')
        #     kb.setHidden
        #     kb.doModal() 
        #     if kb.isConfirmed():
        #         xbmc.log(f"Got input: {kb.getText()}")
        #         exit = True

    # def onPlayBackEnded(self, *args):
    #     xbmc.log(f"{ishanga} playing next video", log_info)
    #     xbmc.Player.playnext(self)


        
if __name__ == '__main__':
    xbmc.log(f"{ishanga} successfully booted")
    player = XBMCPlayer()
    while not monitor.abortRequested():
        if monitor.waitForAbort(1):
            xbmc.log(f"{ishanga} shutting down", log_info)