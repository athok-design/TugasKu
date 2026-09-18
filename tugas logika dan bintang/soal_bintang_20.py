"""
Tugas Matkul: Pemrograman Berorientasi Objek

20 Soal Formasi Bintang 
"""


class Soal01:
    def __init__(self):
        self.nomor = 1
        self.judul = "Dua segitiga mengerucut ke tengah (lebar 11)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")

        # baris pertama: bintang penuh
        baris = ""
        for i in range(11):
            baris = baris + "*"
        print(baris)

        # baris berikutnya: makin sedikit bintang, ada spasi di tengah
        for jumlah in range(5, 0, -1):
            baris = ""
            for i in range(jumlah):
                baris = baris + "*"
            baris = baris + " "
            for i in range(jumlah):
                baris = baris + "*"
            print(baris)


class Soal02:
    def __init__(self):
        self.nomor = 2
        self.judul = "Piramida bintang (meruncing ke atas)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        for jumlah in range(1, 12, 2):
            spasi = (11 - jumlah) // 2

            baris = ""
            for i in range(spasi):
                baris = baris + " "
            for i in range(jumlah):
                baris = baris + "*"
            print(baris)


class Soal03:
    def __init__(self):
        self.nomor = 3
        self.judul = "Dua segitiga kecil (kiri lalu kanan)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")

        # segitiga pertama, rata kiri
        for jumlah in range(1, 4):
            baris = ""
            for i in range(jumlah):
                baris = baris + "*"
            print(baris)

        # segitiga kedua, rata kanan
        for jumlah in range(1, 4):
            spasi = 3 - jumlah
            baris = ""
            for i in range(spasi):
                baris = baris + " "
            for i in range(jumlah):
                baris = baris + "*"
            print(baris)


class Soal04:
    def __init__(self):
        self.nomor = 4
        self.judul = "Dua segitiga melebar dari tengah, ditutup garis penuh"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")

        for jumlah in range(1, 6):
            baris = ""
            for i in range(jumlah):
                baris = baris + "*"
            baris = baris + " "
            for i in range(jumlah):
                baris = baris + "*"
            print(baris)

        baris = ""
        for i in range(11):
            baris = baris + "*"
        print(baris)


class Soal05:
    def __init__(self):
        self.nomor = 5
        self.judul = "Piramida terbalik (meruncing ke bawah)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        for jumlah in range(11, 0, -2):
            spasi = (11 - jumlah) // 2

            baris = ""
            for i in range(spasi):
                baris = baris + " "
            for i in range(jumlah):
                baris = baris + "*"
            print(baris)


class Soal06:
    def __init__(self):
        self.nomor = 6
        self.judul = "Dua segitiga kecil (kanan lalu kiri)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")

        # segitiga pertama, rata kanan
        for jumlah in range(1, 4):
            spasi = 3 - jumlah
            baris = ""
            for i in range(spasi):
                baris = baris + " "
            for i in range(jumlah):
                baris = baris + "*"
            print(baris)

        # segitiga kedua, rata kiri
        for jumlah in range(1, 4):
            baris = ""
            for i in range(jumlah):
                baris = baris + "*"
            print(baris)


class Soal07:
    def __init__(self):
        self.nomor = 7
        self.judul = "Formasi jam pasir (lebar 5)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        urutan_jumlah = [5, 4, 3, 2, 1, 2, 3, 4, 5]

        for jumlah in urutan_jumlah:
            spasi = 5 - jumlah
            baris = ""
            for i in range(spasi):
                baris = baris + " "
            for i in range(jumlah):
                baris = baris + "*"
            print(baris)


class Soal08:
    def __init__(self):
        self.nomor = 8
        self.judul = "Kotak bintang dengan pembatas 0 di kiri, alas 0"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")

        for baris_ke in range(5):
            baris = "0"
            for i in range(10):
                baris = baris + "*"
            print(baris)

        baris = ""
        for i in range(11):
            baris = baris + "0"
        print(baris)


class Soal09:
    def __init__(self):
        self.nomor = 9
        self.judul = "Kotak bintang dengan pembatas 0 di kanan, alas 0"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")

        for baris_ke in range(5):
            baris = ""
            for i in range(10):
                baris = baris + "*"
            baris = baris + "0"
            print(baris)

        baris = ""
        for i in range(11):
            baris = baris + "0"
        print(baris)


class Soal10:
    def __init__(self):
        self.nomor = 10
        self.judul = "Formasi jam pasir (lebar 6)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        urutan_jumlah = [6, 5, 4, 3, 2, 1, 2, 3, 4, 5]

        for jumlah in urutan_jumlah:
            spasi = 6 - jumlah
            baris = ""
            for i in range(spasi):
                baris = baris + " "
            for i in range(jumlah):
                baris = baris + "*"
            print(baris)


