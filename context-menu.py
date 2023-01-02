import xbmc 
import sys

xbmc.executebuiltin(f"PlayMedia({sys.listitem.getPath()}, isdir=true)")