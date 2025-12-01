class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai 
    # 1. GETTER (menggunakan @property)
    @property
    def nilai(self):
        print("(Memanggil getter @property)")
        return self.__nilai
    # 2. SETTER (menggunakan @<nama_getter>.setter)
    @nilai.setter
    def nilai(self, nilai_baru):
        print(f"(Memanggil setter @nilai.setter dengan nilai {nilai_baru})")
        
        # Logika validasi ('satpam') tetap di sini
        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
        
susi = Siswa("Susi", 80)
# Output:
# (Memanggil setter @nilai.setter dengan nilai 80)
# -> Nilai berhasil diupdate.

print("-" * 20)

susi.nilai = 101 
print("-" * 20)

susi.nilai = 90  
print("-" * 20)

print(f"Nilai Susi sekarang: {susi.nilai}")

#Klasik (get_ / set_) Mudah dipahami pemula, tapi panjang
#Pythonic (@property) Lebih elegan, alami, dan efisien
#(@property) lebih disarankan karena membuat kode lebih bersih, mudah dibaca