class Mobil:
    
    total_mobil_dibuat = 0 #atribut,Karena milik seluruh class Mobil, bukan milik satu objek saja.

    def __init__(self, nama):
        self.nama = nama #karna setiap objek punya nama
        Mobil.total_mobil_dibuat += 1 
    def nyalakan_mesin(self): #method objek untuk menjalankan aksi tiap mobil
        print(f"Mesin {self.nama} menyala!")

    @classmethod #classmethod untuk mengakses atau menampilkan data class
    def get_total_produksi(cls):
        print(f"Pabrik telah memproduksi {cls.total_mobil_dibuat} unit mobil.")

#pungsi atribut menyimpan data atau informasi objek
Mobil.get_total_produksi() 

print("--- Membuat mobil ---")
avanza = Mobil("Avanza")
xenia = Mobil("Xenia")
print("---------------------")

Mobil.get_total_produksi()







#Digunakan untuk menjalankan class method tanpa perlu membuat objek terlebih dahulu.