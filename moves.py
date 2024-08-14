
from Globals import weapons

# This file consists of all the possible moves in the game

# General Moves #

# Move 5 positions forward
def move_towards(player):
    new_distance = player.position + 5
    if new_distance > 50:
        new_distance = 50
    elif new_distance < 0:
        new_distance = 0
    player.position = new_distance
    
# Move 5 positions backward
def move_away(player):
    new_distance = player.position - 5
    if new_distance > 50:
        new_distance = 50
    elif new_distance < 0:
        new_distance = 0
    player.position = new_distance

# Attack function, checks all available moves and prompts the player to pick one
#def attack(player):
#   available_actions = []
#   for weapon in weapons:
#       if weapon["name"] == player.weapon["name"]: 
#           available_actions = weapon["action"]
#
#
#
#


def block(player):
        print(f"\nEnemy is blocking the next attack")
        player.is_blocking = True

def heal(player):
    current_health = player.health 
    heal_amount = current_health // 2
    player.health += heal_amount
    
    if player.health > 100:
        player.health = 100

# Weapon Specific Moves #

