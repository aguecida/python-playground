class Card:

    def __init__(self, rank, suit, faceup = True):
        self.rank = rank
        self.suit = suit
        self.faceup = faceup

    def __str__(self):
        if self.faceup:
            return f'{self.rank} of {self.suit.name}'
        else:
            return 'Face down card'
