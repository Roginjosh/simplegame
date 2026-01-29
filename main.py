
class Gear:
    def __init__(self, name, tags, stats):
        self.name = name
        self.tags = tags
        self.stats = stats
    
    def __str__(self):
        return self.name

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
        pass

    def __str__(self):
        return f'Name: {self.name}\nHP: {self.health}/{self.stats["max_health"]}\n\
Gear:\n\
Helm: {self.gear['head']}\n\
Chest: {self.gear['chest']}\n\
Legs: {self.gear['legs']}\n\
Boots: {self.gear['boots']}\n\
Main Hand: {self.gear['right hand']}\n\
Offhand: {self.gear['left hand']}\n\
'


def main():
    Josh = Character("Josh", {"max_health":100})
    sword = Gear("Sword of Compensation", ["right hand"], {"damage":3,"type":"physical"})
    print(Josh)

    Josh.equip_item(sword)
    print(Josh)

if __name__ == "__main__":
    main()