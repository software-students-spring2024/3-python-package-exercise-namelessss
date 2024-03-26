# new_york_minute/new_york_minute/utils.py

import json
import os

def save_progress(player_data):
    with open('savegame.json', 'w') as f:
        json.dump(player_data, f)
    print("Game progress saved.")

def load_progress():
    if os.path.exists('savegame.json'):
        with open('savegame.json', 'r') as f:
            player_data = json.load(f)
        return player_data
    else:
        return None