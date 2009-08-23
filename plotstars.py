import sys
import shutil
import RMSastro as RMS
from pylab import *
import scipy
from numpy import *
from matplotlib import rcParams


path='F:/VSA2009/VSS/9'   #######################


mag=[]
sigma=[]
JDT=[]
stars = zeros([10000,300])



fa= open(path+'stars_mag.txt')
for line in fa:
    line=line.split()
    magv=line[0]
    #print magv
    mag.append(float(magv))
fa.close()

fa= open(path+'stars_sigma.txt')
for line in fa:
    line=line.split()
    sigmav=line[0]
    sigma.append(float(sigmav))
fa.close()

fa= open(path+'stars_JDT.txt')
for line in fa:
    line=line.split()
    jdtv=line[0]
    JDT.append(float(jdtv))
fa.close()

fa= open(path+'stars.txt')
i=0
for line in fa:
    line=line.split()
    for j in range (0,300):
        stars[i][j]=float(line[j])
    i=i+1
fa.close()

JDTmin=float(JDT[0])
JDTmax=float(JDT[len(JDT)-1])

for i in range(0, len(mag)):
    plotmag=[]
    plotJDT=[]
    for j in range(0, len(JDT)):
        if float(stars[i][j+2]) != 0.0:
            plotmag.append(stars[i][j+2]-mag[i])
            plotJDT.append((float(JDT[j])-JDTmin)*24.0)
            
    figtext(0.05, 0.93, 'Star'+str(i)+'     JDstart: '+ str(JDTmin)+'      RA: '+str(RMS.RAdec_to_RAsex(stars[i][0]))+'    DEC: '+ str(RMS.DEdec_to_DEsex(stars[i][1]))+'          Mag: '+str(round(mag[i], 1)), fontsize=12)

    plot(plotJDT, plotmag, '.')
    axis([0, max(plotJDT), 0.5, -0.5])
    xlabel('time (h)')
    ylabel('mag')
    savefig('plots/star-9b-'+str(i)+'.png')
    clf()
    print 'Star'+str(i)+':  '+ str(RMS.RAdec_to_RAsex(stars[i][0]))+'    '+ str(RMS.DEdec_to_DEsex(stars[i][1]))+'    '+str(round(mag[i], 1))+'     ' +str(round(sigma[i],3))



#for i in range(0, len(mag)):
 #   if i==218 or i==515 or i==561 or i==646 or i==1379 or i==1423 or i==1445 or i==1448 or i==2067 or i==2693:
  #      print 'Star'+str(i)+':  '+ str(RMS.RAdec_to_RAsex(stars[i][0]))+'    '+ str(RMS.DEdec_to_DEsex(stars[i][1]))+'    '+str(round(mag[i], 1))+'     ' +str(round(sigma[i],3))


##plot(mag, sigma, '.b')
##show()
