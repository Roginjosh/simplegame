import os
import json
from pathlib import Path

from character import Character
from premades import make_premade, goblin
from gear import Gear


def load_item_templates(path: str | Path = "data/items.json") -> dict:
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("items.json must be a JSON object mapping item_id -> item definition")
    return data

ITEMS = load_item_templates()


def show(a, b):
    print(a)
    print(b)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    josh_stats = {
    "STR":50,
    "DEX":50,
    "END":50,
    "VIT":50,
    "WIS":50,
    "INT":50,
}  

    Josh = Character("Josh", josh_stats)
    print("Pick an item for the upcoming battle:")
    for i in ITEMS:
        print(i)
    Josh.equip_item(ITEMS["sword_of_compensation"])
    enemy = make_premade(goblin)

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