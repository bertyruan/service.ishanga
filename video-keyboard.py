import xbmc
import xbmcgui

log_info = xbmc.LOGINFO
keyboard_script = 'Ishanga Keyboard Script:'
screensaver_window = 11200
video_window = 12005
video_nav_window = 10025

if xbmc.Player().isPlayingVideo():
    xbmc.log(f"{keyboard_script}: start", log_info)
    xbmc.executebuiltin('Dialog.Close(all, true)')
    xbmc.executebuiltin(f'ActivateWindow({video_window})')
    xbmc.Player().pause()
    xbmc.log(f"{keyboard_script}: VIDEO IS_PLAYING {xbmc.Player().isPlaying()}", log_info)

elif xbmcgui.getCurrentWindowId() == screensaver_window:
    xbmc.executebuiltin(f'ActivateWindow({video_nav_window})')
    xbmc.log(f"{keyboard_script} window id is {xbmcgui.getCurrentWindowId()}", log_info)
