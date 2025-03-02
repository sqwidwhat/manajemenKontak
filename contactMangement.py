# Program Manajemen Kontak

def melihat_kontak():
    if kontak:
        print("\nDaftar Kontak:")
        for idx, item in enumerate(kontak, start=1):
            print(f'{idx}. {item["Nama"]} ({item["HP"]} | {item["EMAIL"]})')
    else:
        print("\nKontak Kosong")
        return 1

def menambah_kontak():
    nama = input("Masukkan nama kontak baru: ")
    hp = input("Masukkan nomor HP: ")
    email = input("Masukkan email: ")
    kontak.append({'Nama': nama, 'HP': hp, 'EMAIL': email})
    print("\nKontak baru berhasil ditambahkan!")

def menghapus_kontak():
    if melihat_kontak() == 1:
        return
    try:
        hapus_kontak = int(input("Masukkan nomor kontak yang ingin dihapus: "))
        if 1 <= hapus_kontak <= len(kontak):
            del kontak[hapus_kontak - 1]
            print("\nKontak berhasil dihapus!")
        else:
            print("\nNomor kontak tidak valid!")
    except ValueError:
        print("\nMasukkan angka yang valid!")

# Inisialisasi daftar kontak
kontak = [
    {'Nama': "Andi", 'HP': '0812323143', 'EMAIL': "andi@gmail.com"},
    {'Nama': "Ane", 'HP': '0812323145', 'EMAIL': "ane@gmail.com"}
]

# Menu utama
while True:
    print("\nMenu Kontak")
    print("1. Lihat Semua Kontak")
    print("2. Tambah Kontak Baru")
    print("3. Hapus Kontak")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        melihat_kontak()
    elif pilihan == '2':
        menambah_kontak()
    elif pilihan == '3':
        menghapus_kontak()
    elif pilihan == '4':
        print("\nKeluar dari program. Terima kasih!")
        break
    else:
        print("\nPilihan tidak valid, coba lagi!")