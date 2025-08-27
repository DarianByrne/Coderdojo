"""
Entrypoint for our TopTrumps game. This script is used to decide which base deck we are going to play with.
"""

from toptrumps.base_decks import *
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def set_game_mode(game_string):
    eval(f"{game_string}_game.main()")


def main():
    base_decks = [f.replace(".py", "").replace("_game", "") for f in os.listdir(f"{CURRENT_DIR}/base_decks") if "_game" in f]
    print("What base deck would you like to play with?")
    index = 0
    for deck in base_decks:
        index += 1
        print(index, deck)
    choice = input("Enter the number")
    print("You have chosen ", base_decks[int(choice) - 1])
    set_game_mode(base_decks[int(choice) - 1])


if __name__ == "__main__":
    main()
