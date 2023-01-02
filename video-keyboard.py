import xbmc
import xbmcgui

def log(file, text):
    xbmc.log(f"{file}: {text}", xbmc.LOGINFO)


keyboard_script = 'Ishanga Keyboard Script:'
screensaver_window = 11200
video_window = 12005
video_nav_window = 10025

if xbmc.Player().isPlayingVideo():
    log(keyboard_script, "STARTS")
    xbmc.executebuiltin('Dialog.Close(all, true)')
    xbmc.executebuiltin(f'ActivateWindow({video_window})')
    xbmc.Player().pause()
    log(keyboard_script, f"VIDEO IS_PLAYING {xbmc.Player().isPlaying()}")

elif xbmcgui.getCurrentWindowId() == screensaver_window:
    xbmc.executebuiltin(f'ActivateWindow({video_nav_window})')
    log(keyboard_script, f"window id is {xbmcgui.getCurrentWindowId()}")
