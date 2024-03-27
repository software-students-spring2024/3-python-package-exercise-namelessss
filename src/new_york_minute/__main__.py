from new_york_minute.game import solo_game, multiplayer_game, custom_game, load_game

def main():
    print("Welcome to New York Minute!")
    game_type = input("Choose the type of game ('solo', 'multiplayer', 'custom', 'load'): ")
    if game_type == 'solo':
        print("Starting New Game!")
        player_name = input("What's your name? ")
        player_dream = input("What's your dream in New York City? ")
        player_background = input("Choose your background (e.g. Artist/Entrepreneur/Student): ")
        solo_game(player_name, player_dream, player_background)
    elif game_type == 'multiplayer':
        num_players = int(input("Enter the number of players: "))
        player_names = []
        player_dreams = []
        player_backgrounds = []
        for i in range(num_players):
            player_names.append(input(f"Enter the name for Player {i+1}: "))
            player_dreams.append(input(f"Enter the dream for Player {i+1}: "))
            player_backgrounds.append(input(f"Enter the background for Player {i+1}: "))
        multiplayer_game(player_names, player_dreams, player_backgrounds)
    elif game_type == 'custom':
        num_players = int(input("Enter the number of players: "))
        player_names = []
        player_dreams = []
        player_backgrounds = []
        for i in range(num_players):
            player_names.append(input(f"Enter the name for Player {i+1}: "))
            player_dreams.append(input(f"Enter the dream for Player {i+1}: "))
            player_backgrounds.append(input(f"Enter the background for Player {i+1}: "))
        custom_game(num_players, player_names, player_dreams, player_backgrounds)
    elif game_type == 'load':
        save_file = input("Enter the path to the save file: ")
        load_game(save_file)
    else:
        print("Invalid game type. Please try again.")

if __name__ == "__main__":
    main()