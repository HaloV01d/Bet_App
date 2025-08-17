from dataclasses import dataclass
import random

@dataclass
class Card:
    suit: str
    rank: str
    value: int


@dataclass
class Deck:
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

    #Shuffle the deck
    def shuffle(self):
        random.shuffle(self.cards)

    #Gives you the top card (like drawing a card)
    def deal_one(self):
        return self.cards.pop()