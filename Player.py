from Game import Game
class Player():
    
    def __init__(self):
        self.weapon = Game.weapons[self.choose_weapon() - 1].get("name")
        self.health = 100
        self.position = 10
        self.is_blocking = False
        self.potions = 3
        

    
    def move_towards(self):
        new_distance = self.position + 5
        if new_distance > 50:
            new_distance = 50
        elif new_distance < 0:
            new_distance = 0
        self.position = new_distance
        
    def move_away(self):
        new_distance = self.position - 5
        if new_distance > 50:
            new_distance = 50
        elif new_distance < 0:
            new_distance = 0
        self.position = new_distance

    def heal(self):
        current_health = self.health 
        heal_amount = current_health // 2
        self.health += heal_amount
        
        if self.health > 100:
            self.health = 100
    
    


    def block(self):
        print(f"\nEnemy is blocking the next attack")
        self.is_blocking = True
   
    def display_legal_player_moves(self): #return a list of legal moves with certain weapon
        legal_moves = []

        for weapon in Game.weapons:
            if self.weapon == weapon.get("name"):
                legal_moves.append(weapon.get("action"))
                legal_moves.append(weapon.get("action2"))
            legal_moves.append("Move toward enemy")
            legal_moves.append("Move away from enemy")
            legal_moves.append("Use potion to heal")

        for move in legal_moves:
            x = 1
            printf('{x}) {move}\n')
            x+=1

    


    def choose_weapon():
            x = 1
            print(f'Choose your weapon!\n')
            for weapon in Game.weapons:
                print(f'{x}){weapon.get("name")}\n -Damage: {weapon.get("damage")}\n -Range: {weapon.get("range")}')
                x += 1
            
            # User input for weapon number
            weapon_choice = int(input("Enter a number: "))
            while (weapon_choice != 1 and weapon_choice != 2 and weapon_choice != 3 and weapon_choice != 4 and weapon_choice != 5):
                weapon_choice = int(input(f'Choose a valid weapon (Enter a number): '))

            return weapon_choice
            




