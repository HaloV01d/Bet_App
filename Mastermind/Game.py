import random

COLORS = ["R", "G", "B", "Y", "W", "M"]
TRIES = 10
CODE_LENGTH = 4

try:
    from colorama import Fore, Style, init as colorama_init
    colorama_init(autoreset=True)
    COLOR_MAP = {
        "R": Fore.RED + "R" + Style.RESET_ALL,
        "G": Fore.GREEN + "G" + Style.RESET_ALL,
        "B": Fore.BLUE + "B" + Style.RESET_ALL,
        "Y": Fore.YELLOW + "Y" + Style.RESET_ALL,
        "W": Fore.WHITE + "W" + Style.RESET_ALL,
        "M": Fore.MAGENTA + "M" + Style.RESET_ALL,
    }

except Exception:
    COLOR_MAP = {
        "R": "\033[91mR\033[0m",
        "G": "\033[92mG\033[0m",
        "B": "\033[94mB\033[0m",
        "Y": "\033[93mY\033[0m",
        "W": "\033[97mW\033[0m",
        "M": "\033[35mO\033[0m",
    }

def display_colors(seq):
    return " ".join(COLOR_MAP.get(c, c) for c in seq)


def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
        
    
    return code

def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")
    
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue
    
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            break

    return guess

def check_code(guess, real_code):
    color_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1

    for guess_color, real_code in zip(guess, real_code):
        if guess_color == real_code:
            correct_pos += 1
            color_count[guess_color] -= 1
        
    for guess_color, real_code in zip(guess, real_code):
        if guess_color in color_count and color_count[guess_color] > 0:
            incorrect_pos += 1
            color_count[guess_color] -= 1
    
    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to mastermind, you have {TRIES} tries to guess the code...")
    print("The valid colors are",display_colors(COLORS))

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        

        if correct_pos == CODE_LENGTH:
            print(f"You guess the code in {attempts} tries!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Position: {incorrect_pos}")

    else:
        print("You ran out of tries, code was: ", display_colors(code))

if __name__ == "__main__":
    game()