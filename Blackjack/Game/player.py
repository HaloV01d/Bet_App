from cards import Deck   # Importing the Deck class from cards module
from hand import Hand  # Importing the Hand class from hand module

class Player: # Player class to represent a player in the game
    def __init__(self, name):
        self.name = name
        self.hand = Hand()  # Ensure this is a Hand object, not a list
        self.is_active = True
        self.bet = 0
        self.balance = 1000  # Starting balance for the player

    def add_card(self, card): # Add a card to the player's hand
        self.hand.append(card)

    def show_hand(self): # Show the player's hand
        return [f"{card.rank} of {card.suit}" for card in self.hand]

    def hit (self, deck):
        card = deck.deal_one()
        self.hand.add_card(card)
        return not self.hand.is_bust()

    def stand(self): # Player stands, ending their turn
        self.is_active = False

    def double_down(self, deck): # Player doubles their bet and gets one final card
        self.bet *= 2
        self.hit(deck)
        self.is_active = False

    def split(self):

        pass

    def surrender(self): # Player surrenders, losing half their bet and ending their turn
        self.is_active = False
        self.bet /= 2 

    def insurance(self):

        pass