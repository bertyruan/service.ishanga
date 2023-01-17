import xbmc
import xbmcgui

from resources.lib import utilities as util

keyboard_script = "Ishanga Keyboard Script"

if xbmc.Player().isPlayingVideo() or xbmc.Player().isPlayingAudio():
    util.log(keyboard_script, "SPACE BUTTON TOGGLED")
    xbmc.Player().pause()

elif util.KodiWindowId().screensaver_ids.count(xbmcgui.getCurrentWindowId()):
    xbmc.executebuiltin('InhibitScreensaver(false)')
    xbmc.executebuiltin('Dialog.Close(all, true)')
    xbmc.executebuiltin(f'ActivateWindow({util.KodiWindowId.video_nav_window})')
    util.log(keyboard_script, f"PLAYLIST ENDED")
