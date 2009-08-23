import os
import RMSastro as RMS
fullpath='F:/VSA2009/VSS/plots/Variable/'


k=0
from os.path import join, getsize
for root, dirs, files in os.walk(fullpath):
    for image in files:
        ime = image[5:6]
        a = image[8:]
        a = a[:-4]
        #print ime,a
        f= open('F:/VSA2009/VSS/' + str(ime) + 'stars.txt')
        red = f.readlines()[int(a)]
        red = red.split()
        f1 = open('F:/VSA2009/VSS/' + str(ime) + 'stars_mag.txt')
        magred= f1.readlines()[int(a)]
        magred = magred.split()
        k = 0
        magred=magred[k]
        k=k+1
        print 'Star'+str(a)+'     '+str(RMS.RAdec_to_RAsex(red[0]))+'    '+ str(RMS.DEdec_to_DEsex(red[1]))+'       ',str(round(float(magred), 2))
        
f.cl ose()
f1.close()    
    
    
    

    
