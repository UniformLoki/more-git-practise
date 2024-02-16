from pokemon import Pokemon

class Togedemaru(Pokemon):
    ELEMENTAL_TYPE = "Lightning"
    
    def __init__(self, level):
        Pokemon.__init__(self ,"Togedemaru", level)
        
    def thunderbolt(self, other: Pokemon):
        print(f"{self.nickname} used thunderbolt on {other.nickname}")
        self.power_points -= 2
        other.current_hp -= 3