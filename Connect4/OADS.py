import connectfour.board
from connectfour.board import Board
from connectfour.players import negamax
from connectfour import players
import time
from copy import deepcopy
global player1Time
global player1Count 
global player2Time 
global player2Count

player1Time=0
player1Count=0
player2Time=0
player2Count=0


def getSortedPositions(avaialblePositions):
    list = []
    for i in range(0,len(avaialblePositions)):
        list.append((avaialblePositions[i], avaialblePositions[i].getScore(2)))
    list = sorted(list,key=lambda x:(-x[1],x[0]))
    return list;
     
def getTime():
    ts = time.time()
    return ts

def getMovesinTime(board, maxTime):
    maxTime = maxTime/1000.0
    result = []
    start = getTime()
#     board = connectfour.board.Board()
#     board.reset()
    avaialblePositions = Board.getPossibleBoardPositions(board)
    sortedPositions = getSortedPositions(avaialblePositions)
    for i in sortedPositions:
        p1=players.negamax.NegamaxPlayer(2)
#         # print "==============="
#         # print(i[0])
#         # print "==============="
#       
        i[0].playerTurn=1   
        move = p1.getMove(i[0], 1)
        # print "Time Taken : " + str((getTime() - start) * 1000)
        if(getTime()  - start < maxTime):
            result.append((i[0], move))
        else:
            break;
    
    return result;
# board = connectfour.board.Board()
# board.reset()
        
# # print getMovesinTime(board, 500)
def play(board,preComputedSteps,player):
    newBoard = deepcopy(board)
    
    for step in preComputedSteps:
        if(step[0].__str__() == board.__str__()):
            newBoard.placeToken(player,step[1])
            print "Found *******************"
            return (newBoard, 0.005)
    start= getTime()
    p1=players.negamax.NegamaxPlayer(2)
    move = negamax.NegamaxPlayer.getMove(p1,board, player)
    newBoard.placeToken(player,move)
#     # print(newBoard)
#     # print "\n \n"
    return (newBoard,getTime() - start)

def updateTimeAndCountPlayer1(time):
    print "Player 1 Time : " + str(time)
    global player1Time
    global player1Count
    player1Time = player1Time + (time * 1000)
    player1Count = player1Count + 1

def updateTimeAndCountPlayer2(time):
    print "Player 2 Time : " + str(time)
    global player2Time
    global player2Count
    player2Time = player2Time + (time * 1000)
    player2Count = player2Count + 1
    
def isGameOver(board):
        if board.isFull() or not board.isValid() or board.winningState() != 0:
            return True
        else:
            return False


board = connectfour.board.Board()
board.reset()
newBoard = deepcopy(board)
# # print newBoard.__str__() == board.__str__()
# player1= play(board,[(board, 6)],1)
# player2= play(player1[0],[],2)
# player3= play(player2[0],[],1)

player1 = play(board, [], 1)
# print
updateTimeAndCountPlayer1(player1[1])

# print(player1[0])

# print "\n\n"

player2 = play(player1[0], [], 2) 
updateTimeAndCountPlayer2(player2[1])



while(1):
    # print(player2[0])
    if (isGameOver(player2[0]) == False):
        preComputedSteps = getMovesinTime(player1[0],120)
        player1=play(player2[0],preComputedSteps,1)
        updateTimeAndCountPlayer1(player1[1])
        # print(player1[0])
        # print "\n\n"

    else:
        break
    
    if (isGameOver(player1[0]) == False):
        player2=play(player1[0],[],2)
        updateTimeAndCountPlayer2(player2[1])
    else:
        break
        
        
print "player1Time = " + str(player1Time) + " player2Time = " + str(player2Time)
        
print "player1Count = " + str(player1Count) + " player2Count = " + str(player2Count)
    
