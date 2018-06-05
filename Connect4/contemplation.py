import Queue
from _collections import deque
from _elementtree import Element
import fileinput

from DAO import fetchEntry
from DAO import updateScore, fetchEntry
import DAO


def printTree(boardPosition):
 #   print "hello" + boardPosition
    print "printing the tree"
    queue = deque([])
    queue.append(boardPosition)
    turn = 'P2'
    while(len(queue) != 0):
        boardPosition = queue.popleft()
        currentBoardPosition = fetchEntry(boardPosition)
        print boardPosition + "currentBoardPosition"
        currentTurn = currentBoardPosition['turn']
        if(currentTurn != turn):
            print ""
     #   print "hello1" + boardPosition
#         print currentBoardPosition

        print currentBoardPosition['turn'], currentBoardPosition['tscore'],
      #  print "####" ,currentTurn, turn, currentTurn != turn

        turn = currentTurn
        children = getChildrenArray(currentBoardPosition['tchildrens'])
        putElementsInQueue(queue, children)

def putElementsInQueue(queue, array):
  #  print array
    for element in array:
        if(element != ''):
            queue.append(element)

    
def getChildrenArray(children):
    return children.split(",")

def populateValues(boardPosition):
    currentBoardPosition = fetchEntry(boardPosition);
    if currentBoardPosition['touched']== 1:
        return currentBoardPosition['tscore']
    
    children = currentBoardPosition['tchildrens']
    childlist = children.split(",")
    
    if currentBoardPosition['tscore']==0:
        #print "hello" + currentBoardPosition['turn']
        if (currentBoardPosition['turn'] == "P1"):
            myValue=-100000
        else:
            myValue=100000
    else:
        myValue=currentBoardPosition['tscore']  
        
    if children == '':
        DAO.updateTouched(boardPosition)
        return myValue      
    for child in childlist:
        if currentBoardPosition['turn']=="P1":
            myValue= max(populateValues(child),myValue)
        else:
            myValue= min(populateValues(child),myValue)
    updateScore(boardPosition, myValue)
        #myValue = (details[turn]=="P1") ?max(populateValues(value.boardposition)) :min(sdafs)
    #updateScore(boardPosition, myValue);
    DAO.updateTouched(boardPosition)
    return myValue



fp1 = open("Player1", "r")
fp2 = open("Player2", "r")
movecount = 0
parent = ""
child = ""
score = 0
for line in fp1:
    if not "end" in line:
            line = line.split(",")
            if parent == "":
                line[1]=line[1].replace("\n","")
                DAO.addorupdate(line[0],"player1", line[1], "", "",  0)
            if parent != "":
                line[1]=line[1].replace("\n","")
                DAO.addorupdate(line[0], "player1", line[1], parent, "",  0)
                DAO.updateChild(parent, line[0])
            if len(line) > 2:
                line[1]=line[1].replace("\n","")
                score = line[2].split("=")
                score = score[1]
                DAO.updateLeaf(line[0], score, line[1])
            # print int(score[1])
            movecount += 1
            parent = line[0]
    if "end" in line:
        parent = ""
        
        
        
movecount = 0
parent = ""
child = ""
score = 0
for line in fp2:
    if not "end" in line:
            line = line.split(",")
            if parent == "":
                line[1]=line[1].replace("\n","")
                DAO.addorupdate(line[0],"player2", line[1], "", "",  0)
            if parent != "":
                line[1]=line[1].replace("\n","")
                DAO.addorupdate(line[0], "player2", line[1], parent, "",  0)
                DAO.updateChild(parent, line[0])
            if len(line) > 2:
                line[1]=line[1].replace("\n","")
                score = line[2].split("=")
                score = score[1]
                DAO.updateLeaf(line[0], score, line[1])
            # print int(score[1])
            movecount += 1
            parent = line[0]
    if "end" in line:
        parent = ""
boardP = ". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ";
#printTree(boardP)
s=populateValues(boardP); 
#print s
printTree(boardP)        

        
fp1.close()
        

        
# for line in fp2: 
#     if not line.contains("end") and movecount!=0:
#             line=line.split(",")
#             DAO.addorupdate(line[0], "player2", parent, "", score)
#             if parent!="":
#                 DAO.updatechild(parent,line[0])
#             score= line[2].split("=")
#             #print int(score[1])
#             movecount+=1
#             parent=line[0]
#     if line.contains("end"):
#         parent=""
#         movecount=0
# 
# 
# for line in fp3:
#     if not line.contains("end") and movecount!=0:
#             line=line.split(",")
#             DAO.addorupdate(line[0], "draw", parent, "", score)
#             if parent!="":
#                 DAO.updatechild(parent,line[0])
#             score= line[2].split("=")
#             #print int(score[1])
#             movecount+=1
#             parent=line[0]
#     if line.contains("end"):
#         parent=""
#         movecount=0


        
    
