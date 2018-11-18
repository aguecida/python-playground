from deck import Deck

deck = Deck()

print(len(deck))

deck.shuffle()

card = deck.deal_card()

print(card.value)
print(card.suit)
