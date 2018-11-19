from random import shuffle

from card import Card
from suit import Suit

class Deck():

    cards = []

    def __init__(self):
        # Generate number cards
        self.cards.extend([ Card(i, Suit.SPADES) for i in range(1, 11) ])
        self.cards.extend([ Card(i, Suit.CLUBS) for i in range(1, 11) ])
        self.cards.extend([ Card(i, Suit.HEARTS) for i in range(1, 11) ])
        self.cards.extend([ Card(i, Suit.DIAMONDS) for i in range(1, 11) ])

        # Generate face cards
        self.cards.extend([ Card(10, Suit.SPADES), Card(10, Suit.SPADES), Card(10, Suit.SPADES) ])
        self.cards.extend([ Card(10, Suit.CLUBS), Card(10, Suit.CLUBS), Card(10, Suit.CLUBS) ])
        self.cards.extend([ Card(10, Suit.HEARTS), Card(10, Suit.HEARTS), Card(10, Suit.HEARTS) ])
        self.cards.extend([ Card(10, Suit.DIAMONDS), Card(10, Suit.DIAMONDS), Card(10, Suit.DIAMONDS) ])

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
