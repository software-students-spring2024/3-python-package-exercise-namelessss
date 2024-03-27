# new_york_minute/new_york_minute/__init__.py

from .events import handle_event, random_event
from .player import Player
from .utils import save_progress
from .game import start_game, play_turn

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
