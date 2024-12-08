# Checkers AI

Welcome to the Checkers AI project! This repository contains a Python implementation of the game Checkers, and includes an AI player - Maraion, an AI agent working based on Alpha-Beta Pruning Algorythm(Optimization of MiniMax algorythm). The project is leveraging Pygame library for graphical representation and game dynamics.

## Project Structure

- `algorithms.py`: Contains the AI algorithms used for decision making in the game.
- `config.py`: Configuration settings for the game and AI parameters.
- `game.py`: Core game logic and rules for Checkers.
- `main.py`: Entry point for playing the game, initializing game settings and starting the game loop.
- `play.py`: Handles the gameplay, interacting with the user for moves and displaying the game state.
- `utils.py`: Utility functions supporting game operations and AI processes.

## Features

- Play checkers against a computer-controlled opponent.
- Adjustable AI settings to change difficulty levels.
- Graphical user interface using Pygame for interactive gameplay and clear display of the game board.

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/davitsargsyan0/checkers_ai.git
```

Navigate to the cloned directory:

```bash
cd checkers_ai
```

Install Pygame:

```bash
pip install pygame
```

Run the main script to start the game:

```bash
python main.py
```

## How to Play

You can play against the AI by executing the `main.py` script. Moves are made using the mouse to select and move pieces on the graphical board.

## Dependencies

- Python 3
- [Pygame](https://www.pygame.org/news): A Python library for writing video games. It is required to run the graphical interface of this game.

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project. You can also open issues for bugs or feature suggestions.
