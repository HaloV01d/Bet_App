# 🎲 Bet_App

A Python-based collection of classic games featuring Blackjack, Rock-Paper-Scissors, and Mastermind. Built as a personal project to explore game logic, object-oriented programming, and interactive CLI applications.

## 🎮 Games Included

### 🃏 Blackjack
A fully-featured casino card game implementation with:
- Object-oriented design with separate `Player`, `Dealer`, `Deck`, `Hand`, and `Card` classes
- Modular architecture for easy maintenance and expansion
- Betting system integration
- Proper game flow and dealer AI

**Location:** `Blackjack/`

### ✊✋✌️ Rock-Paper-Scissors
Classic hand game with:
- Player vs. Computer gameplay
- Win/loss tracking across multiple rounds
- Interactive command-line interface
- Game statistics display

**Location:** `Rock_Paper_Scissors/`

### 🧠 Mastermind
Code-breaking logic puzzle game featuring:
- 4-color code guessing with 10 attempts
- Color-coded terminal output using `colorama`
- Position feedback system (correct position vs. correct color)
- Support for 6 different colors (R, G, B, Y, W, M)

**Location:** `Mastermind/`

## 💻 Tech Stack

- **Language:** Python 3.x
- **Libraries:** 
  - `random` - Game randomization
  - `colorama` - Enhanced terminal colors (Mastermind)
- **Design Patterns:** Object-oriented programming, modular architecture

## 📁 Project Structure

```
Bet_App/
├── Blackjack/
│   ├── main.py              # Game entry point
│   ├── requirements.txt     # Python dependencies
│   └── Game/                # Game logic modules
│       ├── blackjack.py
│       ├── cards.py
│       ├── dealer.py
│       ├── deck.py
│       ├── hand.py
│       └── player.py
├── Mastermind/
│   └── Game.py              # Complete Mastermind implementation
└── Rock_Paper_Scissors/
    └── rock_paper_scissors.py
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Installation

1. Clone the repository:
```bash
git clone https://github.com/HaloV01d/Bet_App.git
cd Bet_App
```

2. Install dependencies (for Blackjack):
```bash
cd Blackjack
pip install -r requirements.txt
```

### Running the Games

**Blackjack:**
```bash
cd Blackjack
python main.py
```

**Rock-Paper-Scissors:**
```bash
cd Rock_Paper_Scissors
python rock_paper_scissors.py
```

**Mastermind:**
```bash
cd Mastermind
python Game.py
```

## 🎯 Features

- **Clean CLI Interface:** Intuitive text-based gameplay
- **Modular Design:** Easy to extend and maintain
- **Game Statistics:** Track wins, losses, and performance
- **Reusable Components:** Object-oriented architecture for code reuse

## 🔮 Future Enhancements

- [ ] Complete Blackjack betting system and game loop
- [ ] Add GUI using `tkinter` or `pygame`
- [ ] Persistent user profiles and statistics
- [ ] Additional games (Poker, Slots, Roulette)
- [ ] Multiplayer support
- [ ] Achievement system
- [ ] Save/load game state

## 📝 License

This is a personal project for educational purposes.

## 👤 Author

**Alondra Soto**
- GitHub: [@HaloV01d](https://github.com/HaloV01d)

---

*Built with ❤️ and Python*