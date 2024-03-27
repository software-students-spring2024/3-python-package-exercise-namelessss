# New York Minute

New York Minute is a text-based game set in New York City. As a player, you choose your background and dream, and navigate through different locations in the city while making decisions to work, relax, network, and save your progress. The goal is to achieve your dream by gaining reputation points.

## Installation

You can install New York Minute using pip:

```
pip install new-york-minute
```

## Usage

New York Minute provides four different functions to start and play the game:

1. `solo_game(player_name, player_dream, player_background)`: Start a single-player game with the provided player details.
2. `multiplayer_game(player_names, player_dreams, player_backgrounds)`: Start a multiplayer game with the provided player details for each player.
3. `custom_game(num_players, player_names, player_dreams, player_backgrounds)`: Start a custom game with the specified number of players and their details.
4. `load_game(save_file)`: Load a previously saved game from the specified save file.

To use these functions, first import them from the `new_york_minute` package:

```python
from new_york_minute import solo_game, multiplayer_game, custom_game, load_game
```

### Starting a Solo Game
To start a solo game, call the `solo_game` function with the player's name, dream, and background:

```python
solo_game("John", "Become a successful artist", "Artist")
```

### Starting a Multiplayer Game
To start a multiplayer game, call the `multiplayer_game` function with lists of player names, dreams, and backgrounds:

```python
multiplayer_game(["Alice", "Bob"], ["Open a cafe", "Launch a tech startup"], ["Entrepreneur", "Student"])
```

### Starting a Custom Game
To start a custom game with a specific number of players, call the `custom_game` function with the desired number of players and lists of player names, dreams, and backgrounds:

```python
custom_game(3, ["Alice", "Bob", "Charlie"], ["Open a cafe", "Launch a tech startup", "Become a famous musician"], ["Entrepreneur", "Student", "Artist"])
```

### Loading a Saved Game
To load a previously saved game, call the `load_game` function with the path to the save file:

```python
load_game("savegame.json")
```

### Playing the Game
During each turn, you will be presented with the current location and a random event. You can choose to work, relax, network, or save your progress. The game ends when you achieve your dream by gaining enough reputation points or when you complete all the locations.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/software-students-spring2024/3-python-package-exercise-namelessss).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.