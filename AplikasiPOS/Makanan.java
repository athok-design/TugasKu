package aplikasikasir;

public class Makanan extends Produk {

    public Makanan(String kode, String nama, int harga, int stok) {
        super(kode, nama, harga, stok);
    }

    @Override
    public String getKategori() {
        return "Makanan";
    }
}
