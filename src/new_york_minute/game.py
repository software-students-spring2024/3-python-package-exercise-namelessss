from new_york_minute.events import handle_event, random_event
from new_york_minute.player import Player
from new_york_minute.utils import save_progress


def solo_game(player_name, player_dream, player_background, actions=None):
    player = Player(player_name, player_dream, player_background)
    start_game(player, actions)

def multiplayer_game(player_names, player_dreams, player_backgrounds, actions=None):
    players = [Player(name, dream, background) for name, dream, background in zip(player_names, player_dreams, player_backgrounds)]
    start_game(players, actions)

def custom_game(num_players, player_names, player_dreams, player_backgrounds, actions=None):
    players = [Player(name, dream, background) for name, dream, background in zip(player_names, player_dreams, player_backgrounds)]
    start_game(players[:num_players], actions)

def load_game(save_file, actions=None):
    player = Player.load_progress(save_file)
    if player:
        start_game(player, actions)
    else:
        print("No saved game found.")

def start_game(players, actions=None):
    if isinstance(players, list):
        for player in players:
            print(f"Welcome, {player.name}!")
    else:
        print(f"Welcome, {players.name}!")

    completed_players = []
    while len(completed_players) < len(players):
        for player in players:
            if player not in completed_players:
                if play_turn(player, actions):
                    completed_players.append(player)
                    print(f"{player.name} has achieved their dream!")
                else:
                    print(f"{player.name}'s turn is over.")
        print("All players have completed their turns.")

    print("The game has ended. Thank you for playing!")

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
    if player.reputation >= 50:
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