from colorama import init, Fore, Back, Style

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

def game_reset(player, dealer):
    # Setup new deck
    deck = Deck()
    deck.shuffle()

    # Setup new player hands
    player.clean_hand()
    dealer.clean_hand()
    deal_cards(deck, player, dealer)
    display_hands(player, dealer)

    return deck

def end_game():
    while True:
        restart = input('Play again (y/n)?: ')
        if restart == 'y' or restart == 'n':
            return restart == 'n'
        else:
            continue

if __name__ == '__main__':
    # Initialize colorama
    init()

    game_over = False
    player, dealer = create_players()

    while not game_over:
        deck = game_reset(player, dealer)
        
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
            dealer.reveal_cards()
            display_hands(player, dealer)
            print(Fore.RED + '\nYou busted. Dealer wins.')
            print(Style.RESET_ALL)
            game_over = end_game()
            continue

        if player.has_blackjack():
            dealer.reveal_cards()
            display_hands(player, dealer)
            print(Fore.GREEN + '\nYou got Blackjack! You win!')
            print(Style.RESET_ALL)
            game_over = end_game()
            continue

        # Dealer's turn
        while True:
            if dealer.hand_total() < 17:
                card = deck.deal_card()
                dealer.add_card_to_hand(card)
            else:
                break

        dealer.reveal_cards()
        display_hands(player, dealer)

        if dealer.hand_total() >= player.hand_total() and not dealer.is_bust():
            print(Fore.RED + '\nGame over. Dealer wins.')
        else:
            print(Fore.GREEN + '\nGame over. You win!')

        print(Style.RESET_ALL)
        game_over = end_game()
