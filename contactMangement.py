"Program Manajemen Kontak"

kontak1 = {'Nama' : "Andi", 'HP' : '0812323143', 'EMAIL' : "andi@gmail.com"}
kontak2 = {'Nama' : "Ane", 'HP' : '0812323145', 'EMAIL' : "ane@gmail.com"}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahakan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Maukan menu yang tersedia (1, 2, 3, dan 4): ")

    if pilihan == '1':
        #untuk melihat semua kontak
        if kontak:
            for one, item in enumerate(kontak, start=1):
                print(f'{one}, {item["Nama"]} ({item["HP"]} | {item["EMAIL"]})')
        else:
            print("Kontak Kosong")
    elif pilihan == '2':
        #Menambahkan kontak baru
        nama = input("Masukan nama kontak yang baru: ")
        hp = input("Masukan nomor hp yang baru: ")
        email = input("Masukan email yang baru: ")
        kontakBaru = {'Nama' : nama, 'HP' : hp, 'EMAIL' : email}
        kontak.append(kontakBaru)
        print("Kontak baru berahasil ditambahkan")
        pass
    elif pilihan == '3':
        #manghapus kontak
        if kontak:
            for one, item in enumerate(kontak, start=1):
                print(f'{one}, {item["Nama"]} ({item["HP"]} | {item["EMAIL"]})')
        else:
            print("Kontak Kosong")
            continue
        hapusKontak = int(input("Masukan nomor kontak ke berapa yang ingin dihapus: "))
        del kontak[hapusKontak-1]
        pass
    elif pilihan == '4':
        #Keluar dari kontak
        break
    else:
        print("Anda Memasukan Pilihan yang Salah")