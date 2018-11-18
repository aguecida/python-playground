class Player():

    def __init__(self, name = 'Dealer'):
        self.cards = []
        self.name = name

    def display_hand(self):
        print(f"\n{self.name}'s hand:\n")
        for card in self.cards:
            if card.faceup:
                print(f"{card.value} of {card.suit}")
            else:
                print("One face down card")

    def total(self):
        total = 0
        for card in self.cards:
            total += card.value
        return total

    def is_bust(self):
        return self.total() > 21

    def has_blackjack(self):
        return self.total() == 21

    def add_card_to_hand(self, card):
        self.cards.append(card)
