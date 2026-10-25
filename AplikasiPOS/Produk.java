package aplikasikasir;

public abstract class Produk {

    private String kode;
    private String nama;
    private int harga;
    private int stok;

    public Produk(String kode, String nama, int harga, int stok) {
        this.kode = kode;
        this.nama = nama;
        this.harga = harga;
        this.stok = stok;
    }

    // getter
    public String getKode()  { return kode; }
    public String getNama()  { return nama; }
    public int getHarga()    { return harga; }
    public int getStok()     { return stok; }

    public void kurangiStok(int jumlah) {
        stok = stok - jumlah;
    }

    public abstract String getKategori();
}
