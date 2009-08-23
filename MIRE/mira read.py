import os
import shutil

fullpath= 'F:/VSA2009/mire/'

from os.path import join, getsize
for root, dirs, files in os.walk(fullpath):
    for html in files:
        htmll= html[:-5]
        data = open(fullpath+html, 'r')
        text= data.readlines()
       
        for s in text:
            if 'Coordinates:</a></b> ' in s: 
                ss=s[s.find('Coordinates:</a></b> ')+21:s.find('Coordinates:</a></b> ')+27+21]
                ss=str(ss)
                ss=ss.split(', ')
                #print ss
                ra=ss[0]
                dec=ss[1].split()
                dec=dec[0]
                print htmll, ra, dec
                








##from os.path import join, getsize
##for root, dirs, files in os.walk(fullpath):
##    for html in files:




##if "Coordinates" in data:
##    print line()
##       
      

##import os
##def read_file():
##    file=open(F:/VSA2009/mire/, 'r')
##    text=file.readlines()
##    file.close()
##    return text
##        
