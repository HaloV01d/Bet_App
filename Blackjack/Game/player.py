# from Game.cards import deck

class Player:
    def _init_(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        return [f"{card.rank} of {card.suit}" for card in self.hand]

    def hit (self, deck):
        self.add.card(deck.deal_one())

    def stand(self):
        self.is_active = False

    def double_down(self, deck):
        self.bet *= 2
        self.hit(deck)
        self.is_active = False

    def split(self):

        pass

    def surrender(self):
        self.is_active = False
        self.bet /= 2 

    def insurance(self):

        pass