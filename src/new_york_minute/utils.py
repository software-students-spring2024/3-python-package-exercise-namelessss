# new_york_minute/new_york_minute/utils.py

import json
import os

def save_progress(player):
    player_data = {
        'name': player.name,
        'dream': player.dream,
        'background': player.background,
        'money': player.money,
        'reputation': player.reputation,
        'stress_level': player.stress_level,
        'current_location': player.current_location,
        'inventory': player.inventory
    }
    with open('savegame.json', 'w') as f:
        json.dump(player_data, f)
    print("Game progress saved.")