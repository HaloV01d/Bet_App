import random
from Game.cards import Deck
from Game.cards import Card

class Dealer:
    def __init__(self):
        self.hand = []
        self.is_active = True

    def add_card(self, card):
        self.hand.append(card)

    def show_one_card(self):
        return f"{self.hand[0].rank} of {self.hand[0].suit}"
    
    
    def hand_value(self):
        value = sum(card.value for card in self.hand)
        ace = sum (1 for card in self.hand if card.rank == "Ace")
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value
    
    def should_hit(self) -> bool:
        value = self.hand_value()
        has_ace = any(card.rank == "Ace" for card in self.hand)

        if value < 17:
            return True
        else:
            return False
        
    def play(self, deck: Deck):
        while self.should_hit():
            self.add_card(deck.deal_one())
        self.is_active = False

    def reset_hand(self):
        self.hand = []
        self.is_active = True

    def dealer_hit_one_16_or_less(hand_value: int) -> bool:

        return hand_value <= 16

    def dealer_counts_an_ace_as_an_11(hand: list) -> bool:
        value = 0
        ace = 0 
        for card in hand:
            if card.rank == "Ace":
                ace += 1
                value += 11
            else:
                value += card.value

        return value <= 21

    def dealer_is_in_charge_of_shuffling_properly(deck: list) -> None:
        random.shuffle(deck)

    # def dealer_stands_on_a_hard_11():

    #     return

    # def dealer_is_last_to_show_second_hand():

    #     return

    def dealer_hits_on_soft_17(hand: list) -> bool:
        value = 0
        has_ace = False

        for card in hand:
            value += card.value
            if card.rank == "Ace":
                has_ace = True

        return value == 17 and has_ace

    # def dealer_cannot_make_bets():

    #     return