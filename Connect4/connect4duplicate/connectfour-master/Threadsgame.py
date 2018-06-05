import threading
import connectfour as cf
import connectfour.players as players
import connectfour.games.standard

def worker():
    """thread worker function"""
    p1=players.negamax.NegamaxPlayer(2)
    p2=players.negamax.NegamaxPlayer(4)
    game = connectfour.games.standard.StandardGame(p1=p1, p2=p2, verbose=True)
    game.play()
    return

threads = []
for i in range(30):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
