from utils.card import Deck
from player import Player


class Board:
    def __init__(self) -> None:
        """
        Board's constructor method. Initializes an empty list that will contain objects
        representing the players, a turn counter, and two more empty lists that will
        contain played cards' history for the current turn AND the number of cards played
        in the whole game.
        """
        self.players = []
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []
        print("--- Board Initialized. ---")

    def start_game(self, NUMBER_OF_PLAYERS: int) -> None:
        """
        Manages the game start and the main game loop.
        1. Instantiates all players' objects and stores them in a list.
        2. Instantiates all 52 cards objects and stores them in a deck list.
        3. Distributes the cards evenly to all players.
        4. Resets the active_cards variable every new turn.
        5. Updates played cards' history.
        6. Print current turn, active cards (played this turn), number of cards in history.
        7. Updates the turns' counters.

        Parameters:
            NUMBER_OF_PLAYERS (int): The number of players that will play the game. The program will
            use this value to instantiate a number of players' objects equal to the number
            of players that will play. This value can modified in the main.py.
        """
        # Creating players objects
        for i in range(NUMBER_OF_PLAYERS):
            self.players.append(Player(i + 1))

        deck = Deck()
        deck.fill_deck()
        deck.distribute(self.players)

        # While players still possess cards in their hands, keep the game going.
        while all([player.cards for player in self.players]):
            for player in self.players:
                # Refresh the active cards at the beginning of every turn.
                # The len of the active cards will be equal to the number of players
                # when everyone has played.
                if len(self.active_cards) == len(self.players):
                    self.active_cards = []
                played_card = player.play()
                # Updates history
                self.active_cards.append(played_card)
                self.history_cards.append(played_card)
                print(f"Turn {self.turn_count}")
                print(f"Active cards : {self.active_cards}")
                print(f"Number of cards in history : {len(self.history_cards)}")
                player.turn_count += 1
            self.turn_count += 1

    def __str__(self) -> str:
        """
        Returns a string representation of the Board object.
        """
        return f"Board({self.players}, {self.turn_count}, {self.active_cards}, {self.history_cards})"
