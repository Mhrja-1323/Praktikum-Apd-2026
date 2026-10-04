# PROGRAM REKAPITULASI TITIK API
# BPBD dan Manggala Agni

# =========================
# FORM LOGIN
# =========================

username_benar = "kiboo"
password_benar = "127"

while True:
    print("===== FORM LOGIN =====")
    username = input("Username : ")
    password = input("Password : ")

    if username == username_benar and password == password_benar:
        print("\nLogin berhasil!")
        break
    else:
        print("\nUsername atau Password salah!")
        print("Silakan coba lagi.\n")


# =========================
# VARIABEL TOTAL LAHAN
# =========================

total_kalimantan_gambut = 0
total_kalimantan_mineral = 0
total_sumatera_gambut = 0
total_sumatera_mineral = 0


# =========================
# INPUT DATA TITIK API
# =========================

while True:

    print("\n===== INPUT DATA TITIK API =====")

    pulau = input("Masukkan pulau (KALIMANTAN/SUMATERA): ").upper()

    if pulau == "KALIMANTAN":

        lahan = input("Masukkan jenis lahan (GAMBUT/MINERAL): ").upper()

        if lahan == "GAMBUT":
            kategori = "Kalimantan-Gambut"

            hotspot = int(input("Jumlah Titik Api (Hotspot): "))
            luas = hotspot * 5

            total_kalimantan_gambut += luas

            print("Kategori :", kategori)
            print("Luas lahan terbakar :", luas, "Hektare")

        elif lahan == "MINERAL":
            kategori = "Kalimantan-Mineral"

            hotspot = int(input("Jumlah Titik Api (Hotspot): "))
            luas = hotspot * 5

            total_kalimantan_mineral += luas

            print("Kategori :", kategori)
            print("Luas lahan terbakar :", luas, "Hektare")

        else:
            print("Jenis lahan tidak valid!")
            continue

    elif pulau == "SUMATERA":

        lahan = input("Masukkan jenis lahan (GAMBUT/MINERAL): ").upper()

        if lahan == "GAMBUT":
            kategori = "Sumatera-Gambut"

            hotspot = int(input("Jumlah Titik Api (Hotspot): "))
            luas = hotspot * 5

            total_sumatera_gambut += luas

            print("Kategori :", kategori)
            print("Luas lahan terbakar :", luas, "Hektare")

        elif lahan == "MINERAL":
            kategori = "Sumatera-Mineral"

            hotspot = int(input("Jumlah Titik Api (Hotspot): "))
            luas = hotspot * 5

            total_sumatera_mineral += luas

            print("Kategori :", kategori)
            print("Luas lahan terbakar :", luas, "Hektare")

        else:
            print("Jenis lahan tidak valid!")
            continue

    else:
        print("Pulau tidak valid!")
        continue

    # =========================
    # PENGULANGAN INPUT
    # =========================

    lagi = input("\nApakah anda masih mau input data titik api lagi? (Y/T): ").upper()

    if lagi == "T":
        break


# =========================
# RINGKASAN AKHIR
# =========================

print("\n===================================")
print("       RINGKASAN DATA TITIK API")
print("===================================")

print("Kalimantan-Gambut  :", total_kalimantan_gambut, "Hektare")
print("Kalimantan-Mineral :", total_kalimantan_mineral, "Hektare")
print("Sumatera-Gambut    :", total_sumatera_gambut, "Hektare")
print("Sumatera-Mineral   :", total_sumatera_mineral, "Hektare")

print("===================================")
print("Program selesai.")