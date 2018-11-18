from random import shuffle

from card import Card
from suit import Suit

class Deck():
    cards = []

    def __init__(self):
        # Generate number cards
        self.cards.extend([ Card(i, Suit.SPADE) for i in range(1, 11) ])
        self.cards.extend([ Card(i, Suit.CLUB) for i in range(1, 11) ])
        self.cards.extend([ Card(i, Suit.HEART) for i in range(1, 11) ])
        self.cards.extend([ Card(i, Suit.DIAMOND) for i in range(1, 11) ])

        # Generate face cards
        self.cards.extend([ Card(10, Suit.SPADE), Card(10, Suit.SPADE), Card(10, Suit.SPADE) ])
        self.cards.extend([ Card(10, Suit.CLUB), Card(10, Suit.CLUB), Card(10, Suit.CLUB) ])
        self.cards.extend([ Card(10, Suit.HEART), Card(10, Suit.HEART), Card(10, Suit.HEART) ])
        self.cards.extend([ Card(10, Suit.DIAMOND), Card(10, Suit.DIAMOND), Card(10, Suit.DIAMOND) ])

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        shuffle(self.cards)
