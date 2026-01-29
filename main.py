import os
from character import Character
from premades import goblin_fighters
from gear import Gear

def show(a, b):
    print(a)
    print(b)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    Josh = Character("Josh", {"max_health":100, "strength":70})
    sword = Gear("Sword of Compensation", ["right hand"], {"damage":3,"type":"physical"})
    Josh.equip_item(sword)
    enemy = goblin_fighters[0]

    show(Josh, enemy)

    while Josh.health > 0 and enemy.health > 0:
        input("Whatcha gonna do?\n")
        enemy.take_damage(Josh.make_attack())
        Josh.take_damage(enemy.make_attack())
        clear_screen()
        show(Josh, enemy)
    
    if Josh.health > 0:
        print(f"Triumph! {Josh.name} the MIGHTY! May his foe rest in pieces.")
    else:
        print(f"Woe, for the just and righteous have fallen today.")

if __name__ == "__main__":
    main()