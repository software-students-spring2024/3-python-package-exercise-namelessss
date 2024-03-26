# new_york_minute/new_york_minute/events.py

import random

def handle_event(location):
    events = {
        'Brooklyn': 'attend a local art show',
        'Manhattan': 'visit a famous landmark',
        'Queens': 'explore diverse neighborhoods',
        'The Bronx': 'watch a baseball game',
        'Staten Island': 'take a ferry ride and enjoy the view',
        'Central Park': 'enjoy a peaceful walk and meet new friends',
        'Wall Street': 'take a finance workshop to boost your money management skills',
        'Harlem': 'attend a live jazz night and unwind'
    }
    
    return events.get(location, "just explore the city")

def random_event(player):
    event_chance = random.randint(1, 10)
    if event_chance > 8:
        print("You found $100 on the street!")
        player.money += 100
    elif event_chance < 3:
        print("Oh no! You lost your metro card.")
        player.money -= 50
    elif event_chance == 4:
        print("You met a street performer and earned $50.")
        player.money += 50
    elif event_chance == 5:
        print("You got a discount coupon for a local restaurant.")
    elif event_chance == 6:
        print("You stumbled upon a free outdoor concert.")
    elif event_chance == 7:
        print("You found a rare collectible item.")
    else:
        print("Nothing out of the ordinary happened.")
