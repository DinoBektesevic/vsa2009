import os
import shutil

fullpath='C:/Python24/mire/'

gice=open(fullpath+'output.txt','w')
from os.path import join,getsize
for root, dirs, files in os.walk(fullpath):
    for images in files:
        zv = images
        ime_zv = zv[:-5]
	#print ime_zv
        f = open(fullpath+zv)
        gice.write(str(ime_zv)+'           ')

        files=f.readlines()
##        print file
        for lines in files:
            if 'Coordinates:</a></b>' in lines:
                mice=lines[lines.find('Coordinates:</a></b>')+21:lines.find('Coordinates:</a></b>')+27+21]
                mice=str(mice)
                #print mice
                mice=mice.split(',')
                gica1 = mice[0]
                gica2 = mice[1]
                print ime_zv,gica1,gica2
                gice.write(gica1+','+gica2)
##            gice.write('\n')
            
        f.close()
gice.close()
