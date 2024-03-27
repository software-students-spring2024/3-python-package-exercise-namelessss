from new_york_minute.game import solo_game

def main():
    print("Welcome to New York Minute! Starting New Game!")
    player_name = input("What's your name? ")
    player_dream = input("What's your dream in New York City? ")
    player_background = input("Choose your background (e.g. Artist/Entrepreneur/Student): ")
    solo_game(player_name, player_dream, player_background)

if __name__ == "__main__":
    main()