import xbmc
import xbmcgui
import xbmcaddon
from enum import Enum

addon = xbmcaddon.Addon()
addon_path = addon.getAddonInfo("path")
addon_name = addon.getAddonInfo("name")

log_info = xbmc.LOGINFO
ishanga = 'Ishanga Service:'

xbmc.log("Ishanga service successfully booted")


class VideoStatus(Enum):
    UNAVAILABLE = 0
    PLAYING = 1
    PAUSED =  2
    ENDED = 3

status = VideoStatus.UNAVAILABLE

class MonitorScreenSaver(xbmc.Monitor):
    def __init__(self, status, player):
        xbmc.log(f"{ishanga} init monitor screen saver", log_info)
        self.status = status
        self.player = player

    def onScreensaverDeactivated(self):
        xbmc.log(f"{ishanga} video status is {self.status['value']}", log_info)
        if self.status['value'] == VideoStatus.PAUSED:
            xbmc.log(f"{ishanga} trying to unpause", log_info)
            self.player.resumePlayer()
        
            
class XBMCPlayer(xbmc.Player):   
    def __init__(self, status):
        self.status = status
        self.playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        self.currentVideo = self.playlist.getposition()
        self.playListId = self.playlist.getPlayListId()

    def onPlayBackStarted(self):
        xbmc.log(f"{ishanga} PLAYBACK STARTED", log_info)
        self.currentVideo = self.playlist.getposition()
        xbmc.Player.pause(self)
       
    def onPlayBackPaused(self):
        self.status['value'] = VideoStatus.PAUSED
        xbmc.executebuiltin('ActivateScreensaver')
        xbmc.log(f"{ishanga} PLAYBACK PAUSED. Screensaver is activated", log_info)

    def onPlayBackEnded(self):
        xbmc.log(f"{ishanga} PLAYBACK ENDED", log_info)
        self.status['value'] = VideoStatus.ENDED
        # xbmc.Player.playnext(self)

    def resumePlayer(self):
        xbmc.log(f"{ishanga} PLAYBACK RESUMED", log_info)
        self.status['value'] = VideoStatus.PLAYING
        xbmc.Player.play(self, item=self.playlist, startpos=self.currentVideo)
        

if __name__ == '__main__':
    xbmc.log(f"{ishanga} successfully booted", log_info)
    status = {
        'value': VideoStatus.UNAVAILABLE,
    }
    player = XBMCPlayer(status)

    ss_monitor = MonitorScreenSaver(status, player)
    while not ss_monitor.abortRequested():
        if ss_monitor.waitForAbort(1):
            xbmc.log(f"{ishanga} shutting down", log_info)
    
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


