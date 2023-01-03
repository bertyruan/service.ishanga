import xbmc
import xbmcgui


def log(file, text):
    xbmc.log(f"{file}: {text}", xbmc.LOGINFO)

keyboard_script = 'Ishanga Keyboard Script:'
screensaver_window = 11200
video_window = 12005
video_nav_window = 10025

if xbmc.Player().isPlayingVideo() or xbmc.Player().isPlayingAudio():
    log(keyboard_script, "SPACE BUTTON TOGGLED")
    xbmc.Player().pause()

elif xbmcgui.getCurrentWindowId() == screensaver_window:
    xbmc.executebuiltin(f'ActivateWindow({video_nav_window})')
    log(keyboard_script, f"PLAYLIST ENDED")
