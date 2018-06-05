import dataset
# import symmetryContemplation

db = dataset.connect('sqlite:///contemplation.db')
table = db["some"]

# class Node(object):
#     boardposition = ""
#     winfrequency = 0
#     loosefrequency = 0
#     drawfrequency=0
#     score=0
#     parents= {}
#     children = {} 
#     # The class "constructor" - It's actually an initializer 
#     def __init__(self,boardposition, winfrequency, loosefrequency, drawfrequency,score,parents, children):
#         self.boardposition = boardposition
#         self.winfrequency =     winfrequency
#         self.drawfrequency=drawfrequency
#         self.loosefrequency = loosefrequency
#         self.parents= parents
#         self.children =children
#         self.score=score
#         
#         
# def make_student(name, age, major):
#     student = Node(name, age, major)
#     return student

def splitCount(s, count):
     return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]


def getMirrorBoard(board):
    reverseBoard=""
#     board=". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 1 . . 2 2 2 1 1 1 . "
    board=board.replace(" ", "")
#     print board
    listRows = splitCount(board, 7)
#     print listRows
    for row in listRows:
        row= row[::-1]
        reverseBoard+=row
#         print row
#     print reverseBoard
    reverseBoard = reverseBoard.replace("", " ")[1: -1]+" "
#     print reverseBoard
    return reverseBoard

def addorupdate(boardposition, endresult, turn1, parent, child, score):
    if(table.find_one(tboardposition=boardposition) == None):
        parents = ''
        parents += parent
        children = ''
        children += child
        if endresult == "player1":
            table.insert(dict(tboardposition=boardposition, twinfrequency=1, tloosefrequency=0, tdrawfrequency=0, turn=turn1, tscore=score, tparents=parents, tchildrens=children,touched=0))
        if endresult == "player2":
            table.insert(dict(tboardposition=boardposition, twinfrequency=0, tloosefrequency=1, tdrawfrequency=0, turn=turn1, tscore=score, tparents=parents, tchildrens=children,touched=0))
        if endresult == "draw":
            table.insert(dict(tboardposition=boardposition, twinfrequency=0, tloosefrequency=0, tdrawfrequency=1, turn=turn1, tscore=score, tparents=parents, tchildrens=children,touched=0))
        print "inserting"
    else:
        x = table.find(tboardposition=boardposition)
        for l in x:
            score=l['tscore']
            if endresult == "player1":
                winfrequency = l['twinfrequency']
                winfrequency += 1
                parents = l['tparents']
                childrens = l['tchildrens']
                if parent not in parents:
                    parents += "," + parent
                if child not in childrens:
                    childrens += "," + child
                loosefrequency = l['tloosefrequency']
                drawfrequency = l['tdrawfrequency']
                table.update(dict(tboardposition=boardposition, twinfrequency=winfrequency, tloosefrequency=loosefrequency, tdrawfrequency=drawfrequency, turn=turn1,tscore=score, tparents=parents, tchildrens=childrens,touched=0), 'tboardposition')
            if endresult == "player2":
                winfrequency = l['twinfrequency']
                parents = l['tparents']
                childrens = l['tchildrens']
                if parent not in parents:
                    parents += "," + parent
                if child not in childrens:
                    childrens += "," + child
                loosefrequency = l['tloosefrequency']
                loosefrequency += 1
                drawfrequency = l['tdrawfrequency']
                table.update(dict(tboardposition=boardposition, twinfrequency=winfrequency, tloosefrequency=loosefrequency, tdrawfrequency=drawfrequency,turn=turn1, tscore=score, tparents=parents, tchildrens=childrens,touched=0), 'tboardposition')
            if endresult == "draw":
                winfrequency = l['twinfrequency']
                parents = l['tparents']
                childrens = l['tchildrens']
                if parent not in parents:
                    parents += "," + parent
                if child not in childrens:
                    childrens += "," + child
                loosefrequency = l['tloosefrequency']
                drawfrequency = l['tdrawfrequency']
                drawfrequency += 1
                table.update(dict(tboardposition=boardposition, twinfrequency=winfrequency, tloosefrequency=loosefrequency, tdrawfrequency=drawfrequency, turn=turn1,tscore=score, tparents=parents, tchildrens=childrens,touched=0), 'tboardposition')
            print "updating"
    
def updateChild(boardposition, child):   
    print "updatechild"
    x = table.find(tboardposition=boardposition)
    for l in x:
        childrens = l['tchildrens']
        if not child in childrens:
            if childrens != '':
                childrens += ','
            childrens += child
            winfrequency = l['twinfrequency']
            parents = l['tparents']
            loosefrequency = l['tloosefrequency']
            drawfrequency = l['tdrawfrequency']
            turn=l['turn']
            score = 0
            table.update(dict(tboardposition=boardposition, twinfrequency=winfrequency, tloosefrequency=loosefrequency, tdrawfrequency=drawfrequency, turn=turn,tscore=score, tparents=parents, tchildrens=childrens,touched=0), 'tboardposition')
          
