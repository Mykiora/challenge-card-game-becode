from random import randint


class Player:
    def __init__(self, player_id: int) -> None:
        """
        Player's constructor method. Initializes an empty list that will contain the cards
        in a player's hand as well as counters for turns and numbers of cards. Finally, creates
        an empty list for the future played cards' history.

        Parameters:
            player_id (int): A number starting from 1 generated with range() in a for loop
            in the start_game() method located in game.py to help identify a player.
        """
        self.player_id = player_id
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

    def play(self) -> str:
        """
        Manages a turn for a given player if he has cards in his hands.

        1. A card is selected randomly from the player's hand.
        2. This card is added in the history and deleted from the player's hand.
        3. Print player id, current turn and the card played.

        Return : A string representing the value and symbol of the card. Example : '10 ♠'
        """
        # Immediately get out of the function if the given player has no cards.
        if len(self.cards) == 0:
            return
        # Takes a random card from the player's hand and adds it to its history.
        picked_card = self.cards.pop(randint(0, len(self.cards) - 1))
        self.history.append(picked_card)
        print(
            f"\nPlayer {self.player_id}, during turn {self.turn_count}, played: {picked_card}"
        )
        return picked_card

    def __str__(self) -> str:
        """
        Returns a string representation of the Player object.
        """
        return f"Player({self.player_id}, {self.cards}, {self.turn_count}, {self.number_of_cards}, {self.history})"
