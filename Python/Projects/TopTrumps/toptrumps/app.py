"""
Entrypoint for our TopTrumps game. This script is used to decide which base deck we are going to play with.
"""

from toptrumps.base_decks import *
from toptrumps.top_trumps import Player  # Explicitly import Player
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_players():
    choice = input(
        "Do you want to play a quick game against one AI? (yes/no): "
    ).lower()
    if choice == "yes" or choice == "y":
        return [
            Player(name="Player One", type="human", hand=[]),
            Player(name="Player Two", type="ai", hand=[]),
        ]

    choice = input(
        "Do you want to watch a quick game against three AIs? (yes/no): "
    ).lower()
    if choice == "yes" or choice == "y":
        return [
            Player(name="AI One", type="ai", hand=[]),
            Player(name="AI Two", type="ai", hand=[]),
            Player(name="AI Two", type="ai", hand=[]),
        ]

    while True:
        num_players = input("Enter the number of players: ")
        if num_players.isdigit() and int(num_players) in range(2, 4):
            num_players = int(num_players)
            break
        print("Invalid input. Please enter a number between 2 and 4.")

    players = []
    for i in range(num_players):
        name = input(f"Enter the name for Player {i + 1}: ")
        player_type = input(f"Is Player {i + 1} a 'human' or 'ai'? ").lower()
        while player_type not in ["human", "ai"]:
            print("Invalid number. Please enter 'human' or 'ai'.")
            player_type = input(f"Is Player {i + 1} a 'human' or 'ai'? ").lower()
        players.append(Player(name=name, type=player_type, hand=[]))
    return players


def set_game_mode(game_string):
    players = get_players()
    eval(f"{game_string}_game.main(players=players)")  # Pass players to the game


def main():
    base_decks = [
        f.replace(".py", "").replace("_game", "")
        for f in os.listdir(f"{CURRENT_DIR}/base_decks")
        if "_game" in f
    ]
    print("What base deck would you like to play with?")
    index = 0
    for deck in base_decks:
        index += 1
        print(index, deck)
    while True:
        choice = input("Enter the number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(base_decks):
            break
        print(f"Invalid option. Please enter between 1 and {len(base_decks)}.")
    print("You have chosen ", base_decks[int(choice) - 1])
    set_game_mode(base_decks[int(choice) - 1])


if __name__ == "__main__":
    main()
