from new_york_minute.game import solo_game, multiplayer_game, custom_game, load_game

# Example 1: Solo game
print("Example 1: Solo game")
solo_game("John", "Become a successful artist", "Artist")

# Example 2: Solo game with automated actions
print("\nExample 2: Solo game with automated actions")
solo_game("Alice", "Become a famous musician", "Artist", actions=['work', 'relax', 'network'])

# Example 3: Multiplayer game
print("\nExample 3: Multiplayer game")
multiplayer_game(["Alice", "Bob"], ["Open a cafe", "Launch a tech startup"], ["Entrepreneur", "Student"])

# Example 4: Multiplayer game with automated actions
print("\nExample 4: Multiplayer game with automated actions")
multiplayer_game(["Alice", "Bob"], ["Open a cafe", "Launch a tech startup"], ["Entrepreneur", "Student"], actions=['work', 'relax', 'network'])

# Example 5: Custom game
print("\nExample 5: Custom game")
custom_game(3, ["Alice", "Bob", "Charlie"], ["Open a cafe", "Launch a tech startup", "Become a famous musician"], ["Entrepreneur", "Student", "Artist"])

# Example 6: Custom game with automated actions
print("\nExample 6: Custom game with automated actions")
custom_game(3, ["Alice", "Bob", "Charlie"], ["Open a cafe", "Launch a tech startup", "Become a famous musician"], ["Entrepreneur", "Student", "Artist"], actions=['work', 'relax', 'network'])

# Example 7: Load game from a save file
print("\nExample 7: Load game from a save file")
load_game("savegame.json")

# Example 8: Load game from a save file with automated actions
print("\nExample 8: Load game from a save file with automated actions")
load_game("savegame.json", actions=['work', 'relax', 'network'])