class Gear:
    def __init__(self, name, tags, stats):
        self.name = name
        self.tags = tags
        self.stats = stats
    
    def __str__(self):
        return self.name
