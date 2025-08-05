from Game.cards import Deck
from Game.player import Player
from Game.dealer import Dealer

dealer = Dealer()
deck = Deck()
deck.shuffle()

# player = Player("You")

dealer.add_card(deck.deal_one())
dealer.add_card(deck.deal_one())

print("Dealer shows:", dealer.show_one_card())

dealer.play(deck)

print("Dealer's Hand:", dealer.hand_value())