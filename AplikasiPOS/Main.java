package aplikasikasir;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    static Scanner input = new Scanner(System.in);
    static ArrayList<Produk> daftarProduk = new ArrayList<>();
    static int totalPendapatan = 0;

    public static void main(String[] args) {

        // data awal
        daftarProduk.add(new Makanan("P01", "Indomie Goreng", 3500, 50));
        daftarProduk.add(new Minuman("P02", "Aqua 600ml", 4000, 40));
        daftarProduk.add(new Makanan("P03", "Roti Tawar", 15000, 10));
        daftarProduk.add(new Minuman("P04", "Teh Botol", 5000, 30));

        int pilihan;
        do {
            System.out.println("\n===== APLIKASI KASIR =====");
            System.out.println("1. Lihat Produk");
            System.out.println("2. Transaksi");
            System.out.println("3. Laporan");
            System.out.println("0. Keluar");
            System.out.print("Pilih: ");
            pilihan = input.nextInt();

            if (pilihan == 1) {
                lihatProduk();
            } else if (pilihan == 2) {
                transaksi();
            } else if (pilihan == 3) {
                System.out.println("Total pendapatan: Rp" + totalPendapatan);
            }
        } while (pilihan != 0);

        System.out.println("Program selesai.");
    }

    // menampilkan produk
    static void lihatProduk() {
        System.out.println("\nKode | Nama            | Kategori | Harga  | Stok");
        for (Produk p : daftarProduk) {
            System.out.printf("%-4s | %-15s | %-8s | %-6d | %d%n",
                    p.getKode(), p.getNama(), p.getKategori(), p.getHarga(), p.getStok());
        }
    }

    // proses transaksi
    static void transaksi() {
        int total = 0;
        String lagi;

        do {
            lihatProduk();
            System.out.print("Kode produk : ");
            String kode = input.next();
            System.out.print("Jumlah      : ");
            int jumlah = input.nextInt();

            Produk p = cariProduk(kode);
            if (p == null) {
                System.out.println("Produk tidak ditemukan!");
            } else if (jumlah <= 0) {
                System.out.println("Jumlah tidak valid!");
            } else if (jumlah > p.getStok()) {
                System.out.println("Stok tidak cukup!");
            } else {
                p.kurangiStok(jumlah);
                total = total + p.getHarga() * jumlah;
                System.out.println(p.getNama() + " x" + jumlah + " ditambahkan.");
            }

            System.out.print("Beli lagi? (y/n): ");
            lagi = input.next();
        } while (lagi.equalsIgnoreCase("y"));

        System.out.println("\nTotal bayar : Rp" + total);
        System.out.print("Uang        : Rp");
        int uang = input.nextInt();

        if (uang < total) {
            System.out.println("Uang kurang! Transaksi dibatalkan.");
        } else {
            System.out.println("Kembalian   : Rp" + (uang - total));
            totalPendapatan = totalPendapatan + total;
        }
    }

    // cari produk by kode
    static Produk cariProduk(String kode) {
        for (Produk p : daftarProduk) {
            if (p.getKode().equalsIgnoreCase(kode)) {
                return p;
            }
        }
        return null;
    }
}
