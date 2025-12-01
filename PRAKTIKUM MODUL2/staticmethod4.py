class Kalkulator:

    def __init__(self, nilai_awal):
        self.nilai = nilai_awal
    
    def tambah(self, angka):
        self.nilai += angka
        return self.nilai

    @staticmethod
    def kali(a, b):
        return a * b

calc = Kalkulator(10)
print(f"Hasil tambah: {calc.tambah(5)}")

print(f"Hasil kali: {Kalkulator.kali(5, 3)}")












#perbedaan
# tambah,method biasa, mengubah nilai dalam objek.
#kali,→ method statis, tidak butuh objek, hanya menghitung angka yang dikirim.


#calc adalah objek dari class Kalkulator.
#method adalah method objek yang menambah nilai objek (self.nilai)
#Awalnya self.nilai = 10, lalu ditambah 5 → hasilnya 15.
#Maka outputnya: 15
