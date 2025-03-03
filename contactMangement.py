kontak = [
    {'Nama': "Andi", 'HP': '0812323143', 'EMAIL': "andi@gmail.com"},
    {'Nama': "Ane", 'HP': '0812323145', 'EMAIL': "ane@gmail.com"}
]

def meilihatKontak():
    if kontak:
        for idx, i in enumerate(kontak, start=1):
            print(f'{idx}. {i["Nama"]}. {i["HP"]}. {i["EMAIL"]}')
    else:
        print("Kontak kosong")
        return 1

def menambahKontak():
    nama = input("Masukan nama kontak baru : ")
    hp = input("Masukan nomor hp: ")
    email = input("Masukan email: ")
    kontak.append({'Nama' : nama, 'HP' :hp, 'EMAIL' : email})
    print("\nKontak berhasil ditambahkan")

def menghapusKontak():
    if meilihatKontak() == 1:
        return
    try:
        hapusKontak = int(input("Masukan nomor kontak yang ingin anda hapus: "))
        if 1 <= hapusKontak <= len(kontak):#Fungsi len() dalam Python digunakan untuk menghitung jumlah elemen dalam suatu objek seperti list, string, tuple, atau dictionary.
            del kontak[hapusKontak - 1]
            print("\nKontak berhasil dihapus")
        else:
            print("\nNomor kontak tidak valid!")
    except ValueError:
        print("\nMasukan angka yang valid")



def main():
    while True:
        print("")
        print("1. Melihat Kontak")
        print("2. Menambah Kontak")
        print("3. Menghapus Kontak")
        print("4. Keluar")
        pilihan = input("Masukan Pilihan: ")

        if pilihan == '1':
            meilihatKontak()
        elif pilihan == '2':
            menambahKontak()
        elif pilihan == '3':
            menghapusKontak()
        elif pilihan == '4':
            print("\nKeluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan yang anda masukan tidak sesuai dengan menu")

if __name__ == "__main__":
    main()