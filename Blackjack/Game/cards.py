from dataclasses import dataclass

@dataclass
class card:
    suit: str
    rank: str
    value: int

class deck:
    def _init_(self):
        self.card = []

        suits = ["hearts", "diamonds", "clubs", "spades"]
        rank = [
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
        for suit in suits:
            for rank, value in ranks:
                self.cards.append(Card(suit, rank, value))