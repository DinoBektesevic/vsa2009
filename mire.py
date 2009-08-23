import os
import shutil

fullpath='C:/Python24/mire/'

gice=open(fullpath+'output.txt','w')
from os.path import join,getsize
for root, files, dirs in os.walk(fullpath):
    for images in files:
        zv = images
        ime_zv = zv[:-5]
	print ime_zv
        f = open(fullpath+zv)
        gice.write(str(ime_zv)+'           ')

        files=f.readlines()
##        print files
        c=0
        for lines in files:
            c = c+1
            if c== 43:
                gica1=lines[59:69]
                gica2=lines[72:82]
                gice.write(gica1+'    '+gica2+'\n')
            
        f.close()
gice.close()
