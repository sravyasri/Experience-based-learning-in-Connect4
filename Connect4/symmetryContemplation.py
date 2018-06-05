import DAO
from DAO import getElementsFromDB
symmetryUsed=0

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


# mirrorBoard=getMirrorBoard()
nodes = DAO.getElementsFromDB()
for node in nodes:
#     print "printing each node"
#     print node
    board = node['tboardposition']
    mirrorBoard = getMirrorBoard(board)
    if(DAO.isAvailableInTable(mirrorBoard)==0):
        DAO.insertMirrorToTable(board,mirrorBoard)
        symmetryUsed=symmetryUsed+1
    else:
        print mirrorBoard+"\n"
        print "already available"
#         //insert in table
