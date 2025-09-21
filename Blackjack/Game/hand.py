class Hand: # Hand class to represent a hand of cards
    def __init__(self): # Initialize with an empty list of cards
        self.cards = []

    def add_card(self, card): # Add a card to the hand
        self.cards.append(card)

    def value(self): # Calculate the value of the hand
        val = 0
        aces = 0
        for card in self.cards:
            if card.rank in ['Jack', 'Queen', 'King']:
                val += 10
            elif card.rank == 'Ace':
                val += 11
                aces += 1
            else:
                val += int(card.rank)
        # Adjust for aces
        while val > 21 and aces:
            val -= 10
            aces -= 1
        return val

    def is_bust(self): # Check if the hand is bust (over 21)
        return self.value() > 21

    def __str__(self): # String representation of the hand
        return ', '.join([f"{card.rank} of {card.suit}" for card in self.cards]) #