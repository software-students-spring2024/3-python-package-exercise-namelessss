from new_york_minute.events import handle_event, random_event
from new_york_minute.player import Player
from new_york_minute.utils import save_progress

def start_game():
    print("Welcome to New York Minute!")
    load_game = input("Do you want to load previous game? (yes/no): ")
    if load_game.lower() == 'yes':
        player = Player.load_progress()
        if player:
            print(f"Welcome back, {player.name}!")
        else:
            print("No saved game found. Starting a new game.")
            player = create_new_player()
    else:
        player = create_new_player()
    while True:
        if play_turn(player):
            break

def create_new_player():
    player_name = input("What's your name? ")
    player_dream = input("What's your dream in New York City? ")
    player_background = input("Choose your background (Artist/Entrepreneur/Student): ")
    return Player(player_name, player_dream, player_background)

def play_turn(player):
    current_location = player.current_location
    print(f"You are in {current_location}.")
    print(f"You decide to {handle_event(current_location)}.")
    action = input("What would you like to do next? ('work', 'relax', 'network', 'save'): ")
    if action == 'work':
        player.work()
    elif action == 'relax':
        player.relax()
    elif action == 'network':
        player.network()
    elif action == 'save':
        save_progress(player)
    else:
        print("Invalid action. Please try again.")
    random_event(player)
    if player.reputation >= 100:
        print(f"Congratulations, {player.name}! You've made a name for yourself and achieved your dream of {player.dream}!")
        return True
    else:
        locations = ['Brooklyn', 'Manhattan', 'Queens', 'The Bronx', 'Staten Island', 'Central Park', 'Wall Street', 'Harlem']
        current_index = locations.index(current_location)
        if current_index < len(locations) - 1:
            player.current_location = locations[current_index + 1]
        else:
            print("The week has ended, and it's time to rest. Let's see what next week brings!")
            player.current_location = locations[0]
        return False

start_game()