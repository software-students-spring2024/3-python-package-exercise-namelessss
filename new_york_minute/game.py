# new_york_minute/new_york_minute/game.py

from .player import Player
from .events import handle_event, random_event

def start_game():
    print("Welcome to New York Minute!")
    player_name = input("What's your name? ")
    player_dream = input("What's your dream in New York City? ")
    player_background = input("Choose your background (Artist/Entrepreneur/Student): ")
    player = Player(player_name, player_dream, player_background)
    return player

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
        player.save_progress()
    else:
        print("Invalid action. Please try again.")
    random_event(player)
    if player.reputation >= 100:
        print(f"Congratulations, {player.name}! You've made a name for yourself and achieved your dream of {player.dream}!")
        return True 
    else:
        locations = ['Brooklyn', 'Manhattan', 'Queens', 'The Bronx', 'Staten Island', 'Central Park', 'Wall Street', 'Harlem']
        current_index = locations.index(player.current_location)
        if current_index < len(locations) - 1:
            player.current_location = locations[current_index + 1]
        else:
            print("The week has ended, and it's time to rest. Let's see what next week brings!")
            player.current_location = locations[0]  
        return False