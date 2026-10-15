# STRYNG - Guitar Store Management System
# Posttest 5: CRUD menggunakan nested list
# Tanpa def dan tanpa try-except.
# Data tersimpan sementara selama program berjalan.

import os

akun = [["kibo", "kibo127", "Admin"]]
# Format gitar: [ID, Nama, Merek, Jenis, Harga, Stok]
daftar_gitar = [
    ["G001", "Stratocaster", "Squier", "Elektrik", 2500000, 5],
    ["G002", "Dreadnought", "Yamaha", "Akustik", 1800000, 3],
    ["G003", "RG Series", "Ibanez", "Elektrik", 4200000, 2]
]

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 42)
    print("       STRYNG - GUITAR STORE")
    print("=" * 42)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan_awal = input("Pilih menu: ").strip()

    if pilihan_awal == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("========== LOGIN ==========")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        indeks_akun = -1
        for i in range(len(akun)):
            if akun[i][0] == username and akun[i][1] == password:
                indeks_akun = i
                break

        if indeks_akun == -1:
            print("Login gagal. Username atau password salah.")
            input("Tekan Enter untuk kembali...")
        else:
            role = akun[indeks_akun][2]
            print("Login berhasil. Role:", role)
            input("Tekan Enter untuk masuk ke menu...")
            sedang_login = True

            while sedang_login:
                os.system("cls" if os.name == "nt" else "clear")
                print("=" * 42)
                print("STRYNG | Login sebagai:", username, "-", role)
                print("=" * 42)

                if role == "Admin":
                    print("1. Tambah data gitar")
                    print("2. Lihat data gitar")
                    print("3. Ubah data gitar")
                    print("4. Hapus data gitar")
                    print("5. Cari data gitar")
                    print("6. Logout")
                    pilihan = input("Pilih menu: ").strip()

                    if pilihan == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("====== TAMBAH DATA GITAR ======")
                        id_gitar = input("ID gitar: ").strip().upper()
                        id_sudah_ada = False
                        for gitar in daftar_gitar:
                            if gitar[0] == id_gitar:
                                id_sudah_ada = True
                        if id_gitar == "":
                            print("ID tidak boleh kosong.")
                        elif id_sudah_ada:
                            print("ID sudah digunakan.")
                        else:
                            nama = input("Nama gitar: ").strip()
                            merek = input("Merek: ").strip()
                            jenis = input("Jenis (Elektrik/Akustik): ").strip().capitalize()
                            harga_input = input("Harga (angka): ").strip()
                            stok_input = input("Stok (angka): ").strip()
                            if nama == "" or merek == "":
                                print("Nama dan merek tidak boleh kosong.")
                            elif jenis not in ["Elektrik", "Akustik"]:
                                print("Jenis harus Elektrik atau Akustik.")
                            elif not harga_input.isdigit() or not stok_input.isdigit():
                                print("Harga dan stok harus berupa bilangan bulat nonnegatif.")
                            else:
                                daftar_gitar.append([id_gitar, nama, merek, jenis, int(harga_input), int(stok_input)])
                                print("Data gitar berhasil ditambahkan.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "2":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("====== DAFTAR DATA GITAR ======")
                        if len(daftar_gitar) == 0:
                            print("Belum ada data gitar.")
                        else:
                            for gitar in daftar_gitar:
                                print("-" * 36)
                                print("ID    :", gitar[0])
                                print("Nama  :", gitar[1])
                                print("Merek :", gitar[2])
                                print("Jenis :", gitar[3])
                                print("Harga : Rp", format(gitar[4], ",").replace(",", "."))
                                print("Stok  :", gitar[5])
                        input("\nTekan Enter untuk kembali...")

                    elif pilihan == "3":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("====== UBAH DATA GITAR ======")
                        id_cari = input("Masukkan ID gitar yang ingin diubah: ").strip().upper()
                        indeks_gitar = -1
                        for i in range(len(daftar_gitar)):
                            if daftar_gitar[i][0] == id_cari:
                                indeks_gitar = i
                                break
                        if indeks_gitar == -1:
                            print("ID gitar tidak ditemukan.")
                        else:
                            gitar = daftar_gitar[indeks_gitar]
                            print("Kosongkan input jika tidak ingin mengubah nilai.")
                            nama_baru = input("Nama baru [" + gitar[1] + "]: ").strip()
                            merek_baru = input("Merek baru [" + gitar[2] + "]: ").strip()
                            jenis_baru = input("Jenis baru [" + gitar[3] + "]: ").strip().capitalize()
                            harga_baru = input("Harga baru [" + str(gitar[4]) + "]: ").strip()
                            stok_baru = input("Stok baru [" + str(gitar[5]) + "]: ").strip()
                            if nama_baru != "":
                                gitar[1] = nama_baru
                            if merek_baru != "":
                                gitar[2] = merek_baru
                            if jenis_baru != "":
                                if jenis_baru in ["Elektrik", "Akustik"]:
                                    gitar[3] = jenis_baru
                                else:
                                    print("Jenis tidak valid; data lama dipertahankan.")
                            if harga_baru != "":
                                if harga_baru.isdigit():
                                    gitar[4] = int(harga_baru)
                                else:
                                    print("Harga tidak valid; data lama dipertahankan.")
                            if stok_baru != "":
                                if stok_baru.isdigit():
                                    gitar[5] = int(stok_baru)
                                else:
                                    print("Stok tidak valid; data lama dipertahankan.")
                            print("Proses ubah data selesai.")
                        input("Tekan Enter untuk kembali...")

                    elif pilihan == "4":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("====== HAPUS DATA GITAR ======")
                        id_hapus = input("Masukkan ID gitar yang ingin dihapus: ").strip().upper()
                        indeks_hapus = -1
                        for i in range(len(daftar_gitar)):
                            if daftar_gitar[i][0] == id_hapus:
                                indeks_hapus = i
                                break
                        if indeks_hapus == -1:
                            print("ID gitar tidak ditemukan.")
                        else:
                            konfirmasi = input("Yakin menghapus " + daftar_gitar[indeks_hapus][1] + "? (y/n): ").strip().lower()
                            if konfirmasi == "y":
                                daftar_gitar.pop(indeks_hapus)
                                print("Data gitar berhasil dihapus.")
                            else:
                                print("Penghapusan dibatalkan.")
                        input("Tekan Enter untuk kembali...")

                    elif pilihan == "5":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("====== CARI DATA GITAR ======")
                        kata_kunci = input("Masukkan ID, nama, merek, atau jenis: ").strip().lower()
                        ditemukan = False
                        for gitar in daftar_gitar:
                            if (kata_kunci in gitar[0].lower() or kata_kunci in gitar[1].lower()
                                or kata_kunci in gitar[2].lower() or kata_kunci in gitar[3].lower()):
                                print("-" * 36)
                                print("ID    :", gitar[0])
                                print("Nama  :", gitar[1])
                                print("Merek :", gitar[2])
                                print("Jenis :", gitar[3])
                                print("Harga : Rp", format(gitar[4], ",").replace(",", "."))
                                print("Stok  :", gitar[5])
                                ditemukan = True
                        if not ditemukan:
                            print("Data gitar tidak ditemukan.")
                        input("Tekan Enter untuk kembali...")

                    elif pilihan == "6":
                        print("Logout berhasil.")
                        input("Tekan Enter untuk kembali ke menu utama...")
                        sedang_login = False
                    else:
                        print("Pilihan tidak valid.")
                        input("Tekan Enter untuk mencoba lagi...")

                else:
                    print("1. Lihat daftar gitar")
                    print("2. Cari data gitar")
                    print("3. Logout")
                    pilihan_user = input("Pilih menu: ").strip()
                    if pilihan_user == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("====== DAFTAR DATA GITAR ======")
                        if len(daftar_gitar) == 0:
                            print("Belum ada data gitar.")
                        else:
                            for gitar in daftar_gitar:
                                print("-" * 36)
                                print("ID    :", gitar[0])
                                print("Nama  :", gitar[1])
                                print("Merek :", gitar[2])
                                print("Jenis :", gitar[3])
                                print("Harga : Rp", format(gitar[4], ",").replace(",", "."))
                                print("Stok  :", gitar[5])
                        input("\nTekan Enter untuk kembali...")
                    elif pilihan_user == "2":
                        os.system("cls" if os.name == "nt" else "clear")
                        kata_kunci = input("Masukkan ID, nama, merek, atau jenis: ").strip().lower()
                        ditemukan = False
                        for gitar in daftar_gitar:
                            if (kata_kunci in gitar[0].lower() or kata_kunci in gitar[1].lower()
                                or kata_kunci in gitar[2].lower() or kata_kunci in gitar[3].lower()):
                                print(gitar)
                                ditemukan = True
                        if not ditemukan:
                            print("Data gitar tidak ditemukan.")
                        input("Tekan Enter untuk kembali...")
                    elif pilihan_user == "3":
                        print("Logout berhasil.")
                        input("Tekan Enter untuk kembali ke menu utama...")
                        sedang_login = False
                    else:
                        print("Pilihan tidak valid.")
                        input("Tekan Enter untuk mencoba lagi...")

    elif pilihan_awal == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("========== REGISTER ==========")
        username_baru = input("Buat username: ").strip()
        password_baru = input("Buat password (minimal 4 karakter): ").strip()
        username_terpakai = False
        for data_akun in akun:
            if data_akun[0].lower() == username_baru.lower():
                username_terpakai = True
                break
        if username_baru == "" or password_baru == "":
            print("Username dan password tidak boleh kosong.")
        elif username_terpakai:
            print("Username sudah digunakan.")
        elif len(password_baru) < 4:
            print("Password minimal 4 karakter.")
        else:
            akun.append([username_baru, password_baru, "Pengguna"])
            print("Register berhasil! Role akun baru: Pengguna.")
            print("Silakan login menggunakan akun yang baru dibuat.")
        input("Tekan Enter untuk kembali ke menu utama...")

    elif pilihan_awal == "3":
        print("Terima kasih telah menggunakan STRYNG!")
        break
    else:
        print("Pilihan tidak valid. Masukkan 1, 2, atau 3.")
        input("Tekan Enter untuk mencoba lagi...")
