import xbmc

log_info = xbmc.LOGINFO
keyboard_script = 'Ishanga Keyboard Script:'

if xbmc.Player().isPlayingVideo():
    xbmc.log(f"{keyboard_script}: start", log_info)
    xbmc.executebuiltin("Action(Left)")
    xbmc.Player().pause()
    xbmc.log(f"{keyboard_script}: VIDEO IS_PLAYING {xbmc.Player().isPlaying()}", log_info)