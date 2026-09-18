"""
Soal minggu 1

1. Grid Nilai Siswa
2. Pola Bintang: Piramida
"""


# ===============================
# BAGIAN 1 : GRID NILAI SISWA
# =============================
class Siswa:
    """
    Class ini mewakili satu siswa.
    Menyimpan nama siswa dan satu nilai miliknya.
    """

    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def tentukan_grade(self):
        if self.nilai > 90:
            grade = "A"
        elif self.nilai > 80:
            grade = "B"
        else:
            grade = "C"
        return grade


class GridNilai:
    def __init__(self):
        self.nomor = 1
        self.judul = "Grid Nilai Siswa"

    def input_data_siswa(self):
        jumlah_siswa = int(input("Masukkan jumlah siswa: "))

        daftar_siswa = []  # tempat menyimpan semua object Siswa

        for i in range(jumlah_siswa):
            print("\n-- Data siswa ke-" + str(i + 1) + " --")
            nama = input("Nama siswa: ")
            nilai = float(input("Nilai: "))

            siswa_baru = Siswa(nama, nilai)
            daftar_siswa.append(siswa_baru)

        return daftar_siswa

    def tampilkan_grid(self, daftar_siswa):
        print("\n=== GRID NILAI SISWA ===")
        print("Nama            Nilai       Grade")
        print("--------------------------------------")

        for siswa in daftar_siswa:
            baris = siswa.nama.ljust(16) + str(siswa.nilai).ljust(12) + siswa.tentukan_grade()
            print(baris)

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        daftar_siswa = self.input_data_siswa()
        self.tampilkan_grid(daftar_siswa)


# =====================================
# BAGIAN 2 : POLA BINTANG (PIRAMIDA)
# =======================================
class Piramida:
    def __init__(self):
        self.nomor = 2
        self.judul = "Pola Bintang: Piramida"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        tinggi = int(input("Masukkan jumlah baris: "))

        lebar = (2 * tinggi) - 1

        for i in range(1, tinggi + 1):
            jumlah_bintang = (2 * i) - 1
            jumlah_spasi = (lebar - jumlah_bintang) // 2

            baris = ""
            for s in range(jumlah_spasi):
                baris = baris + " "
            for b in range(jumlah_bintang):
                baris = baris + "*"
            print(baris)


# ==========================
# PROGRAM UTAMA (MENU)
# =============================
def buat_semua_soal():
    daftar = []
    daftar.append(GridNilai())
    daftar.append(Piramida())
    return daftar


def main():
    daftar_soal = buat_semua_soal()

    while True:
        print("\n==================================================")
        print("DAFTAR SOAL TAMBAHAN (1-2)")
        print("==================================================")
        for soal in daftar_soal:
            print(str(soal.nomor) + ". " + soal.judul)
        print("0. Keluar")

        pilihan = input("\nPilih nomor soal yang ingin dijalankan: ")

        if pilihan == "0":
            print("Program selesai.")
            break

        ditemukan = False
        for soal in daftar_soal:
            if str(soal.nomor) == pilihan:
                soal.jalankan()
                ditemukan = True
                break

        if not ditemukan:
            print("Nomor soal tidak valid, coba lagi.")


main()
