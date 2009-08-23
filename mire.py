import os
import shutil

fullpath='C:/Documents and Settings/Neven Golenic/Desktop/vsa2009/VICTORIA/mire/'

from os.path import join,getsize
for root, files, dirs in os.walk(fullpath):
    for images in files:
        zv = images
        ime_zv = zv[:-5]
##	print ime_zv
        f = open(fullpath+zv)
        files=f.readlines()
##        if
        print files
##        for lines in files:
            
