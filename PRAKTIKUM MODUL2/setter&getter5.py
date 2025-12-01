class Siswa:
    def __init__(self, nama, nilai) :
        self.nama = nama
        self.__nilai = 0#Ini memberi nilai awal (default) untuk atribut private __nilai.
        self.set_nilai(nilai) 

    # GETTER: Hanya untuk 'membaca'
    def get_nilai(self):
        print(f"(Akses getter untuk {self.nama})")
        return self.__nilai

    # SETTER: 'Satpam' untuk 'menulis'
    def set_nilai(self, nilai_baru): #method setter, yaitu agar nilai yang dimasukkan sesuai aturan.
        print(f"(Akses setter untuk {self.nama} dengan nilai {nilai_baru})")
        #Menampilkan informasi bahwa setter sedang di jalankan
        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
            print("-> Nilai berhasil diupdate.")
        else:
            print(f"-> Gagal! Nilai {nilai_baru} tidak valid. Harus antara 0-100.")


budi = Siswa("Budi", 70) 

budi.set_nilai(95)

budi.set_nilai(105)


print(f"Nilai Budi sekarang: {budi.get_nilai()}")





# kelemahan, Tidak bisa langsung mengakses atribut private
#Pengguna harus selalu memanggil get_nilai() dan set_nilai()
#tidak bisa budi.__nilai = 90.