import random
from character import Character

# goblin_fighters = [
# Character("Grog", {"max_health":35, "strength":40}),
# Character("Blarg", {"max_health":42, "strength":32}),
# Character("Slgar", {"max_health":55, "strength":18}),
# Character("Frang", {"max_health":15, "strength":65}),
# Character("Tronst", {"max_health":29, "strength":22}),
# ]

BASE_STATS = {
    "STR":50,
    "DEX":50,
    "END":50,
    "VIT":50,
    "WIS":50,
    "INT":50,
}

goblin = {
    "names":[
        "Grog",
        "Blarg",
        "Slgar",
        "Frang",
        "Tronst",
        "Gorsp",
        "Terry", # Thanks Sophia
        "Sophia",
        "Natalie", # Also Sophia
        "Sklate",        
    ],
    "base":{
        "STR":30,
        "DEX":20,
        "END":30,
        "VIT":30,
        "WIS":10,
        "INT":20,
    },
    "variance":10
}

def make_premade(monster):
    name = random.choice(monster["names"])
    var = []
    stats = monster["base"].copy()
    for key in stats:
        stats[key] += round(random.uniform(-1,1)*monster["variance"])
    return Character(name, stats)
    

