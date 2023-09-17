from typing import List
from random import shuffle
from player import Player


class Symbol:
    def __init__(self) -> None:
        """
        Symbol's constructor method. Initializes a list with all 4 possible symbols in the deck.
        """
        self.color = ""
        self.icon = ["♥", "♦", "♣", "♠"]

    def __str__(self) -> str:
        """
        Returns a string representation of the Symbol object.
        """
        return f"Symbol({self.color}, {self.icon})"


class Card(Symbol):
    def __init__(self) -> None:
        """
        Card's constructor method. Initializes all the possible values for a card.
        """
        self.possible_values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.value = ""

    def __str__(self) -> str:
        """
        Returns a string representation of the Card object.
        """
        return f"Card({self.possible_values}, {self.value})"


class Deck:
    def __init__(self) -> None:
        """
        Deck's constructor method. Instantiates Symbol and Card objects, as well as
        an empty list "self.cards" that will contain all 52 cards of the decks after
        they will have been generated.
        """
        self.symbol = Symbol()
        self.card = Card()
        self.cards = []

    def fill_deck(self) -> None:
        """
        Generates all 13 possible values for each of the 4 symbols and fills a deck list with
        all of them.
        """
        for value in self.card.possible_values:
            for symbol in self.symbol.icon:
                self.cards.append(f"{value} {symbol}")

    def shuffle(self) -> None:
        """
        Shuffles the deck.
        """
        shuffle(self.cards)

    def distribute(self, players: List[Player]) -> None:
        """
        Distributes cards evenly to all players. In case of an odd number of players,
        cards will be distributed until each player has the same number of cards,
        eliminating any extra cards that cannot be distributed equally.
        Example : if there are 3 players, 51 cards will be distributed so everyone
        has 17 cards. The 52th card in the deck is not taken into account.

        Parameters:
            players (list) : List containing objects representing all players in the game.
        """
        # Calculating how many cards each player will receive
        cards_per_player = len(self.cards) // len(players)
        # As long as all the players don't have the calculated amount of cards in
        # their hands, keep distributing.
        while not all(map(lambda x: x.number_of_cards == cards_per_player, players)):
            for player in players:
                # This operation deletes the last card in the shuffled deck
                # and appends it in the player's hand in a single line.
                player.cards.append(self.cards.pop())
                player.number_of_cards += 1

    def __str__(self) -> str:
        """
        Returns a string representation of the Deck object.
        """
        return f"Deck({self.symbol}, {self.card}, {self.cards})"
