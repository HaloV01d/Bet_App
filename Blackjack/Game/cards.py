from dataclasses import dataclass
import random

@dataclass
class Card: # Card class to represent a playing card
    suit: str
    rank: str
    value: int


@dataclass
class Deck: # Deck class to represent a deck of cards
    def __init__(self):
        self.cards = []

        suits = ["hearts", "diamonds", "clubs", "spades"]
        ranks = [
            ("Ace", 11),
            ("2", 2),
            ("3", 3),
            ("4", 4),
            ("5", 5),
            ("6", 6),
            ("7", 7),
            ("8", 8),
            ("9", 9),
            ("10", 10),
            ("Jack", 10),
            ("Queen", 10),
            ("King", 10)
        ]
        #Initialize object inside the class
        for suit in suits:
            for rank, value in ranks:
                self.cards.append(Card(suit, rank, value))

    #Add a card to the deck
    def add_card(self, card):
        self.cards.append(card)

    #Shuffle the deck
    def shuffle(self):
        random.shuffle(self.cards)

    #Gives you the top card (like drawing a card)
    def deal_one(self):
        return self.cards.pop()
    
    def __str__(self): # String representation of the deck
        return ', '.join([f"{card.rank} of {card.suit}" for card in self.cards])
    
    def __len__(self): # Returns the number of cards left in the deck
        return len(self.cards)
    
    def is_empty(self): # Checks if the deck is empty
        return len(self.cards) == 0
    
    def reset(self): # Resets the deck to a full, shuffled state
        self.__init__()

    def deal_card(self): # Deals a card from the deck
        if not self.is_empty():
            return self.deal_one()
        else:
            raise ValueError("The deck is empty!")