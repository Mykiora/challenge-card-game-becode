from random import shuffle

class Symbol:
    def __init__(self):
        self.color = ''
        self.icon = ['♥', '♦', '♣', '♠']


class Card(Symbol):
    def __init__(self):
        self.possible_values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        self.value = ''


class Deck:
    def __init__(self):
        self.symbol = Symbol()
        self.card = Card()
        self.cards = []

    def fill_deck(self):
        for value in self.card.possible_values:
            for symbol in self.symbol.icon:
                self.cards.append(f'{value} {symbol}')

    def shuffle(self):
        shuffle(self.cards)

    def distribute(self, players):
        while len(self.cards) > len(players):
            for player in players:
                player.cards.append(self.cards.pop())
                player.number_of_cards += 1
