"""
This is the parent classes of our TopTrumps game. This classes can be imported and overridden in child classes to use or rewrite the functionality provided.
"""

from dataclasses import dataclass
from random import shuffle
from typing import List

"""
Card
- Stats
- Name
"""


@dataclass
class TopTrumpCard:
    name: str
    top_trumps_rating: int

    def print_stats(self):
        """
        Function to print the stats available to the specific card type
        """
        pass

    def get(self, current_stat) -> int:
        """
        Function that returns the value of a chosen stat
        :param current_stat:
        :return: int value of selected stat
        """
        pass


""""
Player
- Name
- Type, human or ai
- Hand
- Is it their turn to pick
- What stat do they choose
- Does the player have any cards left
"""


@dataclass
class Player:
    name: str
    type: str
    hand: List[TopTrumpCard]
    has_choice_of_stat: bool = False

    def has_cards_left(self) -> bool:
        """
        Simple boolean, is the player still in the game
        :return: True/False depending on whether or not they have any cards
        """

    def choose_stat(self, card_type: TopTrumpCard) -> str:
        """
        Function for prompting the player to choose a stat
        """


"""
Deck
- Cards
- Shuffle
- Deal
"""


@dataclass
class Deck:
    cards: List[TopTrumpCard]

    def shuffle_deck(self):
        shuffle(self.cards)

    def deal(self, players: List[Player]):
        """
        Function to deal the cards at the start of the game.
        Example logic
        number of players
        number of cards
        number of cards // number of players eg 100 // 4
        number of cards per player 25
        player one gets cards[0:25]
        player two get cards[25:50]
        player three get cards[50:75]
        player four get cards[75:100]
        """

"""
Game
- Invite players to join
- Shuffle and deal
- First turn
- Give cards to the victor
- End when only one player has cards
"""


class TopTrumpsGame:
    def __init__(self, players: List[Player], deck: Deck):
        self.current_stat = None
        self.players = players
        self.deck = deck
        self.deck.shuffle_deck()
        self.players[0].has_choice_of_stat = True

    def deal_cards(self):
        """
        Deal cards to all players
        """

    def prompt_player_to_choose_stat(self):
        """
        Find the player who's turn it is and prompt them for a decision on which stat we want
        """
    def reveal_cards(self):
        """
        Reveal everyones top card
        :return:
        """

    def give_cards_to_the_winner(self, current_round: dict):
        """
        Resolve the round
        :param current_round: dictionary of stat value: and the owner of the card
        """

    def continue_playing(self) -> bool:
        """
        Function to determine if the game has ended
        """