class Soal11:
    def __init__(self):
        self.nomor = 11
        self.judul = "Atap 0, badan kotak bintang dengan pembatas 0 di kiri"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")

        baris = ""
        for i in range(11):
            baris = baris + "0"
        print(baris)

        for baris_ke in range(5):
            baris = "0"
            for i in range(10):
                baris = baris + "*"
            print(baris)


class Soal12:
    def __init__(self):
        self.nomor = 12
        self.judul = "Atap 0, badan kotak bintang dengan pembatas 0 di kanan"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")

        baris = ""
        for i in range(11):
            baris = baris + "0"
        print(baris)

        for baris_ke in range(5):
            baris = ""
            for i in range(10):
                baris = baris + "*"
            baris = baris + "0"
            print(baris)


class Soal13:
    def __init__(self):
        self.nomor = 13
        self.judul = "Diagonal: 0 dari kiri bertambah, bintang mengecil ke kanan"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        for i in range(1, 7):
            baris = ""
            for j in range(i):
                baris = baris + "0"
            for j in range(7 - i):
                baris = baris + "*"
            print(baris)


class Soal14:
    def __init__(self):
        self.nomor = 14
        self.judul = "Diagonal: bintang dari kiri bertambah, 0 mengecil ke kanan"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        for i in range(1, 7):
            baris = ""
            for j in range(i):
                baris = baris + "*"
            for j in range(7 - i):
                baris = baris + "0"
            print(baris)


class Soal15:
    def __init__(self):
        self.nomor = 15
        self.judul = "Diagonal: 0 mengecil dari kiri, bintang bertambah ke kanan"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        for i in range(1, 7):
            baris = ""
            for j in range(7 - i):
                baris = baris + "0"
            for j in range(i):
                baris = baris + "*"
            print(baris)


class Soal16:
    def __init__(self):
        self.nomor = 16
        self.judul = "Diagonal: 0 mengecil dari kiri, bintang bertambah ke kanan (variasi)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        for i in range(1, 7):
            baris = ""
            for j in range(7 - i):
                baris = baris + "0"
            for j in range(i):
                baris = baris + "*"
            print(baris)


class Soal17:
    def __init__(self):
        self.nomor = 17
        self.judul = "Bintang tunggal bergeser diagonal dari kanan ke kiri"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        lebar = 7
        for i in range(6):
            posisi_bintang = lebar - 1 - i
            baris = ""
            for kolom in range(lebar):
                if kolom == posisi_bintang:
                    baris = baris + "*"
                else:
                    baris = baris + "0"
            print(baris)


class Soal18:
    def __init__(self):
        self.nomor = 18
        self.judul = "Bintang tunggal bergeser diagonal dari kiri ke kanan"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        lebar = 7
        for i in range(6):
            posisi_bintang = i
            baris = ""
            for kolom in range(lebar):
                if kolom == posisi_bintang:
                    baris = baris + "*"
                else:
                    baris = baris + "0"
            print(baris)


class Soal19:
    def __init__(self):
        self.nomor = 19
        self.judul = "Kotak berongga: bingkai 0, isi bintang"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")

        baris = ""
        for i in range(7):
            baris = baris + "0"
        print(baris)

        for baris_ke in range(4):
            baris = "0"
            for i in range(5):
                baris = baris + "*"
            baris = baris + "0"
            print(baris)

        baris = ""
        for i in range(7):
            baris = baris + "0"
        print(baris)


class Soal20:
    def __init__(self):
        self.nomor = 20
        self.judul = "Blok berulang: baris 0, baris bintang, baris sama-dengan"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")

        for ulangan in range(2):
            baris_nol = ""
            baris_bintang = ""
            baris_sama = ""
            for i in range(7):
                baris_nol = baris_nol + "0"
                baris_bintang = baris_bintang + "*"
                baris_sama = baris_sama + "="
            print(baris_nol)
            print(baris_bintang)
            print(baris_sama)


# ======================================================
# PROGRAM UTAMA (MENU)
# ======================================================
def buat_semua_soal():
    daftar = []
    daftar.append(Soal01())
    daftar.append(Soal02())
    daftar.append(Soal03())
    daftar.append(Soal04())
    daftar.append(Soal05())
    daftar.append(Soal06())
    daftar.append(Soal07())
    daftar.append(Soal08())
    daftar.append(Soal09())
    daftar.append(Soal10())
    daftar.append(Soal11())
    daftar.append(Soal12())
    daftar.append(Soal13())
    daftar.append(Soal14())
    daftar.append(Soal15())
    daftar.append(Soal16())
    daftar.append(Soal17())
    daftar.append(Soal18())
    daftar.append(Soal19())
    daftar.append(Soal20())
    return daftar


def main():
    daftar_soal = buat_semua_soal()

    while True:
        print("\n==================================================")
        print("DAFTAR SOAL FORMASI BINTANG (1-20)")
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
