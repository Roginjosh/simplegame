class Character:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        self.gear = {
            "head":"",
            "chest":"",
            "legs":"",
            "boots":"",
            "left hand":"",
            "right hand":"",
        }
        self.health = self.stats["max_health"]
    def equip_item(self, item):
        tags = item.tags
        free_slot = True
        for i in tags:
            if self.gear[i] != "":
                free_slot = False
        if free_slot:
            for i in tags:
                self.gear[i] = item

        
    def make_attack(self):
        str_cont = self.stats["strength"]//10
        gear_cont = 0
        for i in self.gear:
            item = self.gear[i]
            if item != "":
                if item.stats["type"] == "physical":
                    gear_cont += item.stats["damage"]
        return str_cont + gear_cont
    
    def take_damage(self, dmg):
        hp = self.health
        K = 100
        damage = dmg * K / (K + self.armor)
        hp -= damage
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
