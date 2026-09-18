"""
Tugas Matkul: Pemrograman Berorientasi Objek 

50 Soal Logika & Angka

"""

# ======================================================
# Fungsi bantu sederhana (dipakai di beberapa soal)
# ======================================================
def cek_prima(n):
    # Bilangan kurang dari 2 bukan prima
    if n < 2:
        return False
    # Coba bagi dari 2 sampai n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def cek_kabisat(tahun):
    if tahun % 4 == 0 and tahun % 100 != 0:
        return True
    if tahun % 400 == 0:
        return True
    return False


# ======================================================
# SOAL 1 - 3 : Kalimat
# ======================================================
class Soal01:
    def __init__(self):
        self.nomor = 1
        self.judul = "Membalik kalimat"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        kalimat = input("Masukkan kalimat: ")

        hasil = ""
        panjang = len(kalimat)
        for i in range(panjang - 1, -1, -1):
            hasil = hasil + kalimat[i]

        print("Hasil terbalik:", hasil)


class Soal02:
    def __init__(self):
        self.nomor = 2
        self.judul = "Menghitung jumlah huruf tertentu dalam kalimat"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        kalimat = input("Masukkan kalimat: ")
        huruf = input("Huruf yang dicari: ")

        kalimat = kalimat.lower()
        huruf = huruf.lower()

        jumlah = 0
        for karakter in kalimat:
            if karakter == huruf:
                jumlah = jumlah + 1

        print("Jumlah huruf '" + huruf + "' dalam kalimat:", jumlah)


class Soal03:
    def __init__(self):
        self.nomor = 3
        self.judul = "Menghitung jumlah karakter dalam kalimat"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        kalimat = input("Masukkan kalimat: ")

        jumlah = 0
        for karakter in kalimat:
            jumlah = jumlah + 1

        print("Jumlah karakter:", jumlah)


# ======================================================
# SOAL 4 - 15 : Pola angka
# ======================================================
class Soal04:
    def __init__(self):
        self.nomor = 4
        self.judul = "Pola angka 122333444455555666666"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        baris = ""
        for i in range(1, 7):
            for j in range(i):
                baris = baris + str(i)
        print(baris)


class Soal05:
    def __init__(self):
        self.nomor = 5
        self.judul = "Pola angka 666666555554444333221"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        baris = ""
        for i in range(6, 0, -1):
            for j in range(i):
                baris = baris + str(i)
        print(baris)


class Soal06:
    def __init__(self):
        self.nomor = 6
        self.judul = "Pola angka 112123123412345123456"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        baris = ""
        for i in range(1, 7):
            for angka in range(1, i + 1):
                baris = baris + str(angka)
        print(baris)


class Soal07:
    def __init__(self):
        self.nomor = 7
        self.judul = "Pola angka 654321543214321321211"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        baris = ""
        for i in range(6, 0, -1):
            for angka in range(i, 0, -1):
                baris = baris + str(angka)
        print(baris)


class Soal08:
    def __init__(self):
        self.nomor = 8
        self.judul = "Pola angka 112333123455555123456"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        baris = ""
        for i in range(1, 7):
            if i % 2 == 1:
                for j in range(i):
                    baris = baris + str(i)
            else:
                for angka in range(1, i + 1):
                    baris = baris + str(angka)
        print(baris)


class Soal09:
    def __init__(self):
        self.nomor = 9
        self.judul = "Pola angka 122123444412345666666"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        baris = ""
        for i in range(1, 7):
            if i % 2 == 1:
                for angka in range(1, i + 1):
                    baris = baris + str(angka)
            else:
                for j in range(i):
                    baris = baris + str(i)
        print(baris)


class Soal10:
    def __init__(self):
        self.nomor = 10
        self.judul = "Pola angka 654321555554321333211"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        baris = ""
        for i in range(6, 0, -1):
            if i % 2 == 0:
                for angka in range(i, 0, -1):
                    baris = baris + str(angka)
            else:
                for j in range(i):
                    baris = baris + str(i)
        print(baris)


