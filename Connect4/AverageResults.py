'''
Created on Jan 19, 2018

@author: sgarapati
'''
from itertools import count
EndResult = open('ENDRESULTFREQUENT', 'r')
count=-1
numOfRounds=0
l=[]
for i in range(0,6):
    l.append(0)

for line in EndResult:
    print line
    if "NEW ROUND" in line:
        print "yes"
        count=-1
        numOfRounds = numOfRounds+1
    if "NEXT SET" in line:
        count=count+1
    if "WIN TO LOSS Ratio" in line:
        print "count"+str(count)
#         print l[count-1]
        l1=line.split("=")
        ratioString=l1[1]
        ratioNumber= float(ratioString)
        l[count]=l[count]+ratioNumber
EndResult.close()
EndResult1 = open('ENDRESULTFREQUENT', 'a+')
EndResult1.write("AVERAGE RESULTS"+"\n")
for i in range(0,6):
    l[i]=float(l[i])/float(numOfRounds)
    EndResult1.write(str(l[i])+"\n")
EndResult1.close()
# EndResult1.write
#         l[count]=l[count]+
#             WIN TO LOSS Ratio=1.0