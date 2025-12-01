class Pegawai: #clas induk
    def __init__(self, nama, nip, gaji_pokok):
        self.nama = nama
        self.nip = nip
        self.__gaji_pokok = gaji_pokok   

    # getter gaji pokok
    def get_gaji_pokok(self):
        return self.__gaji_pokok

    # method hitung_bonus (akan di-override)
    def hitung_bonus(self):
        return 0

    # getter untuk gaji total
    def get_gaji_total(self):
        return self.__gaji_pokok + self.hitung_bonus()

    # menampilkan informasi pegawai
    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIP: {self.nip}")
        print(f"Gaji Pokok: Rp {self.__gaji_pokok:,}")


# ====================== Manager ======================
class Manager(Pegawai):
    def __init__(self, nama, nip, gaji_pokok, tunjangan_jabatan):
        super().__init__(nama, nip, gaji_pokok)
        self.tunjangan_jabatan = tunjangan_jabatan

    def hitung_bonus(self):
        return self.get_gaji_pokok() * 0.15  # bonus 15%

    def tampilkan_info(self):
        print("\n--- Info Manager ---")
        super().tampilkan_info()
        print(f"Tunjangan: Rp {self.tunjangan_jabatan:,}")
        print(f"Gaji Total Manager: Rp {self.get_gaji_total():,}")


# ====================== Staff Teknis ======================
class StaffTeknis(Pegawai):
    def __init__(self, nama, nip, gaji_pokok, jumlah_proyek):
        super().__init__(nama, nip, gaji_pokok)
        self.jumlah_proyek = jumlah_proyek

    def hitung_bonus(self):
        return 500_000 * self.jumlah_proyek  # 500k × jumlah proyek

    def tampilkan_info(self):
        print("\n--- Info Staff Teknis ---")
        super().tampilkan_info()
        print(f"Jumlah Proyek: {self.jumlah_proyek}")
        print(f"Gaji Total Staff: Rp {self.get_gaji_total():,}")


# ====================== Object ======================
manager1 = Manager("Budi Hartono", "M-001", 10_000_000, 5_000_000)
staff1 = StaffTeknis("Susi Susanti", "S-001", 6_000_000, 3)

manager1.tampilkan_info()
print("\n==============================")
staff1.tampilkan_info()
print("\n==============================")

# ====================== Bukti Enkapsulasi ======================
print("\n--- Tes Keamanan (Encapsulasi) ---")
try:
    print(staff1.__gaji_pokok)   
except Exception as e:
    print("ERROR:", e)
    print("-> TIDAK BISA diakses langsung dari luar!")

print(f"Gaji Total Susi (tetap): Rp {staff1.get_gaji_total():,}")
