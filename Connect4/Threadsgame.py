import connectfour.games.standard
import connectfour.players as players
import os

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
Player1Win=0
Player2Win=0
Draws=0
ExperienceBaseMoves=0
MovesofPlayer=0
EndResult = open('ENDRESULTDummy', 'a+')
EndResult.write("NEXT SET"+"\n")

for i in range(0,1000):
    try:
        game = connectfour.games.standard.StandardGame(p1=players.negamax.NegamaxPlayer(2), p2=players.negamax.NegamaxPlayer(4), verbose=True)
        game.play()
        ExperienceBaseMoves = ExperienceBaseMoves+ game.getUsageOfExperienceBase()
        MovesofPlayer = MovesofPlayer + game.getNumberOfMovesOfEachPlayer()
    except:
        print "Exception"
    if game.getWinner() == 2:
            Player2Win = Player2Win + 1
            scores = game.getBoard().getRawScores()
            print "scores won by player2"
            print scores[3]

    elif game.getWinner() == 1:
            Player1Win = Player1Win + 1
            scores = game.getBoard().getRawScores()
            print "scores won by player1"
            print scores[3]
    else:
            Draws = Draws + 1
EndResult.write("Player1Wins="+str(Player1Win)+"\n")
EndResult.write("Player2Wins="+str(Player2Win)+"\n")
print "Final Player1 wins" + str(Player1Win)
print "Final Player2 wins" + str(Player2Win)
print "Draws" + str(Draws)
print ExperienceBaseMoves
print MovesofPlayer

x=0
if MovesofPlayer!=0:
    x= float(ExperienceBaseMoves)/float(MovesofPlayer)
print "Percentage ofusageof ExperienceBase"+str(x)
EndResult.write("Contemplation Usage="+str(x)+"\n")
size = os.path.getsize('/Users/sgarapati/Documents/PythonWorkspace/Connect4/contemplation.db')
EndResult.write(str(size)+"\n")
# print "MOves" + str(MovesofPlayer)+"\n"
# print "EXPer" + str(ExperienceBaseMoves) + "\n"
EndResult.close()


#     thread = Thread(target = gameplay, args = ( i,))
#     thread.start()
       
        
        
        
