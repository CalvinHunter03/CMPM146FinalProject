from Globals import weapons
#from moves import moves
class Player():
    
    def __init__(self):
        self.weapon = weapons[self.choose_weapon() - 1] #.get("name")# # For now, lets make the weapon variable the weapon dictionary
        #self.weapon = weapons[self.choose_weapon() - 1].get("name")  # If we really need a variable for just the name, we can use this
        self.health = 100
        self.position = 10
        self.is_blocking = False
        self.potions = 3
        
    
    


    def block(self):
        print(f"\nEnemy is blocking the next attack")
        self.is_blocking = True
   
    def display_legal_player_moves(self): #return a list of legal moves with certain weapon
        legal_moves = []

        for weapon in weapons:
            if self.weapon == weapon.get("name"):
                for action in weapon.get("action"):
                    legal_moves.append(action[0])
                    legal_moves.append(action[1])
            legal_moves.append("Move toward enemy")
            legal_moves.append("Move away from enemy")
            legal_moves.append("Use potion to heal")

        for move in legal_moves:
            x = 1
            print(f'{x}) {move}\n')
            x+=1

    


    def choose_weapon(self):
            x = 1
            print(f'Choose your weapon!\n')
            for weapon in weapons:
                print(f'{x}){weapon.get("name")}\n -Damage: {weapon.get("damage")}\n -Range: {weapon.get("range")}')
                x += 1
            
            # User input for weapon number
            weapon_choice = int(input("Enter a number: "))
            while (weapon_choice != 1 and weapon_choice != 2 and weapon_choice != 3 and weapon_choice != 4 and weapon_choice != 5):
                weapon_choice = int(input(f'Choose a valid weapon (Enter a number): '))

            return weapon_choice
            



def main():
    p1 = Player()
    p1.display_legal_player_moves

if __name__ == '__main__':
    main()
