from deck import Deck
from player import Player

def create_players():
    player_name = input('Enter your name: ')
    player = Player(player_name)
    dealer = Player()
    return player, dealer

def new_deck():
    deck = Deck()
    deck.shuffle()
    return deck

def deal_cards(deck, player, dealer):
    print('\nDealing cards...')

    card = deck.deal_card()
    player.add_card_to_hand(card)

    card = deck.deal_card(faceup=False) # Deal one dealer card face down
    dealer.add_card_to_hand(card)

    card = deck.deal_card()
    player.add_card_to_hand(card)

    card = deck.deal_card()
    dealer.add_card_to_hand(card)

def display_hands(player, dealer):
    player.display_hand()
    dealer.display_hand()

if __name__ == '__main__':
    player, dealer = create_players()
    deck = new_deck()
    deal_cards(deck, player, dealer)
    display_hands(player, dealer)