class Soal11:
    def __init__(self):
        self.nomor = 11
        self.judul = "Pola angka 666666123454444123221"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        baris = ""
        for i in range(6, 0, -1):
            if i % 2 == 0:
                for j in range(i):
                    baris = baris + str(i)
            else:
                for angka in range(1, i + 1):
                    baris = baris + str(angka)
        print(baris)


class Soal12:
    def __init__(self):
        self.nomor = 12
        self.judul = "Pola angka lanjutan 1 s.d. 9 (variasi dari soal 8)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        # Catatan: di soal aslinya pola ditulis dengan "..." (dilanjutkan).
        # Di sini dilanjutkan pakai aturan yang sama seperti soal 8.
        baris = ""
        for i in range(1, 10):
            if i % 2 == 1:
                for j in range(i):
                    baris = baris + str(i)
            else:
                for angka in range(1, i + 1):
                    baris = baris + str(angka)
        print(baris)


class Soal13:
    def __init__(self):
        self.nomor = 13
        self.judul = "Pola angka lanjutan 1 s.d. 9 (variasi dari soal 9)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        # Catatan: sama seperti soal 12, mengikuti aturan soal 9 diteruskan sampai 9.
        baris = ""
        for i in range(1, 10):
            if i % 2 == 1:
                for angka in range(1, i + 1):
                    baris = baris + str(angka)
            else:
                for j in range(i):
                    baris = baris + str(i)
        print(baris)


class Soal14:
    def __init__(self):
        self.nomor = 14
        self.judul = "Pola angka 888888887777777654321543214444333211"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        baris = ""
        for i in range(8, 0, -1):
            kelompok = (i + 1) // 2
            if kelompok % 2 == 0:
                for j in range(i):
                    baris = baris + str(i)
            else:
                for angka in range(i, 0, -1):
                    baris = baris + str(angka)
        print(baris)


class Soal15:
    def __init__(self):
        self.nomor = 15
        self.judul = "Pola angka 876543217654321666666555554321321221"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        baris = ""
        for i in range(8, 0, -1):
            kelompok = (i + 1) // 2
            if kelompok % 2 == 0:
                for angka in range(i, 0, -1):
                    baris = baris + str(angka)
            else:
                for j in range(i):
                    baris = baris + str(i)
        print(baris)


# ======================================================
# SOAL 16 - 21 : Deret angka
# ======================================================
class Soal16:
    def __init__(self):
        self.nomor = 16
        self.judul = "Deret 1 5 3 7 5 9 7 11 9 13 11 15 (n+4, n-2, ...)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        n = 1
        deret = [n]
        giliran = 0
        for i in range(11):
            if giliran == 0:
                n = n + 4
            else:
                n = n - 2
            deret.append(n)
            giliran = 1 - giliran
        print(deret)


class Soal17:
    def __init__(self):
        self.nomor = 17
        self.judul = "Deret 2 12 7 17 12 22 17 27 22 32 (n+10, n-5, ...)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        n = 2
        deret = [n]
        giliran = 0
        for i in range(9):
            if giliran == 0:
                n = n + 10
            else:
                n = n - 5
            deret.append(n)
            giliran = 1 - giliran
        print(deret)


class Soal18:
    def __init__(self):
        self.nomor = 18
        self.judul = "Deret 5 2 7 4 9 6 11 8 13 10 15 12 (n-3, n+5, ...)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        n = 5
        deret = [n]
        giliran = 0
        for i in range(11):
            if giliran == 0:
                n = n - 3
            else:
                n = n + 5
            deret.append(n)
            giliran = 1 - giliran
        print(deret)


class Soal19:
    def __init__(self):
        self.nomor = 19
        self.judul = "Deret 3 9 4 12 7 21 16 48 43 129 (n*3, n-5, ...)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        n = 3
        deret = [n]
        giliran = 0
        for i in range(9):
            if giliran == 0:
                n = n * 3
            else:
                n = n - 5
            deret.append(n)
            giliran = 1 - giliran
        print(deret)


