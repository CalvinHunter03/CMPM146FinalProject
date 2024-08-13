weapons = [
    {
        "name": "Sword",
        "action": "Swing",
        "damage": 15,
        "range": 7
    },
    {
        "name": "Bow and Arrows",
        "action": "Shoot",
        "damage": 10,
        "range": 50
    },
    {
        "name": "Mace",
        "action": "Hit",
        "damage": 25,
        "range": 5
    },
    {
        "name": "Flail",
        "action": "Swing",
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

def choose_weapon():
    x = 1
    print(f'Choose your weapon!\n')
    for weapon in weapons:
        print(f'{x}){weapon.get("name")}\n -Damage: {weapon.get("damage")}\n -Range: {weapon.get("range")}')
        x += 1
        
    weapon_choice = int(input("Enter a number: "))
    while (weapon_choice != 1 and weapon_choice != 2 and weapon_choice != 3 and weapon_choice != 4 and weapon_choice != 5):
        weapon_choice = int(input(f'Choose a valid weapon (Enter a number): '))

    return weapon_choice
        
print(choose_weapon())

