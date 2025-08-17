import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        color.append(color)
        
    
    return code

def guess_code():
    guess = input("Guess: ").upper()
    pass