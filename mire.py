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
        for lines in files:
        c=c+1
        if c==43:
            gica1=lines[59:69]
            gica2=lines[72:82]
            
            
