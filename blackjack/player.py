class Player():
    cards = []

    def __init__(self, name = 'Dealer'):
        self.name = name

    def total(self):
        total = 0
        for card in self.cards:
            total += card.value
        return total

    def is_bust(self):
        return self.total() > 21

    def has_blackjack(self):
        return self.total() == 21
