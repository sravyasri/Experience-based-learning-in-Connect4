import connectfour as cf
import connectfour.players as players
import connectfour.games.standard
import time
start = int(round(time.time() * 1000))
# print millis
# play a single game

#game = connectfour.games.standard.StandardGame(p1=players.human.HumanPlayer(), p2=players.negamaxabp.NegamaxAlphaBetaPruningPlayer(4, verbose=True), verbose=True)

game = connectfour.games.standard.StandardGame(p1=players.negamax.NegamaxPlayer(2, verbose=True), p2=players.negamax.NegamaxPlayer(4, verbose=True), verbose=True)
#game = connectfour.games.standard.StandardGame(p1=players.negamax.NegamaxPlayer(4), p2=players.negamax.NegamaxPlayer(4), verbose=True)
#game = connectfour.games.standard.StandardGame(p1=players.negamaxabp.NegamaxAlphaBetaPruningPlayer(4), p2=players.negamaxabp.NegamaxAlphaBetaPruningPlayer(4), verbose=True)
#game = connectfour.games.standard.StandardGame(p1=players.random.RandomPlayer(), p2=players.negamax.NegamaxPlayer(4), verbose=True)
#game = connectfour.games.standard.StandardGame(p1=players.human.HumanPlayer(), p2=players.negamaxalphabeta.NegamaxAlphaBetaPlayer(4, verbose=True), verbose=True)
game.play()

end = int(round(time.time() * 1000))
print start
print end
print end-start