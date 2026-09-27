# Program Pembayaran Langganan Aplikasi ANGKASA

# Data login
nama_benar = "kibo"
nim_belakang = "27"

# Biaya langganan
biaya_langganan = 1500000

print("======================================")
print("       APLIKASI STREAMING ANGKASA")
print("======================================")

# Validasi login
nama = input("Masukkan Nama : ")
nim = input("Masukkan 2 digit belakang NIM : ")

if nama == nama_benar and nim == nim_belakang:
    print("\nLogin berhasil!")
    print("Selamat datang di ANGKASA,", nama)

    # Menu pembayaran
    print("\n======================================")
    print("         PILIH PAKET LANGGANAN")
    print("======================================")
    print("1. Paket Orbit")
    print("2. Paket Nebula")
    print("3. Paket Galaxy")
    print("4. Paket Supernova")
    print("======================================")

    pilihan = input("Pilih paket (1-4): ")

    if pilihan == "1":
        paket = "Orbit"
        admin = 0.01
        fitur = "Akses dasar ke lagu-lagu populer"

    elif pilihan == "2":
        paket = "Nebula"
        admin = 0.03
        fitur = "Akses lagu premium dan playlist kustom"

    elif pilihan == "3":
        paket = "Galaxy"
        admin = 0.05
        fitur = "Akses lagu premium, playlist kustom, dan mode offline"

    elif pilihan == "4":
        paket = "Supernova"
        admin = 0.07
        fitur = "Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis"

    else:
        print("\nPilihan paket tidak valid.")
        exit()

    # Perhitungan biaya administrasi
    biaya_admin = biaya_langganan * admin

    # Perhitungan total pembayaran
    total_bayar = biaya_langganan + biaya_admin

    # Menampilkan hasil
    print("\n======================================")
    print("           DETAIL PEMBAYARAN")
    print("======================================")
    print("Nama              :", nama)
    print("Paket             :", paket)
    print("Biaya Langganan   : Rp", format(biaya_langganan, ",.0f"))
    print("Biaya Administrasi: Rp", format(biaya_admin, ",.0f"))
    print("Total Bayar       : Rp", format(total_bayar, ",.0f"))
    print("--------------------------------------")
    print("Fitur/Keuntungan  :", fitur)
    print("======================================")
    print("Terima kasih telah berlangganan ANGKASA!")

else:
    print("\nLogin gagal!")
    print("Nama atau 2 digit belakang NIM tidak sesuai.")
    print("Program dihentikan.")