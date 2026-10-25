package aplikasikasir;

public class Minuman extends Produk {

    public Minuman(String kode, String nama, int harga, int stok) {
        super(kode, nama, harga, stok);
    }

    @Override
    public String getKategori() {
        return "Minuman";
    }
}
