class Kontak:
    def __init__(self):
        self.kontak = []

    def meilihatKontak(self):
        if self.kontak:
            for idx, i in enumerate(self.kontak, start=1):
                print(f'{idx}. {i["Nama"]}. {i["HP"]}. {i["EMAIL"]}')
        else:
            print("Kontak kosong")
            return 1

    def menambahKontak(self):
        nama = input("Masukan nama kontak baru : ")
        hp = input("Masukan nomor hp: ")
        email = input("Masukan email: ")
        self.kontak.append({'Nama' : nama, 'HP' :hp, 'EMAIL' : email})
        print("\nKontak berhasil ditambahkan")

    def menghapusKontak(self):
        if self.meilihatKontak() == 1:
            return
        try:
            hapusKontak = int(input("Masukan nomor kontak yang ingin anda hapus: "))
            if 1 <= hapusKontak <= len(self.kontak):#Fungsi len() dalam Python digunakan untuk menghitung jumlah elemen dalam suatu objek seperti list, string, tuple, atau dictionary.
                del self.kontak[hapusKontak - 1]
                print("\nKontak berhasil dihapus")
            else:
                print("\nNomor kontak tidak valid!")
        except ValueError:
            print("\nMasukan angka yang valid")

def main():
    kontak = Kontak()
    while True:
        print("")
        print("1. Melihat Kontak")
        print("2. Menambah Kontak")
        print("3. Menghapus Kontak")
        print("4. Keluar")
        pilihan = input("Masukan Pilihan: ")

        if pilihan == '1':
            kontak.meilihatKontak()
        elif pilihan == '2':
            kontak.menambahKontak()
        elif pilihan == '3':
            kontak.menghapusKontak()
        elif pilihan == '4':
            print("\nKeluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan yang anda masukan tidak sesuai dengan menu")

if __name__ == "__main__":
    main()