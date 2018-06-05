fp=open("Expectedtowin","r")

def exhaustiveExploration(boardposition):
    
    
    print "h"






game=""
movecount=1
for line in fp:
    if not line.contains("end"):
        game+=line+"\n"
        if movecount%2==1:
            line=line.split(",")
            score= line[2].split("=")
            print int(score[1])
    else:
        
        exhaustiveExploration(game)
    movecount+=1
    

