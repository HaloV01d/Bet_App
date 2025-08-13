from Game.cards import Deck
from Game.player import Player
from Game.dealer import Dealer

dealer = Dealer()
player = Player("Alondra")
player.bet = 50
deck = Deck()
deck.shuffle()

# player = Player("You")

player.add_card(deck.deal_one())
dealer.add_card(deck.deal_one())

print("Dealer shows:", dealer.show_one_card())
print("Player's hand:", player.show_hand())
print("Current bet:", player.bet)

dealer.play(deck)

print("Dealer's Hand:", dealer.hand_value())