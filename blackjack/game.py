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

def get_player_command():
    while True:
        command = input('\nHit or Stay?: ')
        if command.lower() in ['h','hit']:
            return 'hit'
        elif command.lower() in ['s','stay']:
            return 'stay'
        else:
            print('\nSorry, I did not recognize that command. Please try again.')

if __name__ == '__main__':
    # Setup the game
    player, dealer = create_players()
    deck = new_deck()
    deal_cards(deck, player, dealer)
    display_hands(player, dealer)

    # Player's turn
    while True:
        player_command = get_player_command()
        if player_command == 'hit':
            card = deck.deal_card()
            player.add_card_to_hand(card)
            if player.is_bust() or player.has_blackjack():
                break
            else:
                display_hands(player, dealer)
        else: # Stay
            break

    if player.is_bust():
        print('\nYou went over 21. Dealer wins.')
        quit()

    if player.has_blackjack():
        print('\nYou got 21! You win!')
        quit()

    # Dealer's turn
    while True:
        if dealer.total() < 17 :
            card = deck.deal_card()
            dealer.add_card_to_hand(card)
        else:
            break

    dealer.reveal_cards()
    display_hands(player, dealer)

    if dealer.total() >= player.total() and not dealer.is_bust():
        print('\nGame over. Dealer wins.')
    else:
        print('\nGame over. You won!')