def updateScore(boardposition, score):
    print "scoreupdate"
    x = table.find(tboardposition=boardposition)
    for l in x:
            winfrequency = l['twinfrequency']
            parents = l['tparents']
            childrens = l['tchildrens']
            loosefrequency = l['tloosefrequency']
            drawfrequency = l['tdrawfrequency']
            turn=l['turn']
            table.update(dict(tboardposition=boardposition, twinfrequency=winfrequency, tloosefrequency=loosefrequency, tdrawfrequency=drawfrequency,turn=turn, tscore=score, tparents=parents, tchildrens=childrens,touched=0), 'tboardposition')
          
def fetchEntry(boardPosition):
    x=table.find(tboardposition=boardPosition)
    for l in x:
        return l
    

def updateTouched(boardPosition):
     x=table.find(tboardposition=boardPosition)
     for l in x:
            winfrequency = l['twinfrequency']
            parents = l['tparents']
            childrens = l['tchildrens']
            loosefrequency = l['tloosefrequency']
            drawfrequency = l['tdrawfrequency']
            turn=l['turn']
            score = l['tscore']
            table.update(dict(tboardposition=boardPosition, twinfrequency=winfrequency, tloosefrequency=loosefrequency, tdrawfrequency=drawfrequency,turn=turn, tscore=score, tparents=parents, tchildrens=childrens,touched=1), 'tboardposition')
                  
               
def updateLeaf(boardposition, score, turn):
    print "scoreupdate"
    x = table.find(tboardposition=boardposition)
    for l in x:
            winfrequency = l['twinfrequency']
            parents = l['tparents']
            childrens = l['tchildrens']
            loosefrequency = l['tloosefrequency']
            drawfrequency = l['tdrawfrequency']
#             turn=l['turn']
            table.update(dict(tboardposition=boardposition, twinfrequency=winfrequency, tloosefrequency=loosefrequency, tdrawfrequency=drawfrequency,turn=turn, tscore=score, tparents=parents, tchildrens=childrens,touched=0), 'tboardposition')
           
def getNumberOfNodes():
    return len(db["some"])

def getElementsFromDB():
    nodes = db["some"].all()
    return nodes

def isAvailableInTable(boardposition):
        if(table.find_one(tboardposition=boardposition) == None):
            return 0
        else:
            return 1
        
def insertMirrorToTable(boardPosition, mirrorBoardPosition):
        print "inserting mirror node"
        x = table.find(tboardposition=boardPosition)
        for l in x:
            winfrequency = l['twinfrequency']
            parents = l['tparents']
            newParentList = ""
            if parents != "":
                parentList = parents.split(",")
                for parent in parentList:
                    mirrorParent = getMirrorBoard(parent)
                    if newParentList != "":
                        newParentList = newParentList + "," + mirrorParent
                    else:
                        newParentList = newParentList + mirrorParent
            else:
                newParentList=parents
            childrens = l['tchildrens']
            newChildList=""
            if childrens !="":
                childList = childrens.split(",")
                for child in childList:
                    mirrorChild=getMirrorBoard(child)
                    if newChildList!="":
                        newChildList= newChildList+ "," +mirrorChild
                    else:
                        newChildList=newChildList+mirrorChild
            else:
                newChildList=childrens
            loosefrequency = l['tloosefrequency']
            drawfrequency = l['tdrawfrequency']
            turn=l['turn']
            score = l['tscore']
            print mirrorBoardPosition+"mirrorBoard"
            print newParentList+"newParentList"
            print newChildList+"newChildList"
            print boardPosition+"actualBoardPosition"
            table.insert(dict(tboardposition=mirrorBoardPosition, twinfrequency=winfrequency, tloosefrequency=loosefrequency, tdrawfrequency=drawfrequency,turn=turn, tscore=score, tparents=newParentList, tchildrens=newChildList,touched=1))
                  
        


# addorupdate("board1", "player1", "boardp", "", 0)
# addorupdate("board1", "player1", "boardp", "", 0)
# updatechild("board1", "boardl")
# updatechild("board1", "boardp")   
# addorupdate("board2", "player1", "boardp", "", 0)
# addorupdate("board3", "player2", "boardk", "", 100)
# 
# print table.find_one(tboardposition='board1')
# print table.find_one(tboardposition='board2')
# print table.find_one(tboardposition='board3')


# table.insert(dict(name='John Doe', age=37))
# table.insert(dict(name='Jane Doe', age=34, gender='female'))

# john = table.find_one(name='John Doe')


