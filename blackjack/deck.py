from random import shuffle

from card import Card
from constants.rank import Rank
from constants.suit import Suit

class Deck:

    def __init__(self):
        self.cards = []

        # Generate new deck of 52 cards
        for rank in Rank:
            for suit in Suit:
                self.cards.append(Card(rank, suit))

    def __len__(self):
        ''' Gets the number of cards left in the deck '''
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
