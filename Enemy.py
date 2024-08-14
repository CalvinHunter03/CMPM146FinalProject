import random
import moves

class Enemy():
    def __init__(self, weapon):
        self.weapon = weapon
        self.health = 100
        self.position = 40
        self.name = "" # i have an idea for this 
        self.is_blocking = False

    def generate_name(self):
        names = [
            "Marcus",
            "Lucius",
            "Gaius",
            "Julius",
            "Publius",
            "Tiberius",
            "Aulus",
            "Decimus",
            "Quintus",
            "Setus",
            "Julia",
            "Claudia",
            "Livia",
            "Octavia",
            "Cornelia",
            "Aemilia",
            "Valeria",
            "Flavia",
            "Antonia",
            "Aurelia"]
        
        titles = [
            "the Barbarian",
            "the Conqueror",
            "the Wise",
            "the Great",
            "the Mighty",
            "the Fierce",
            "the Merciful",
            "the Just",
            "the Bold",
            "the Brave",
            "the Swift",
            "the Unstoppable",
            "the Silent",
            "the Jolly",
            "the Hungry",
            "the Fearless",
            "the Sassy",
            "the Sleepy",
            "the Unwashed",
            "the Magnificent"
        ]

        self.name = random.choice(names) + " " + random.choice(titles)


    
    def block(self):
        print(f"\nEnemy is blocking the next attack")
        self.is_blocking = True
   
   
    def move_towards(self):
        new_distance = self.position - 5
        if new_distance > 50:
            new_distance = 50
        elif new_distance < 0:
            new_distance = 0
        self.position = new_distance
        
    def move_away(self):
        new_distance = self.position + 5
        if new_distance > 50:
            new_distance = 50
        elif new_distance < 0:
            new_distance = 0
        self.position = new_distance

    

    
        
    
        