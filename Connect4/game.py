import connectfour.games.standard
import connectfour.players as players
import os
import DAO
# import symmetryContemplation
# play a single game
# game = connectfour.games.standard.StandardGame(p1=players.human.HumanPlayer(), p2=players.negamaxabp.NegamaxAlphaBetaPruningPlayer(4, verbose=True), verbose=True)
#game = connectfour.games.standard.StandardGame(p1=players.human.HumanPlayer(), p2=players.negamax.NegamaxPlayer(4, verbose=True), verbose=True)
# game = connectfour.games.standard.StandardGame(p1=players.negamaxabp.NegamaxAlphaBetaPruningPlayer(4), p2=players.negamaxabp.NegamaxAlphaBetaPruningPlayer(4), verbose=True)
# game = connectfour.games.standard.StandardGame(p1=players.random.RandomPlayer(), p2=players.negamax.NegamaxPlayer(4), verbose=True)
# game = connectfour.games.standard.StandardGame(p1=players.human.HumanPlayer(), p2=players.negamaxalphabeta.NegamaxAlphaBetaPlayer(4, verbose=True), verbose=True)
# def gameplay(thread):
#         print "Thread :"  + str(thread)
#         try:
#             game = connectfour.games.standard.StandardGame(p1=players.negamax.NegamaxPlayer(2), p2=players.negamax.NegamaxPlayer(4), verbose=True)
#             game.play()
#     
#         except:
#             print "Exception"
        # game = connectfour.games.standard.StandardGame(p1=players.negamaxabp.NegamaxAlphaBetaPruningPlayer(2), p2=players.negamaxabp.NegamaxAlphaBetaPruningPlayer(4), verbose=True)
#         if game.getWinner() == 2:
#             Player2Win = Player2Win + 1
#         elif game.getWinner() == 1:
#             Player1Win = Player1Win + 1
#         else:
#             Draws = Draws + 1
#         print "Player1 wins" + str(Player1Win)
#         print "Player2 wins" + str(Player2Win)
#         print "Draws" + str(Draws)
import time
Player1Win=0
Player2Win=0
Draws=0
Except=0
ExperienceBaseMoves=0
MovesofPlayer=0
EndResult = open('ENDRESULTFREQUENT', 'a+')
EndResult.write("NEXT SET"+"\n")
numberOfGames=1
pointsAdavantage=0

for i in range(0,numberOfGames):
    try:
        start = int(round(time.time() * 1000))
        game = connectfour.games.standard.StandardGame(p1=players.negamax.NegamaxPlayer(1), p2=players.negamax.NegamaxPlayer(1), verbose=True)
        game.play("Frequent")
        end = int(round(time.time() * 1000))
        print "time"
        print end-start
        ExperienceBaseMoves = ExperienceBaseMoves+ game.getUsageOfExperienceBase()
        MovesofPlayer = MovesofPlayer + game.getNumberOfMovesOfEachPlayer()
    except:
        print "Exception"
        Except=Except+1
    if game.getWinner() == 2:
            Player2Win = Player2Win + 1
            scores = game.getBoard().getRawScores()
            print "scores won by player2"
            print scores[3]
            pointsAdavantage = pointsAdavantage+game.getPointAdvantage()
    elif game.getWinner() == 1:
            Player1Win = Player1Win + 1
            scores = game.getBoard().getRawScores()
            print "scores won by player1"
            print scores[3]
            pointsAdavantage = pointsAdavantage+game.getPointAdvantage()
    else:
            Draws = Draws + 1
EndResult.write("Player1Wins="+str(Player1Win)+"\n")
EndResult.write("Player2Wins="+str(Player2Win)+"\n")
EndResult.write("Exceptions="+str(Except)+"\n")
print "Final Player1 wins" + str(Player1Win)
print "Final Player2 wins" + str(Player2Win)
print "Draws" + str(Draws)
print ExperienceBaseMoves
print MovesofPlayer
totalPlayedGames=numberOfGames-Except
y= float(ExperienceBaseMoves)/float(totalPlayedGames)
x=0
if MovesofPlayer!=0:
    x= float(ExperienceBaseMoves)/float(MovesofPlayer)

print "Percentage of usage of ExperienceBase"+str(x)
EndResult.write("Percentage of Contemplation Usage="+str(x)+"\n")
EndResult.write("Number of times Experience Base Usage="+str(y)+"\n")
size = DAO.getNumberOfNodes()
EndResult.write("Number of nodes in Contemplation DB="+str(size)+"\n")
EndResult.write("Points Advantage="+ str(pointsAdavantage)+"\n")
PAperGame = float(pointsAdavantage)/float(totalPlayedGames)
EndResult.write("Points Advantage per Game="+ str(PAperGame)+"\n")
WinPercentage = float(Player1Win)/float(totalPlayedGames)
LoosePercentage = float(Player2Win)/float(totalPlayedGames)
EndResult.write("WinPercentage="+str(WinPercentage)+"\n")
EndResult.write("LoosePercentage="+str(LoosePercentage)+"\n")
wintolossRatio=float(WinPercentage)/float(LoosePercentage)
EndResult.write("WIN TO LOSS Ratio="+str(wintolossRatio)+"\n")
# EndResult.write("Symmetry Used="+str(symmetryContemplation.symmetryUsed)+"\n")
EndResult.close()
#     thread = Thread(target = gameplay, args = ( i,))
#     thread.start()