class Hero:

    jumlah = 0    #variabel                  
    __privateJumlah = 0             

    def __init__(self, name, health): #konstruktor
        self.name = name        
        self.health = health    
        self.__private = 'private'
        self._protected = 'protected'
           

# Membuat objek
hero_1 = Hero('Atsu', 100)

print(hero_1.__dict__)
print(Hero.__dict__)
print(Hero._Hero__privateJumlah)
















#jumlah → terbuka untuk umum
#__privateJumlah → hanya bisa diakses di dalam class
#Karena atribut private tidak bisa diakses langsung dari luar class