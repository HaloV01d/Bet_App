from cards import Deck # Importing the Deck class from cards module
from dealer import Dealer # Importing the Dealer class from dealer
from player import Player # Importing the Player class from player
from hand import Hand # Importing the Hand class from hand module

def main():
    deck = Deck() # Create a new deck
    deck.shuffle() # Shuffle the deck

    player = Player("Player") # Create a player
    dealer = Dealer("Dealer") # Create a dealer

    # Initial deal
    player.hand.add_card(deck.deal_card()) # Deal two cards to player and dealer
    dealer.hand.add_card(deck.deal_card()) # Deal two cards to player and dealer
    player.hand.add_card(deck.deal_card()) # Deal two cards to player and dealer
    dealer.hand.add_card(deck.deal_card()) # Deal two cards to player and dealer

    print(f"Dealer shows: {dealer.hand.cards[0]}") # Show one of dealer's cards
    print(f"Player hand: {player.hand}") # Show player's hand

    # Player turn
    while player.hit(deck): # Player hits until they stand or bust
        player.hand.add_card(deck.deal_card())
        print(f"Player hand: {player.hand}")
        if player.hand.is_bust():
            print("Player busts! Dealer wins.")
            return

    # Dealer turn
    print(f"Dealer hand: {dealer.hand}") # Reveal dealer's hand
    while dealer.should_hit():
        dealer.hand.add_card(deck.deal_card())
        print(f"Dealer hand: {dealer.hand}")
        if dealer.hand.is_bust():
            print("Dealer busts! Player wins.")
            return

    # Compare hands
    player_score = player.hand.value() # Calculate scores
    dealer_score = dealer.hand.value() # Calculate scores
    print(f"Player score: {player_score}, Dealer score: {dealer_score}")

    if player_score > dealer_score: # Determine winner
        print("Player wins!")
    elif player_score < dealer_score: # Determine winner
        print("Dealer wins!")
    else:
        print("Push (tie)!")

if __name__ == "__main__": # Run the game
    main()