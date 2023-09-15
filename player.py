from random import randint

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []
    
    def play(self):
        if len(self.cards) == 0:
            return
        picked_card = self.cards.pop(randint(0, len(self.cards) - 1))
        self.history.append(picked_card)
        print(f'\nPlayer {self.player_id}, during turn {self.turn_count}, played: {picked_card}')
        return picked_card