class Soal20:
    def __init__(self):
        self.nomor = 20
        self.judul = "Deret 1 2 4 7 8 10 13 14 16 19 20 22 25 (n+1, n+2, n+3, ...)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        n = 1
        deret = [n]
        tambah = [1, 2, 3]
        index = 0
        for i in range(12):
            n = n + tambah[index]
            deret.append(n)
            index = index + 1
            if index == 3:
                index = 0
        print(deret)


class Soal21:
    def __init__(self):
        self.nomor = 21
        self.judul = "Deret 1 2 4 8 16 32 64 128 256 512"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        deret = []
        nilai = 1
        for i in range(10):
            deret.append(nilai)
            nilai = nilai * 2
        print(deret)


# ======================================================
# SOAL 22 - 23 : Faktorial & Fibonacci
# ======================================================
class Soal22:
    def __init__(self):
        self.nomor = 22
        self.judul = "Faktorial n!"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        n = int(input("Masukkan n: "))

        hasil = 1
        proses = ""
        for i in range(n, 0, -1):
            hasil = hasil * i
            if i == 1:
                proses = proses + str(i)
            else:
                proses = proses + str(i) + " x "

        print(str(n) + "! = " + proses + " = " + str(hasil))


class Soal23:
    def __init__(self):
        self.nomor = 23
        self.judul = "Bilangan Fibonacci sampai nilai maksimum"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        maksimum = int(input("Masukkan nilai maksimum: "))

        a = 0
        b = 1
        deret = []
        while a <= maksimum:
            deret.append(a)
            temp = a + b
            a = b
            b = temp

        print(deret)


# ======================================================
# SOAL 24 - 28 : Tahun kabisat akhiran tertentu
# (setiap soal dibuat sendiri-sendiri, tidak digabung,
#  supaya gampang dijelaskan satu-satu)
# ======================================================
class Soal24:
    def __init__(self):
        self.nomor = 24
        self.judul = "Tahun kabisat n_awal s.d n_akhir, angka terakhir 0"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        awal = int(input("Masukkan n_awal: "))
        akhir = int(input("Masukkan n_akhir: "))

        for tahun in range(awal, akhir + 1):
            if tahun % 10 == 0:
                if cek_kabisat(tahun):
                    print(tahun)


class Soal25:
    def __init__(self):
        self.nomor = 25
        self.judul = "Tahun kabisat n_awal s.d n_akhir, angka terakhir 2"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        awal = int(input("Masukkan n_awal: "))
        akhir = int(input("Masukkan n_akhir: "))

        for tahun in range(awal, akhir + 1):
            if tahun % 10 == 2:
                if cek_kabisat(tahun):
                    print(tahun)


class Soal26:
    def __init__(self):
        self.nomor = 26
        self.judul = "Tahun kabisat n_awal s.d n_akhir, angka terakhir 4"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        awal = int(input("Masukkan n_awal: "))
        akhir = int(input("Masukkan n_akhir: "))

        for tahun in range(awal, akhir + 1):
            if tahun % 10 == 4:
                if cek_kabisat(tahun):
                    print(tahun)


class Soal27:
    def __init__(self):
        self.nomor = 27
        self.judul = "Tahun kabisat n_awal s.d n_akhir, angka terakhir 6"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        awal = int(input("Masukkan n_awal: "))
        akhir = int(input("Masukkan n_akhir: "))

        for tahun in range(awal, akhir + 1):
            if tahun % 10 == 6:
                if cek_kabisat(tahun):
                    print(tahun)


class Soal28:
    def __init__(self):
        self.nomor = 28
        self.judul = "Tahun kabisat n_awal s.d n_akhir, angka terakhir 8"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        awal = int(input("Masukkan n_awal: "))
        akhir = int(input("Masukkan n_akhir: "))

        for tahun in range(awal, akhir + 1):
            if tahun % 10 == 8:
                if cek_kabisat(tahun):
                    print(tahun)


