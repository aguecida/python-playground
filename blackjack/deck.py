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
        ''' Gets the number of cards in the deck '''
        return len(self.cards)

    def shuffle(self):
        ''' Shuffles the deck of cards '''
        print('\nShuffling deck...')
        shuffle(self.cards)

    def deal_card(self, faceup = True):
        ''' Gets the next card off the top of the deck '''
        card = self.cards.pop()
        card.faceup = faceup
        return card
