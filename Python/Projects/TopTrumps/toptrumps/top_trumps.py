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
        stats = vars(self)
        for stat, value in stats.items():
            if stat != "name":
                print(f"{stat}: {value}")

    def get(self, current_stat) -> int:
        """
        Function that returns the value of a chosen stat
        :param current_stat:
        :return: int value of selected stat
        """
        value = getattr(self, current_stat, None)
        if value is None:
            raise ValueError(f"Stat '{current_stat}' does not exist on this card.")
        if not isinstance(value, int):
            raise TypeError(
                f"Stat '{current_stat}' must be an integer, got {type(value).__name__}."
            )
        return value


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
        return len(self.hand) > 0

    def choose_stat(self, card_type: TopTrumpCard) -> str:
        if self.type == "human":
            print(f"{self.name}, choose a stat from the following:")
            card_type.print_stats()
            return input("Enter the stat name: ")
        else:
            # AI chooses the stat with the highest numeric value
            numeric_stats = {
                stat: value
                for stat, value in vars(card_type).items()
                if isinstance(value, int)
            }
            return max(numeric_stats, key=numeric_stats.get)


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
        num_players = len(players)
        for i, card in enumerate(self.cards):
            players[i % num_players].hand.append(card)


class TopTrumpsGame:
    def __init__(self, players: List[Player], deck: Deck):
        self.current_stat = None
        self.players = players
        self.deck = deck
        self.deck.shuffle_deck()
        self.players[0].has_choice_of_stat = True

    def deal_cards(self):
        self.deck.deal(self.players)

    def prompt_player_to_choose_stat(self):
        for player in self.players:
            if player.has_choice_of_stat:
                while True:
                    self.current_stat = player.choose_stat(player.hand[0])
                    if hasattr(player.hand[0], self.current_stat):
                        break
                    print(f"Invalid stat '{self.current_stat}'. Please try again.")

    def reveal_cards(self):
        print("Revealing cards:")
        current_round = {}
        for player in self.players:
            if player.has_cards_left():
                card = player.hand[0]
                stat_value = getattr(card, self.current_stat)
                current_round[stat_value] = player
                print(
                    f"{player.name} reveals {card.name} with {self.current_stat}: {stat_value}"
                )
        return current_round

    def give_cards_to_the_winner(self, current_round: dict):
        winning_stat = max(current_round.keys())
        winners = [
            player
            for stat_value, player in current_round.items()
            if stat_value == winning_stat
        ]

        if len(winners) > 1:
            print("It's a draw! No one wins this round.")
            for player in self.players:
                if player.has_cards_left():
                    player.hand.append(player.hand.pop(0))
            return

        winner = winners[0]
        print(f"{winner.name} wins this round!")
        for stat_value, player in current_round.items():
            winner.hand.append(player.hand.pop(0))
        winner.has_choice_of_stat = True
        for player in self.players:
            if player != winner:
                player.has_choice_of_stat = False

    def continue_playing(self) -> bool:
        active_players = [player for player in self.players if player.has_cards_left()]
        return len(active_players) > 1

    def play_game(self):
        """
        Main game loop to play the game until a winner is determined
        """
        self.deal_cards()
        while self.continue_playing():
            self.prompt_player_to_choose_stat()
            current_round = self.reveal_cards()
            self.give_cards_to_the_winner(current_round)
        winner = [player for player in self.players if player.has_cards_left()][0]
        print(f"{winner.name} is the winner!")
