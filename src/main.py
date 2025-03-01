import sys

from Game import Game
import Interface

usernames = sys.argv[1:]

if len(usernames) == 0:
    Interface.error("No names were passed in the arguments")

game = Game(usernames)

game.start()