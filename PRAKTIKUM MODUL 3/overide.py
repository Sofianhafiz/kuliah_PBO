class Hero:
    # Constructor class induk (parent class)
    def __init__(self,name,health):
        self.name = name      
        self.health = health  

    # Method 
    def showInfo(self):
        print("showInfo di class Hero")
        print("{} health: {}".format(
            self.name,
            self.health
            )
        )
class Hero_intelligent(Hero):
    # Constructor pada subclass
    def __init__(self,name):
        super().__init__(name,100)

    # Override method showInfo() milik class induk
    def showInfo(self):
        print("showInfo di subclass Hero_intelligent")
        
        print("{} \n\tTipe: intelligent, \n\thealth: {}".format(
            self.name,
            self.health
            )
        )
# Class Hero_strength juga turunan dari Hero
class Hero_strength(Hero):
    def __init__(self,name):
        super().__init__(name,200)  # memanggil constructor parent

lina = Hero_intelligent('lina')#int
axe = Hero_strength('axe')#str
# Memanggil method showInfo() milik lina
lina.showInfo()
