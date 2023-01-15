import xbmc
import xbmcgui

from resources.lib import utilities as util

keyboard_script = "Ishanga Keyboard Script"
screensaver_ids = [util.KodiWindowId.audio_screensaver_window, util.KodiWindowId.screensaver_window]

if xbmc.Player().isPlayingVideo() or xbmc.Player().isPlayingAudio():
    util.log(keyboard_script, "SPACE BUTTON TOGGLED")
    xbmc.Player().pause()

elif screensaver_ids.count(xbmcgui.getCurrentWindowId()):
    xbmc.executebuiltin(f'ActivateWindow({util.KodiWindowId.video_nav_window})')
    util.log(keyboard_script, f"PLAYLIST ENDED")
