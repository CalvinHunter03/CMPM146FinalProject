import random
import Player
import Enemy

# Weapons to choose from and their respective stats
weapons = [
    {
        "name": "Sword",
        "action": "Swing",
        "action2": "Riposte",
        "damage": 15,
        "range": 7
    },
    {
        "name": "Bow and Arrows",
        "action": "Shoot",
        "action2": "Quick Shot",
        "damage": 10,
        "range": 50
    },
    {
        "name": "Mace",
        "action": "Hit",
        "action2": "Break Shield",
        "damage": 25,
        "range": 5
    },
    {
        "name": "Flail",
        "action": "Swing",
        "action2": "Whirlwind",
        "damage": 20,
        "range": 10
    },
    {
        "name": "Spear and Sheild",
        "action": "Stab",
        "action2": "Block",
        "damage": 15,
        "range": 13
    }
]


class Game():
    def __init__(self, player):
        self.round = 0
        self.player = player
        self.enemy = None
        self.over

    def start_round(self):
        
        self.round += 1
        self.enemy = Enemy(random.choice(weapons)) # init enemy here
        
        # Set positions
        self.enemy.position = 40
        self.player.position = 10

        print(f"Round {self.round}...\n{self.enemy.name} enters the Arena!")

    # Returns 0 on player death, 1 on enemy death
    def check_end(self):
        if self.player.health == 0:
            print(f"You've died!")
            self.over = True
            return True
        elif self.enemy.health == 0:
            print(f"{self.enemy.name} has fallen!")
            return True
        return False
        
    
    # Outputs the game state to the console including the battlefield, distance between player and enemy, health, weapons
    # Currently prints at 100 characters wide, but can be changed as wanted
    def display_game(self, player, enemy):
        #output the field and distance between player and enemy
        field = []

        field[0] = (" " * player.position) + "o/" + (" " * (enemy.position - player.position)) + "\o"
        field[1] = (" " * player.position) + "|" + (" " * (enemy.position - player.position)) + "|"
        field[2] = ("-" * 50)
        field[3] = (" " * player.position) + "P" + (" " * (enemy.position - player.position)) + "E"
        
        distance_text = f"Distance: {enemy.position - player.position} feet"
        field[4] = distance_text.center(50)

        for line in field:
            #added spacing before the battlefield, because health and weapons uses so many characters
            empty_space = " " * 25
            print(empty_space + line)

        #output the health
        player_health = f"Player Health: [{"-" * (player.health // 10)}{"#" * (10 - player.health // 10)}] ({player.health})"
        enemy_health = f"Enemy Health: [{"-" * (enemy.health // 10)}{"#" * (10 - enemy.health // 10)}] ({enemy.health})"
        num_spaces = 100 - (len(player_health) + len(enemy_health))
        health_output = player_health + (" " * num_spaces) + enemy_health
        print(health_output)

        #output the weapons
        player_weapon = f"Player Weapon: {player.weapon}"
        enemy_weapon = f"Enemy Weapon: {enemy.weapon}"
        num_spaces = 100 - (len(player_weapon) + len(enemy_weapon))
        weapon_output = player_weapon + (" " * num_spaces) + enemy_weapon
        print(weapon_output)


        
