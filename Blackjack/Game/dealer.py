import random # Importing the random module for shuffling
from cards import Deck # Importing the Deck class from cards module
from hand import Hand # Importing the Hand class from hand module

class Dealer: # Dealer class to represent the dealer in the game
    def __init__(self, name):
        self.name = name
        self.hand = Hand()  # Ensure this is a Hand object, not a list
        self.is_active = True
        self.bet = 0

    def add_card(self, card): # Add a card to the dealer's hand
        self.hand.add_card(card)

    def show_one_card(self): # Show only one card of the dealer
        return f"{self.hand.cards[0].rank} of {self.hand.cards[0].suit}"
    
    
    def hand_value(self): # Calculate the value of the dealer's hand
        value = sum(card.value for card in self.hand.cards)
        ace = sum (1 for card in self.hand.cards if card.rank == "Ace")
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value
    
    def should_hit(self) -> bool: # Determine if the dealer should hit based on hand value
        value = self.hand_value()
        if value < 17:
            return True
        else:
            return False    
        
    def play(self, deck: Deck): #  Dealer plays their turn
        while self.should_hit():
            self.add_card(deck.deal_one())
        self.is_active = False

    def reset_hand(self): # Reset the dealer's hand for a new round
        self.hand = Hand()
        self.is_active = True

    def dealer_hit_one_16_or_less(hand_value: int) -> bool: # Dealer hits on 16 or less

        return hand_value <= 16

    def dealer_counts_an_ace_as_an_11(hand: list) -> bool: # Dealer counts an Ace as 11 if it doesn't bust the hand
        value = 0
        ace = 0 
        for card in hand:
            if card.rank == "Ace":
                ace += 1
                value += 11
            else:
                value += card.value

        return value <= 21

    def dealer_is_in_charge_of_shuffling_properly(deck: list) -> None: # Dealer is responsible for shuffling the deck properly
        random.shuffle(deck)

    # def dealer_stands_on_a_hard_11():

    #     return

    # def dealer_is_last_to_show_second_hand():

    #     return

    def dealer_hits_on_soft_17(hand: list) -> bool: # Dealer hits on soft 17 (a hand with an Ace counted as 11)
        value = 0
        has_ace = False

        for card in hand:
            value += card.value
            if card.rank == "Ace":
                has_ace = True

        return value == 17 and has_ace

    # def dealer_cannot_make_bets():

    #     return