# ======================================================
# SOAL 29 - 33 : Bilangan habis dibagi n
# ======================================================
class Soal29:
    def __init__(self):
        self.nomor = 29
        self.judul = "Bilangan habis dibagi 3 dari n_awal s.d n_akhir"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        awal = int(input("Masukkan n_awal: "))
        akhir = int(input("Masukkan n_akhir: "))

        for angka in range(awal, akhir + 1):
            if angka % 3 == 0:
                print(angka)


class Soal30:
    def __init__(self):
        self.nomor = 30
        self.judul = "Bilangan habis dibagi 4 dari n_awal s.d n_akhir"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        awal = int(input("Masukkan n_awal: "))
        akhir = int(input("Masukkan n_akhir: "))

        for angka in range(awal, akhir + 1):
            if angka % 4 == 0:
                print(angka)


class Soal31:
    def __init__(self):
        self.nomor = 31
        self.judul = "Bilangan habis dibagi 5 dari n_awal s.d n_akhir"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        awal = int(input("Masukkan n_awal: "))
        akhir = int(input("Masukkan n_akhir: "))

        for angka in range(awal, akhir + 1):
            if angka % 5 == 0:
                print(angka)


class Soal32:
    def __init__(self):
        self.nomor = 32
        self.judul = "Bilangan habis dibagi 6 dari n_awal s.d n_akhir"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        awal = int(input("Masukkan n_awal: "))
        akhir = int(input("Masukkan n_akhir: "))

        for angka in range(awal, akhir + 1):
            if angka % 6 == 0:
                print(angka)


class Soal33:
    def __init__(self):
        self.nomor = 33
        self.judul = "Bilangan habis dibagi 7 dari n_awal s.d n_akhir"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        awal = int(input("Masukkan n_awal: "))
        akhir = int(input("Masukkan n_akhir: "))

        for angka in range(awal, akhir + 1):
            if angka % 7 == 0:
                print(angka)


# ======================================================
# SOAL 34 - 41 : Animasi angka 0 (disimulasikan per baris/frame)
# Karena dijalankan di terminal, animasi ditampilkan sebagai
# beberapa "frame" berurutan, posisi angka 0 berpindah.
# ======================================================
class Soal34:
    def __init__(self):
        self.nomor = 34
        self.judul = "Animasi 0: kiri->kanan lalu kiri->kanan lagi (baris atas)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        lebar = 11
        posisi_list = []
        for p in range(lebar):
            posisi_list.append(p)
        for p in range(lebar):
            posisi_list.append(p)

        for posisi in posisi_list:
            baris = ""
            for kolom in range(lebar):
                if kolom == posisi:
                    baris = baris + "0"
                else:
                    baris = baris + " "
            print(baris)


class Soal35:
    def __init__(self):
        self.nomor = 35
        self.judul = "Animasi 0: kiri->kanan lalu kanan->kiri (baris atas)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        lebar = 11
        posisi_list = []
        for p in range(lebar):
            posisi_list.append(p)
        for p in range(lebar - 1, -1, -1):
            posisi_list.append(p)

        for posisi in posisi_list:
            baris = ""
            for kolom in range(lebar):
                if kolom == posisi:
                    baris = baris + "0"
                else:
                    baris = baris + " "
            print(baris)


class Soal36:
    def __init__(self):
        self.nomor = 36
        self.judul = "Animasi 0: kiri->kanan lalu kiri->kanan lagi (baris bawah)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        lebar = 11
        posisi_list = []
        for p in range(lebar):
            posisi_list.append(p)
        for p in range(lebar):
            posisi_list.append(p)

        for posisi in posisi_list:
            baris = ""
            for kolom in range(lebar):
                if kolom == posisi:
                    baris = baris + "0"
                else:
                    baris = baris + " "
            print(baris)


