BASE_STATS = {
    "STR":50,
    "DEX":50,
    "END":50,
    "VIT":50,
    "WIS":50,
    "INT":50,
}
class Character:
    def __init__(self, name, stats = BASE_STATS):
        self.name = name
        self.stats = stats
        self.gear = []
        self.stats["max_health"] = self.stats["VIT"]
        self.health = self.stats["max_health"]
        self.update_armor()    
    def equip_item(self, item):
        islot = item["slot"]
        free = True
        for i in self.gear:
            if i["slot"] == islot:
                free = False
        if free:
            self.gear.append(item)
        
    def make_attack(self):
        str_cont = self.stats["STR"]//10
        gear_cont = 0
        for i in self.gear:
            weapon = {"damage_type": "flat", "base_damage": 0}
            if "weapon" in i:
                weapon = i["weapon"]
            dtype = weapon["damage_type"]
            dmg = weapon["base_damage"]
            if dtype in ["flat", "phys"]:
                gear_cont += dmg
        return str_cont + gear_cont
    
    def update_armor(self):
        armor = 0
        armor += self.stats["END"]//10
        for i in self.gear:
            gear = {"armor":0}
            if "armor" in i["tags"]:
                gear = i["stats"]
            armor += gear["armor"]
        self.armor = armor

    def take_damage(self, dmg):
        hp = self.health
        K = 100
        damage = dmg * K / (K + self.armor)
        hp -= round(damage)
        hp = max(hp, 0)
        self.health = hp
        print(f'{self.name} took {damage} damage.')

    def __str__(self):
        healthbar = ""
        perc = self.health/self.stats["max_health"]
        for i in range(20):
            if i < perc*20:
                healthbar += "█"
            else:
                healthbar += "░"
        return f'\
Name: {self.name}\n\
HP: {healthbar}\n\
    {self.health}/{self.stats["max_health"]}\n\
        '

    def __repr__(self):
        return f'\
Name: {self.name}\nHP: {self.health}/{self.stats["max_health"]}\n\
Gear:\n\
Helm: {self.gear['head']}\n\
Chest: {self.gear['chest']}\n\
Legs: {self.gear['legs']}\n\
Boots: {self.gear['boots']}\n\
Main Hand: {self.gear['right hand']}\n\
Offhand: {self.gear['left hand']}\n\
'
