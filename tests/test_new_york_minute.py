import pytest

from new_york_minute.events import handle_event, random_event
from new_york_minute.player import Player
from new_york_minute.utils import save_progress
from new_york_minute.game import solo_game, multiplayer_game, custom_game, load_game, start_game, play_turn

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
    assert player.money == initial_money or player.money == initial_money + 100 or player.money == initial_money - 50 or player.money == initial_money + 50

def test_save_and_load_progress(tmp_path):
    player = Player("John", "Become a famous musician", "Artist")
    player.money = 1500
    player.reputation = 20
    save_file = tmp_path / "savegame.json"
    save_progress(player, save_file)
    loaded_player = Player.load_progress(save_file) # has save_file parameter
    assert loaded_player.name == "John"
    assert loaded_player.money == 1500
    assert loaded_player.reputation == 20

def test_solo_game(capsys):
    solo_game("Alice", "Become a successful entrepreneur", "Entrepreneur", actions=['work'])
    captured = capsys.readouterr()
    assert "Welcome, Alice!" in captured.out

def test_multiplayer_game(capsys):
    multiplayer_game(["Bob", "Charlie"], ["Open a restaurant", "Become a famous actor"], ["Entrepreneur", "Artist"], actions=['work', 'relax'])
    captured = capsys.readouterr()
    assert "Welcome, Bob!" in captured.out
    assert "Welcome, Charlie!" in captured.out

def test_custom_game(capsys):
    custom_game(2, ["David", "Eve", "Frank"], ["Become a famous writer", "Launch a tech startup", "Become a successful lawyer"], ["Artist", "Entrepreneur", "Entrepreneur"], actions=['network', 'work'])
    captured = capsys.readouterr()
    assert "Welcome, David!" in captured.out
    assert "Welcome, Eve!" in captured.out
    assert "Welcome, Frank!" not in captured.out

def test_load_game(tmp_path, capsys):
    save_file = tmp_path / "savegame.json"
    player = Player("John", "Become a famous musician", "Artist")
    save_progress(player, save_file)
    load_game(save_file, actions=['save'])
    captured = capsys.readouterr()
    assert "Welcome, John!" in captured.out