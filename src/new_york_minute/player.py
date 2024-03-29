# new_york_minute/new_york_minute/player.py

import json
import os

class Player:
    def __init__(self, name, dream, background):
        self.name = name
        self.dream = dream
        self.background = background
        self.money = 1000
        self.reputation = 0
        self.stress_level = 0
        self.current_location = 'Brooklyn'
        self.inventory = []

    def work(self):
        self.money += 100
        self.stress_level += 10
        print(f"You worked hard and earned some money. Current balance: ${self.money}")

    def relax(self):
        self.stress_level -= 10
        print("You took some time off to relax and reduce stress.")

    def network(self):
        self.reputation += 10
        print("You attended a networking event and improved your reputation.")

    @classmethod
    def load_progress(cls, save_file):
        if os.path.exists(save_file):
            with open(save_file, 'r') as f:
                player_data = json.load(f)
            player = cls(
                player_data['name'],
                player_data['dream'],
                player_data['background']
            )
            player.money = player_data['money']
            player.reputation = player_data['reputation']
            player.stress_level = player_data['stress_level']
            player.current_location = player_data['current_location']
            player.inventory = player_data['inventory']
            return player
        else:
            return None