class Soal37:
    def __init__(self):
        self.nomor = 37
        self.judul = "Animasi 0: kiri->kanan lalu kanan->kiri (baris bawah)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        lebar = 11
        posisi_list = []
        for p in range(lebar):
            posisi_list.append(p)
        for p in range(lebar - 1, -1, -1):
            posisi_list.append(p)

        for posisi in posisi_list:
            baris = ""
            for kolom in range(lebar):
                if kolom == posisi:
                    baris = baris + "0"
                else:
                    baris = baris + " "
            print(baris)


class Soal38:
    def __init__(self):
        self.nomor = 38
        self.judul = "Animasi 0: atas->bawah lalu atas->bawah lagi (kolom kiri)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        tinggi = 8
        posisi_list = []
        for p in range(tinggi):
            posisi_list.append(p)
        for p in range(tinggi):
            posisi_list.append(p)

        for posisi in posisi_list:
            for baris_ke in range(tinggi):
                if baris_ke == posisi:
                    print("0")
                else:
                    print(" ")
            print("---")  # pemisah antar frame


class Soal39:
    def __init__(self):
        self.nomor = 39
        self.judul = "Animasi 0: atas->bawah lalu bawah->atas (kolom kiri)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        tinggi = 8
        posisi_list = []
        for p in range(tinggi):
            posisi_list.append(p)
        for p in range(tinggi - 1, -1, -1):
            posisi_list.append(p)

        for posisi in posisi_list:
            for baris_ke in range(tinggi):
                if baris_ke == posisi:
                    print("0")
                else:
                    print(" ")
            print("---")


class Soal40:
    def __init__(self):
        self.nomor = 40
        self.judul = "Animasi 0: atas->bawah lalu atas->bawah lagi (kolom kanan)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        tinggi = 8
        posisi_list = []
        for p in range(tinggi):
            posisi_list.append(p)
        for p in range(tinggi):
            posisi_list.append(p)

        for posisi in posisi_list:
            for baris_ke in range(tinggi):
                if baris_ke == posisi:
                    print("0")
                else:
                    print(" ")
            print("---")


class Soal41:
    def __init__(self):
        self.nomor = 41
        self.judul = "Animasi 0: atas->bawah lalu bawah->atas (kolom kanan)"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        tinggi = 8
        posisi_list = []
        for p in range(tinggi):
            posisi_list.append(p)
        for p in range(tinggi - 1, -1, -1):
            posisi_list.append(p)

        for posisi in posisi_list:
            for baris_ke in range(tinggi):
                if baris_ke == posisi:
                    print("0")
                else:
                    print(" ")
            print("---")


# ======================================================
# SOAL 42 - 45 : Input beberapa angka (minimal 10)
# ======================================================
class Soal42:
    def __init__(self):
        self.nomor = 42
        self.judul = "Mencari bilangan terbesar dari input"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        angka_list = []
        print("Masukkan minimal 10 angka:")
        for i in range(10):
            nilai = int(input("Angka ke-" + str(i + 1) + ": "))
            angka_list.append(nilai)

        terbesar = angka_list[0]
        for angka in angka_list:
            if angka > terbesar:
                terbesar = angka

        print("Bilangan terbesar:", terbesar)


class Soal43:
    def __init__(self):
        self.nomor = 43
        self.judul = "Mencari bilangan terkecil dari input"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        angka_list = []
        print("Masukkan minimal 10 angka:")
        for i in range(10):
            nilai = int(input("Angka ke-" + str(i + 1) + ": "))
            angka_list.append(nilai)

        terkecil = angka_list[0]
        for angka in angka_list:
            if angka < terkecil:
                terkecil = angka

        print("Bilangan terkecil:", terkecil)


class Soal44:
    def __init__(self):
        self.nomor = 44
        self.judul = "Menghitung jumlah bilangan genap dari input"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        print("Masukkan minimal 10 angka:")
        jumlah_genap = 0
        for i in range(10):
            nilai = int(input("Angka ke-" + str(i + 1) + ": "))
            if nilai % 2 == 0:
                jumlah_genap = jumlah_genap + 1

        print("Jumlah bilangan genap:", jumlah_genap)


