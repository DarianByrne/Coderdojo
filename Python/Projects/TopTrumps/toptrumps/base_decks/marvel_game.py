from dataclasses import dataclass
from toptrumps.top_trumps import TopTrumpCard, Deck, Player, TopTrumpsGame

import os
import yaml

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


@dataclass
class MarvelHero(TopTrumpCard):
    strength: int
    speed: int
    intelligence: int
    skills: int
    reflexes: int
    real_name: str


def build_deck(decks: dict, group: str):
    deck = []
    for cards in decks[group]:
        card = decks[group][cards]
        deck.append(MarvelHero(name=cards,
                               strength=card["strength"],
                               speed=card["speed"],
                               intelligence=card["intelligence"],
                               skills=card["skills"],
                               reflexes=card["reflexes"],
                               top_trumps_rating=card["top_trumps_rating"],
                               real_name=card["real_name"]))
    return Deck(deck)


def main():
    with open(f"{CURRENT_DIR}/../config/marvel.yaml", "r") as marvel_deck:
        config = yaml.unsafe_load(marvel_deck)
    choice = 0
    while choice != 1 and choice != 2:
        choice = int(input("Which deck would you like to play with?: \n 1. Heroes \n 2. Villains"))
    deck_type = "heroes" if choice == 1 else "villains"
    deck = build_deck(config, deck_type)

    player_one = Player(name="Player One", type="human")
    player_two = Player(name="Player Two", type="ai")

    new_game = TopTrumpsGame(players=[player_one, player_two], deck=deck)
    new_game.deal_cards()

    while new_game.continue_playing():
        new_game.prompt_player_to_choose_stat()
        current_round = new_game.reveal_cards()
        new_game.give_cards_to_the_winner(current_round)

    for player in [player_one, player_two]:
        if player.has_cards_left():
            print(f"Congratulations {player.name}, you are the winner.")


if __name__ == "__main__":
    main()
