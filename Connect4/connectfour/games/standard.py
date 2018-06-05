from copy import deepcopy
from findertools import move
import random
import DAO

import connectfour
import connectfour.players as players
from DAO import fetchEntry


# import DAO
class StandardGame:

    def __init__(self, p1=players.human.HumanPlayer(), p2=players.random.RandomPlayer(), verbose=True):
        """
        Constructor
        """
        self.board = connectfour.board.Board()
        self.tempboard = connectfour.board.Board()
        self.players = { 1: p1, 2: p2 }
        self.verbose = verbose
        # self.tempfile=open("tempfile","w")
        self.gamemoves = ""
        self.Player1 = open('Player1', 'a+')
        self.Player2 = open('Player2', 'a+')
        self.Draw = open('Draw', 'a+')
        self.movecount = 0
        self.bestmovescount1 = 0
        self.bestmovescount2 = 0
        self.expectedtowin = open('ExpectedtoWin', 'a+')
        self.experiencebase = 0
        self.pointAdvantage= 0

    def printGameBoard(self):
         # print 0, 1, 2, 3, 4, 5, 6
         # print self.board.__str__()
         self.gamemoves += self.board.__str__().replace("\n", "")
         # self.gamemoves+=self.board.__str__()


    def isGameOver(self):
        if self.board.isFull() or not self.board.isValid() or self.board.winningState() != 0:
            return True
        else:
            return False
    
    def getNumberofUnfilledColumns(self, boad): 
        unfilled = 0
        for x in xrange(0, 7):
            if not self.board.isColumnFull(x):
                unfilled = unfilled + 1
#         print "unfilledcolumns",unfilled
#         print unfilled
#         print self.board
        return unfilled
    
    def getBoardFromMove(self, move, tempboard, player):
        self.tempboard = tempboard
#         print "get board from move", player,move
        self.tempboard.placeToken(player, move)
#         print self.tempboard
        tempboard1 = self.tempboard.__str__().replace("\n", "")
        return tempboard1
       
    def getPositionDifference(self, a, b):
#         print "len"
#         print len(a),len(b)
        return [i for i in range(len(a)) if a[i] != b[i]] 
    
    def getMoveFromBoard(self, board1, board2):
#         print "get move from board"
        board1 = board1.replace(" ", "")
        board2 = board2.replace(" ", "")
        diff = self.getPositionDifference(board1, board2)
        if len(diff) == 1:
                # print diff[0]
                move = diff[0] % 7
                # print "moves"
                # print move
#                 print move
                return move
        else:
            print "SOMETHING WRONG"
        
    def getExperienceBasedLearningMove(self, board, player):
            print "gettingExperienceBasedLearningMove"
#             print "came"
            board1 = board.__str__().replace("\n", "")
            currentBoardEntry = fetchEntry(board1)
#             print currentBoardEntry['tboardposition']
            children = currentBoardEntry['tchildrens']
            childList = children.split(",")
#             print childList
            selectedChild = None
            score = -9999
            for child in childList:
                childEntry = fetchEntry(child)
#                 print childEntry['tboardposition']
#                 print childEntry['twinfrequency']
#                 print childEntry['tscore']
                if childEntry['twinfrequency'] > 0 and childEntry['tscore'] > score:
                    selectedChild = childEntry
                    score = childEntry['tscore']
                    # print childEntry['tboardposition']+"Child of  "+board1
#                     print "HaveWinFrequency"
            if selectedChild == None:
                score = -9999
                for child in childList:
                    if childEntry['tscore'] > score:
                        selectedChild = childEntry
                        score = childEntry['tscore']
                unfilledColumns = self.getNumberofUnfilledColumns(board)                    
                if unfilledColumns != len(childList):
#                     print "There are moves to be explored"
#                     print board
                    move = self.players[player].getMove(board, player)
#                     print "move suggested by engine"
#                     print move
                    tempBoard = self.getBoardFromMove(move, board, player)
#                     print board
                    for child in childList:
                        childEntry = fetchEntry(child)
                        if childEntry['tboardposition'] == tempBoard:
#                             print "Already explored"
#                             print childEntry['tboardposition']
#                             print tempBoard
                            m = self.getMoveFromBoard(selectedChild['tboardposition'], board1)
                            self.experiencebase += 1
                            return m
                    return move
                else:
                    m = self.getMoveFromBoard(selectedChild['tboardposition'], board1)
                    self.experiencebase += 1
                    return m 
            else:
                m = self.getMoveFromBoard(selectedChild['tboardposition'], board1)
                self.experiencebase += 1
                return m    
    
    def getFrequentAnalysisMove(self,board,player):
