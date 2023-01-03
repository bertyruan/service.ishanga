import xbmc
import xbmcgui

from resources.lib import utilities as util

keyboard_script = "Ishanga Keyboard Script"

if xbmc.Player().isPlayingVideo() or xbmc.Player().isPlayingAudio():
    xbmc.executebuiltin('InhibitScreensaver(true)')
    util.log(keyboard_script, "SPACE BUTTON TOGGLED")
    xbmc.Player().pause()

elif xbmcgui.getCurrentWindowId() == util.KodiWindowId.screensaver_window:
    xbmc.executebuiltin('InhibitScreensaver(false)')
    xbmc.executebuiltin(f'ActivateWindow({util.KodiWindowId.video_nav_window})')
    util.log(keyboard_script, f"PLAYLIST ENDED")
