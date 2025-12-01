class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo

    def info(self):
        print(f"nama : {self.nama}")
        print("saldo : ERROR! tidak bisa mengakses saldo")

akun_budi = RekeningBank("Budi", 100000)
akun_budi.info()





















#Modifier adalah penanda tingkat akses suatu atribut di dalam class.
#jenis modifer = public = umum, protected = sebaiknya jgn, private = tidak bisa
