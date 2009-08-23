import RMSastro as RMS

file1=open('F:/VSA2009/pod.txt', 'r')
text=file1.readlines()
for line in text:
    line=line.split()
    ra=line[1]
    dec=line[2]
    ra2=RMS.RAsex_to_RAdec(ra)
    dec2=RMS.DEsex_to_DEdec(dec)
    ra3=ra2*15.0
    print ra3, dec2
    
