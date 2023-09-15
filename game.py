from utils.card import Deck
from player import Player

class Board:
    def __init__(self):
        self.players = []
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []
        print("--- Board Initialized. ---")

    def start_game(self, number_of_players):
        self.number_of_players = number_of_players
        for i in range(number_of_players):
            self.players.append(Player(i+1))
        
        deck = Deck()
        deck.fill_deck()
        deck.distribute(self.players)
        
        while all([player.cards for player in self.players]):
            for player in self.players:
                if len(self.active_cards) == len(self.players):
                    self.active_cards = []
                played_card = player.play()
                self.active_cards.append(played_card)
                self.history_cards.append(played_card)
                print(f'Turn {self.turn_count}')
                print(f'Active cards : {self.active_cards}')
                print(f'Number of cards in history : {len(self.history_cards)}')
                player.turn_count += 1
            self.turn_count += 1
            