class Soal45:
    def __init__(self):
        self.nomor = 45
        self.judul = "Menghitung jumlah bilangan ganjil dari input"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        print("Masukkan minimal 10 angka:")
        jumlah_ganjil = 0
        for i in range(10):
            nilai = int(input("Angka ke-" + str(i + 1) + ": "))
            if nilai % 2 != 0:
                jumlah_ganjil = jumlah_ganjil + 1

        print("Jumlah bilangan ganjil:", jumlah_ganjil)


# ======================================================
# SOAL 46 - 50 : Total bilangan dari n_awal s.d n_akhir
# ======================================================
class Soal46:
    def __init__(self):
        self.nomor = 46
        self.judul = "Total bilangan bulat positif dari n_awal s.d n_akhir"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        awal = int(input("Masukkan n_awal: "))
        akhir = int(input("Masukkan n_akhir: "))

        total = 0
        for angka in range(awal, akhir + 1):
            if angka > 0:
                total = total + angka

        print("Total bilangan bulat positif:", total)


class Soal47:
    def __init__(self):
        self.nomor = 47
        self.judul = "Total bilangan genap dari n_awal s.d n_akhir"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        awal = int(input("Masukkan n_awal: "))
        akhir = int(input("Masukkan n_akhir: "))

        total = 0
        for angka in range(awal, akhir + 1):
            if angka % 2 == 0:
                total = total + angka

        print("Total bilangan genap:", total)


class Soal48:
    def __init__(self):
        self.nomor = 48
        self.judul = "Total bilangan ganjil dari n_awal s.d n_akhir"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        awal = int(input("Masukkan n_awal: "))
        akhir = int(input("Masukkan n_akhir: "))

        total = 0
        for angka in range(awal, akhir + 1):
            if angka % 2 != 0:
                total = total + angka

        print("Total bilangan ganjil:", total)


class Soal49:
    def __init__(self):
        self.nomor = 49
        self.judul = "Menampilkan bilangan Prima dari n_awal s.d n_akhir"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        awal = int(input("Masukkan n_awal: "))
        akhir = int(input("Masukkan n_akhir: "))

        for angka in range(awal, akhir + 1):
            if cek_prima(angka):
                print(angka)


class Soal50:
    def __init__(self):
        self.nomor = 50
        self.judul = "Total jumlah bilangan Prima dari n_awal s.d n_akhir"

    def jalankan(self):
        print("\n=== Soal", self.nomor, ":", self.judul, "===")
        awal = int(input("Masukkan n_awal: "))
        akhir = int(input("Masukkan n_akhir: "))

        jumlah = 0
        for angka in range(awal, akhir + 1):
            if cek_prima(angka):
                jumlah = jumlah + 1

        print("Jumlah total bilangan prima:", jumlah)


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
    daftar.append(Soal21())
    daftar.append(Soal22())
    daftar.append(Soal23())
    daftar.append(Soal24())
    daftar.append(Soal25())
    daftar.append(Soal26())
    daftar.append(Soal27())
    daftar.append(Soal28())
    daftar.append(Soal29())
    daftar.append(Soal30())
    daftar.append(Soal31())
    daftar.append(Soal32())
    daftar.append(Soal33())
    daftar.append(Soal34())
    daftar.append(Soal35())
    daftar.append(Soal36())
    daftar.append(Soal37())
    daftar.append(Soal38())
    daftar.append(Soal39())
    daftar.append(Soal40())
    daftar.append(Soal41())
    daftar.append(Soal42())
    daftar.append(Soal43())
    daftar.append(Soal44())
    daftar.append(Soal45())
    daftar.append(Soal46())
    daftar.append(Soal47())
    daftar.append(Soal48())
    daftar.append(Soal49())
    daftar.append(Soal50())
    return daftar


def main():
    daftar_soal = buat_semua_soal()

    while True:
        print("\n==================================================")
        print("DAFTAR SOAL LOGIKA & ANGKA (1-50)")
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
