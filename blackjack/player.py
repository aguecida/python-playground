from constants.rank import Rank

class Player:

    def __init__(self, name = 'Dealer'):
        self.cards = []
        self.name = name

    def __len__(self):
        return len(self.cards)

    def display_hand(self):
        ''' Prints our the cards in the player's hand '''
        print(f"\n{self.name}'s hand:\n")
        for card in self.cards:
            print(card)

    def hand_total(self):
        ''' Gets the total value of all cards in the player's hand '''
        total = 0

        for card in self.cards:
            # TODO: ACEs needs to be counted last
            if card.rank == 'ACE':
                # Treat ACE as 1 or 11
                if total + 11 > 21:
                    total += 1
                else:
                    total += 11
            else:
                rank_value = Rank[card.rank]
                total += rank_value
                
        return total

    def is_bust(self):
        ''' Checks if the player busted '''
        return self.hand_total() > 21

    def has_blackjack(self):
        ''' Checks if the player has blackjack '''
        return self.hand_total() == 21

    def add_card_to_hand(self, card):
        ''' Adds a card to the player's current hand '''
        self.cards.append(card)

    def reveal_cards(self):
        ''' Turns all player cards face up '''
        for card in self.cards:
            card.faceup = True

    def clean_hand(self):
        ''' Empty the player's hand '''
        self.cards = []
