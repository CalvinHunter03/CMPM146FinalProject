import random
from Enemy import Enemy
from Player import Player
from Globals import weapons
import os




class Game():
    def __init__(self, player):
        self.round = 0
        self.player = player
        self.enemy = None
        self.over = False

    def start_round(self):
        self.round += 1
        self.enemy = Enemy(random.choice(weapons)) # init enemy here
        self.enemy.generate_name()
        
        # Set positions
        self.enemy.position = 40
        self.player.position = 10

        print(f"Round {self.round}...\n{self.enemy.name} enters the Arena!")

    # Returns 0 on player death, 1 on enemy death
    def check_end(self):
        if self.player.health == 0:
            print("You've died!")
            self.over = True
            return True
        elif self.enemy.health == 0:
            print(f"{self.enemy.name} has fallen!")
            return True
        return False
        
    
    # Outputs the game state to the console including the battlefield, distance between player and enemy, health, weapons
    # Currently prints at 100 characters wide, but can be changed as wanted
    def display_game(self, player):
        #output the field and distance between player and enemy
        field = []

        field.append((" " * player.position) + "o/" + (" " * (self.enemy.position - player.position - 2)) + "\o")
        field.append((" " * player.position) + "|" + (" " * (self.enemy.position - player.position)) + "|")
        field.append(("-" * 50))
        field.append((" " * player.position) + "P" + (" " * (self.enemy.position - player.position)) + "E")
        
        distance_text = f"Distance: {self.enemy.position - player.position} feet"
        field.append(distance_text.center(50))

        for line in field:
            #added spacing before the battlefield, because health and weapons uses so many characters
            empty_space = " " * 25
            print(empty_space + line)

        #output the health
        player_health = f"Player Health: [{'-' * (player.health // 10)}{'#' * (10 - player.health // 10)}] ({player.health})"
        enemy_health = f"Enemy Health: [{'-' * (self.enemy.health // 10)}{'#' * (10 - self.enemy.health // 10)}] ({self.enemy.health})"
        num_spaces = 100 - (len(player_health) + len(enemy_health))
        health_output = player_health + (" " * num_spaces) + enemy_health
        print(health_output)


        #output the weapons
        player_weapon = f"Player Weapon: {(player.weapon['name'])}"
        enemy_weapon = f"Enemy Weapon: {(self.enemy.weapon['name'])}"
        num_spaces = 100 - (len(player_weapon) + len(enemy_weapon))
        weapon_output = player_weapon + (" " * num_spaces) + enemy_weapon
        print(weapon_output)

    def clear_console():
        # Check if the operating system is Windows or not for console clearing
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')