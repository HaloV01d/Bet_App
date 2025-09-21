import random # Import random module for generating random choices

user_wins = 0 # Initialize user wins counter
computer_wins = 0 # Initialize computer wins counter

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower() # Get user input and convert to lowercase
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]: # Validate user input
        print("Invalid input. Please try again.")
        continue

    random_number = random.randint(0, 2) # Generate random number for computer's choice
    if random_number == 0:
        computer_pick = "rock"
    elif random_number == 1:
        computer_pick = "paper"
    else:
        computer_pick = "scissors"

    print("Computer picked", computer_pick + ".") # Display computer's choice

    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a tie!")
    else:
        print("You lose!")
        computer_wins += 1

print("You won", user_wins, "times.") # Display total user wins
print("The computer won", computer_wins, "times.") # Display total computer wins
print("Goodbye!")