#         print "gettingFrequentAnalysisMove"
        board1 = board.__str__().replace("\n", "")
        currentBoardEntry = fetchEntry(board1)
        children = currentBoardEntry['tchildrens']
        childList = children.split(",")
        selectedChild= None
        maxWinFrequency=0
        for child in childList:
            childEntry = fetchEntry(child)
            if childEntry['twinfrequency'] > maxWinFrequency:
                maxWinFrequency=childEntry['twinfrequency']
                selectedChild=childEntry
        if selectedChild==None:
            move = self.players[player].getMove(board, player)
            return move
        else:
            move = self.getMoveFromBoard(selectedChild['tboardposition'], board1)
            self.experiencebase += 1
            return move

    

    def takeTurn(self, player,typeOfLearning):
#         print self.movecount
#         print "movecount"
        # print player
        if self.verbose:
            self.printGameBoard()
            # if not self.players[player].isHuman():
            #    print 
                # print "%s is thinking..." % self.players[player].getName()

        # make a copy so it doesn't mess with the game
        board = deepcopy(self.board)
        if self.movecount == 1 or self.movecount == 2:
            move = players.random.RandomPlayer().getMove(board, player)
        else:
            if player == 1:
                board1 = board.__str__().replace("\n", "")
                if DAO.fetchEntry(board1) != None:
                    if typeOfLearning=="Experience":
                        move = self.getExperienceBasedLearningMove(board, player)  # Experience Based learning logic to get the best move
                    if typeOfLearning=="Frequent":
                        move = self.getFrequentAnalysisMove(board, player)
#                     print "experienceBaseMove="+ str(move) 
#                     print "board=" + str(board1)
                else:
                    move = self.players[player].getMove(board, player)
            else:
                move = self.players[player].getMove(board, player)
        scorebefore = self.board.getScore(player)
        self.board.placeToken(player, move)
        scoreafter = self.board.getScore(player)
        scoreofmove = scoreafter - scorebefore
#         print "scoreafter"
#         print scoreafter
#         print "scorebefore"
#         print scorebefore
        if scoreofmove > 5:
            if player == 1:
                self.bestmovescount1 += 1
            if player == 2:
                self.bestmovescount2 += 1
        
        if self.verbose:
#             print "Player "+str(player)+" ("+self.players[player].getName()+") places in column " + str(move) + ":"
#             self.gamemoves+= ","+ "move="+str(move)+","+"score="+str(scoreofmove)+"\n"
            self.gamemoves += "," + "P" + str(player) + "\n"

#             self.gamemoves+= ","+ "move="+str(move)+","+"score="+str(scoreofmove)+"\n"

            # print self.move+"move number:      
    def getWinner(self):
        if not self.board.isValid():
            return None
        else:
            return self.board.winningState()

    def getTurns(self):
        return self.board.getNumberOfMoves()

    def getMoves(self):
        return self.board.getMoves()

    def getBoard(self):
        return self.board

    def getPlayer(self, player):
        return players[player]

    def play(self,typeOfLearning):
        self.board.reset()
        
        while not self.isGameOver():
            self.movecount = self.movecount + 1
#             if self.movecount
            self.takeTurn(1,typeOfLearning)
            # is this the end?
            if (self.isGameOver()):
                break
            
            self.movecount = self.movecount + 1
            self.takeTurn(2,typeOfLearning)    

        if self.verbose:
            self.printGameBoard()
            if not self.board.isValid():
                print "The game board somehow became invalid! No winner!"
            else:       
                # self.gamemoves= self.gamemoves[:self.gamemoves.rfind('\n')]
                if not self.board.winningState() == 0:
                    print "Player " + str(self.board.winningState()) + " (" + self.players[self.board.winningState()].getName() + ") wins in " + str(self.getTurns()) + " turns."
                    if self.board.winningState() == 2:
                        if self.bestmovescount1 > self.movecount / 4:
                                # self.Player1.write("Expectedtowin")
                                self.expectedtowin.write(self.gamemoves + "\n")
                                self.expectedtowin.write("end" + "\n")
                        scoresarray = self.board.getRawScores()
                        self.gamemoves += "," + "P1" + "," + "Value=" + str(scoresarray[3])
                        self.Player2.write(str(self.gamemoves) + "\n" + "end" + "\n")
                        self.pointAdvantage=scoresarray[3]
                        # print self.getBoard().getScore(2)
                    else:
                        scoresarray = self.board.getRawScores()
                        # print "GAMEMOVES"
                        # print self.gamemoves
                        self.gamemoves += "," + "P2" + "," + "Value=" + str(scoresarray[3])
                        self.Player1.write(str(self.gamemoves) + "\n" + "end" + "\n")
                        self.pointAdvantage=scoresarray[3]
                        # print self.getBoard().getScore(1)
                        
                else:
                    print "Draw in " + str(str(self.getTurns())) + " turns."
                    self.Draw.write(self.gamemoves + "\n") + "end" + "\n"
                print
                self.Player1.close()
                self.Player2.close()
                self.Draw.close()
                self.expectedtowin.close()
    
    def getUsageOfExperienceBase(self):
        return self.experiencebase
    
    def getNumberOfMovesOfEachPlayer(self):
        x = self.movecount / 2
        return x
    
    def getPointAdvantage(self):
        return self.pointAdvantage 
        
