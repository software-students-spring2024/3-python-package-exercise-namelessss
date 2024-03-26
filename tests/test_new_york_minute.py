import pytest
from new_york_minute.player import Player
from new_york_minute.events import handle_event, random_event
from new_york_minute.utils import save_progress, load_progress
from new_york_minute.game import start_game, play_turn

def test_player_creation():
    player = Player("John", "Become a famous musician", "Artist")
    assert player.name == "John"
    assert player.dream == "Become a famous musician"
    assert player.background == "Artist"
    assert player.money == 1000
    assert player.reputation == 0
    assert player.stress_level == 0
    assert player.current_location == "Brooklyn"
    assert player.inventory == []

def test_player_actions():
    player = Player("John", "Become a famous musician", "Artist")
    player.work()
    assert player.money == 1100
    assert player.stress_level == 10
    player.relax()
    assert player.stress_level == 0
    player.network()
    assert player.reputation == 10

def test_handle_event():
    assert handle_event("Brooklyn") == "attend a local art show"
    assert handle_event("Manhattan") == "visit a famous landmark"
    assert handle_event("Unknown Location") == "just explore the city"

def test_random_event():
    player = Player("John", "Become a famous musician", "Artist")
    initial_money = player.money
    random_event(player)
    assert player.money != initial_money

def test_save_and_load_progress():
    player = Player("John", "Become a famous musician", "Artist")
    player.money = 1500
    player.reputation = 20
    save_progress(player)
    loaded_player = load_progress()
    assert loaded_player.name == "John"
    assert loaded_player.money == 1500
    assert loaded_player.reputation == 20