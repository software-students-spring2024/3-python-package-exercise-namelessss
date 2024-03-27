from new_york_minute import game

# TODO - Follows similar structure to the examples on our README.

# Starts a single player game, with the player name, dream, and background.
solo_game("John", "Become a successful artist", "Artist")
# Starts a single player game, with the player name, dream, background, and a list of actions to automate the game.
solo_game("John", "Become a famous musician", "Artist", actions=['work', 'relax', 'network'])

# Starts a multiplayer game, with the players' names, dreams, and backgrounds.
multiplayer_game(["Alice", "Bob"], ["Open a cafe", "Launch a tech startup"], ["Entrepreneur", "Student"])
# Starts a multiplayer game, with the players' names, dreams, backgrounds, and a list of actions to automate the game.
multiplayer_game(["Alice", "Bob"], ["Open a cafe", "Launch a tech startup"], ["Entrepreneur", "Student"], actions=['work', 'relax', 'network'])

# Starts a custom game with a specified number of players, and a list of the player names, dreams, and backgrounds.
custom_game(3, ["Alice", "Bob", "Charlie"], ["Open a cafe", "Launch a tech startup", "Become a famous musician"], ["Entrepreneur", "Student", "Artist"])
# Starts a custom game with a specified number of players, and a list of the player names, dreams, backgrounds, and actions to automate the game.
custom_game(3, ["Alice", "Bob", "Charlie"], ["Open a cafe", "Launch a tech startup", "Become a famous musician"], ["Entrepreneur", "Student", "Artist"], actions=['work', 'relax', 'network'])

# Loads a previously saved game using the path to the saved file.
load_game("savegame.json")
# Loads a previously saved game using the path to the saved file, and loads this game with a list of actions to automate the game.
load_game("savegame.json", actions=['work', 'relax', 'network'])