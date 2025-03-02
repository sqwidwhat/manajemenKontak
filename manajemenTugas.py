# List untuk menyimpan daftar tugas
daftar_tugas = []

def melihat_tugas():
    if daftar_tugas:
        print("\nDaftar Tugas:")
        for idx, item in enumerate(daftar_tugas, start=1):
            print(f"{idx}. {item}")
    else:
        print("\nTidak ada tugas.")
        return 1

def menambah_tugas():
    tugas = input("Masukkan nama tugas baru: ").strip()
    if tugas:
        daftar_tugas.append(tugas)
        print("\nTugas baru berhasil ditambahkan!")
    else:
        print("\nTugas tidak boleh kosong!")

def menghapus_tugas():
    if melihat_tugas() == 1:
        return
    try:
        hapus_tugas = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if 1 <= hapus_tugas <= len(daftar_tugas):
            del daftar_tugas[hapus_tugas - 1]
            print("\nTugas berhasil dihapus!")
        else:
            print("\nNomor tugas tidak valid!")
    except ValueError:
        print("\nMasukkan angka yang valid!")

while True:
    print("\nMenu Tugas")
    print("1. Lihat Semua Tugas")
    print("2. Tambah Tugas Baru")
    print("3. Hapus Tugas")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        melihat_tugas()
    elif pilihan == '2':
        menambah_tugas()
    elif pilihan == '3':
        menghapus_tugas()
    elif pilihan == '4':
        print("\nKeluar dari program. Terima kasih!")
        break
    else:
        print("\nPilihan tidak valid, coba lagi!")
