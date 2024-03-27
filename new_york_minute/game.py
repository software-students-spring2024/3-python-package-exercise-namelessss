# new_york_minute/new_york_minute/game.py

from .player import Player
from .events import handle_event, random_event
from .utils import save_progress

def start_game(players, input_func=input):
    if isinstance(players, list):
        for player in players:
            print(f"Welcome, {player.name}!")
    else:
        print(f"Welcome, {players.name}!")
    while True:
        if isinstance(players, list):
            for player in players:
                if play_turn(player, input_func):
                    break
        else:
            if play_turn(players, input_func):
                break

def play_turn(player, actions=None):
    current_location = player.current_location
    print(f"You are in {current_location}.")
    print(f"You decide to {handle_event(current_location)}.")
    if actions:
        action = actions.pop(0)
        print(f"Action: {action}")
    else:
        action = input("What would you like to do next? ('work', 'relax', 'network', 'save'): ")
    if action == 'work':
        player.work()
    elif action == 'relax':
        player.relax()
    elif action == 'network':
        player.network()
    elif action == 'save':
        save_progress(player, 'savegame.json')
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