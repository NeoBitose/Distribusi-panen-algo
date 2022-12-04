import pandas as pd
import os
import time
import csv

file_panen = "data_panen.csv"
file_distribusi = "data_distribusi.csv"


def petani():

    while True:

        os.system('cls')
        print("\nPilihan Menu Petani")
        print("\n1. Tambah data hasil panen")
        print("2. Tampil data hasil panen")
        print("3. Edit data hasil panen")
        print("4. Hapus data hasil panen")
        print("5. Menu awal")

        while True:

            pilihan = int(input("\nMasukkan pilihan : "))

            if pilihan == 1:
                os.system('cls')
                tambah_hp()
                break
            elif pilihan == 2:
                os.system('cls')
                tampil_hp()
                break
            elif pilihan == 3:
                os.system('cls')
                edit_hp()
                break
            elif pilihan == 4:
                os.system('cls')
                hapus_hp()
                break
            elif pilihan == 5:
                break

        if pilihan == 5:
            os.system('cls')
            Opening()
            break

    return 0


def distributor():

    while True:

        os.system('cls')
        print("\nPilihan Menu Distributor")
        print("\n1. Tambah distribusi hasil panen")
        print("2. Tampil distribusi hasil panen")
        print("3. Edit distribusi hasil panen")
        print("4. Hapus distribusi hasil panen")
        print("5. Menu awal")

        while True:

            pilihan = int(input("\nMasukkan pilihan : "))

            if pilihan == 1:
                tambah_dhp()
                break
            elif pilihan == 2:
                tampil_dhp()
                break
            elif pilihan == 3:
                edit_dhp()
                break
            elif pilihan == 4:
                hapus_dhp()
                break
            elif pilihan == 5:
                break

        if pilihan == 5:
            os.system('cls')
            Opening()
            break

    return 0


def konsumen():

    while True:

        os.system('cls')
        df = pd.read_csv(file_distribusi)
        print(df)

        while True:

            il = input("\nApakah anda ingin melihat data lagi ? [y]/[t] ")
            if il == "y" or il == "Y" or il == "t" or il == "T":
                os.system('cls')
                break

        if il == "t" or il == "T":
            Opening()
            break

    return 0


def Opening():

    os.system('cls')

    print("=================================")
    print("|   Selamat Datang Di Program   |")
    print("|     Distribusi Hasil Panen    |")
    print("=================================\n\n")

    print("Pilihan Pengguna User")
    print("1. Petani")
    print("2. Distributor")
    print("3. Konsumen")
    print("4. Keluar")

    while True:

        pilihan = int(input("\nMasukkan pilihan : "))

        if pilihan == 1:
            petani()
            break
        elif pilihan == 2:
            distributor()
            break
        elif pilihan == 3:
            konsumen()
            break
        elif pilihan == 4:
            break

    return 0


def tambah_hp():

    while True:
        os.system('cls')

        df = pd.read_csv(file_panen)
        print(df)

        petani = input("\nNama petani : ")
        komoditas = input("Jenis Komoditas : ")
        berat = input("Berat hasil panen : ")
        kota = input("Asal kota : ")

        data_panen = [petani, komoditas, berat, kota]

        with open(file_panen, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(data_panen)

        print("\n")
        df = pd.read_csv(file_panen)
        print(df)

        while True:

            il = input("\nApakah anda ingin menambah data lagi ? [y]/[t] ")
            if il == "y" or il == "Y" or il == "t" or il == "T":
                os.system('cls')
                break

        if il == "t" or il == "T":
            break
            petani()

    return 0


def tampil_hp():

    while True:

        os.system('cls')

        df = pd.read_csv(file_panen)
        print(df)

        while True:

            il = input("\nApakah anda ingin melihat data lagi ? [y]/[t] ")
            if il == "y" or il == "Y" or il == "t" or il == "T":
                os.system('cls')
                break

        if il == "t" or il == "T":
            break
            petani()

    return 0


def edit_hp():

    while True:

        os.system('cls')

        df = pd.read_csv(file_panen)
        print(df)

        noindex = input("\nMasukkan nomor data : ")
        petani = input("Nama petani : ")
        komoditas = input("Jenis Komoditas : ")
        berat = input("Berat hasil panen : ")
        kota = input("Asal kota : ")

        df.iloc[int(noindex), 0] = petani
        df.iloc[int(noindex), 1] = komoditas
        df.iloc[int(noindex), 2] = int(berat)
        df.iloc[int(noindex), 3] = kota

        df.to_csv(file_panen, index=False)

        df = pd.read_csv(file_panen)
        print(df)

        while True:

            il = input("\nApakah anda ingin mengubah data lagi ? [y]/[t] ")
            if il == "y" or il == "Y" or il == "t" or il == "T":
                os.system('cls')
                break

        if il == "t" or il == "T":
            break
            petani()

    return 0


def hapus_hp():

    while True:

        os.system('cls')

        df = pd.read_csv(file_panen)
        print(df)

        noindex = int(input("\nMasukkan nomor data yang ingin dihapus : "))

        df.iloc[int(noindex), 2] = 0
        # df.drop([noindex], axis=0, inplace=True)
        # df.index = range(0, len(df))
        df.to_csv(file_panen, index=False)

        df = pd.read_csv(file_panen)
        print(df)

        while True:

            il = input("\nApakah anda ingin menghapus data lagi ? [y]/[t] ")
            if il == "y" or il == "Y" or il == "t" or il == "T":
                os.system('cls')
                break

        if il == "t" or il == "T":
            break
            petani()

    return 0


def tambah_dhp():

    while True:

        os.system('cls')
        print("\nData Distribusi")
        print("==========================\n")
        dfhp = pd.read_csv(file_distribusi)
        print(dfhp)

        print("\nData Hasil Panen")
        print("==========================\n")
        df = pd.read_csv(file_panen)
        print(df)

        dfdhp = pd.read_csv(file_distribusi)

        while True:
            noind = input("\nPilih hasil panen : ")

            listPanen = df.loc[int(noind)]
            dataPanen = list(listPanen)

            print(f"Nama petani : {dataPanen[0]}")
            print(f"Jenis Komoditas : {dataPanen[1]}")
            print(f"Stok Barang : {dataPanen[2]}")
            print(f"Asal kota : {dataPanen[3]}")

            distributor = input("\nNama distributor : ")
            berat = int(input("Berat hasil panen : "))
            stok = dataPanen[2]

            if berat <= stok:
                break
            elif berat > stok:
                print("\nstok panen kurang dari yang ingin dikirim")

        konsumen = input("Nama konsumen : ")
        kota_tujuan = input("kota tujuan : ")
        tanggal = input("tanggal pengiriman : ")

        data_distribusi = [distributor, dataPanen[0], dataPanen[1],
                           berat, konsumen, dataPanen[3], kota_tujuan, tanggal, noind]

        df.iloc[int(noind), 2] = dataPanen[2] - berat
        df.to_csv(file_panen, index=False)

        with open(file_distribusi, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(data_distribusi)

        dfhp = pd.read_csv(file_distribusi)
        print(dfhp)

        while True:

            il = input("\nApakah anda ingin menambah data lagi ? [y]/[t] ")
            if il == "y" or il == "Y" or il == "t" or il == "T":
                os.system('cls')
                break

        if il == "t" or il == "T":
            break
            distributor()

    return 0


def tampil_dhp():

    while True:

        os.system('cls')

        df = pd.read_csv(file_distribusi)
        print(df)

        while True:

            il = input("\nApakah anda ingin menampilkan data lagi ? [y]/[t] ")
            if il == "y" or il == "Y" or il == "t" or il == "T":
                os.system('cls')
                break

        if il == "t" or il == "T":
            break
            distributor()

    return 0


def edit_dhp():

    while True:

        os.system('cls')

        print("\nData Hasil Panen")
        print("==========================\n")
        dfhp = pd.read_csv(file_panen)
        print(dfhp)

        print("\nData Distribusi")
        print("==========================\n")
        df = pd.read_csv(file_distribusi)
        print(df)

        while True:
            noindex = int(input("\nMasukkan nomor data distribusi : "))

            listDist = df.loc[int(noindex)]
            dataDist = list(listDist)

            listPanen = dfhp.loc[int(dataDist[8])]
            dataPanen = list(listPanen)

            print(f"Nama petani : {dataDist[1]}")
            print(f"Jenis Komoditas : {dataDist[2]}")
            print(f"Berat Barang : {dataDist[3]}")
            print(f"Stok barang asal: {dataPanen[2]}")
            print(f"Asal kota : {dataDist[5]}")

            stok = int(dataPanen[2])
            jkirim = int(dataDist[3])

            distributor = input("\nNama distributor : ")
            berat = int(input("Berat hasil panen : "))
            if berat <= jkirim:
                dfhp.iloc[int(dataDist[8]), 2] = stok + (jkrim - berat)
                dfhp.to_csv(file_panen, index=False)
                break
            elif berat > jkirim:
                if berat <= stok + jkirim:
                    dfhp.iloc[int(dataDist[8]), 2] = stok - (berat - jkirim)
                    dfhp.to_csv(file_panen, index=False)
                    break
                else:
                    print("\nstok panen kurang dari yang ingin dikirim\n")

        konsumen = input("Nama konsumen : ")
        kota_tujuan = input("kota tujuan : ")
        tanggal = input("tanggal pengiriman : ")

        df.iloc[noindex, 0] = distributor
        df.iloc[noindex, 1] = dataDist[1]
        df.iloc[noindex, 2] = dataDist[2]
        df.iloc[noindex, 3] = berat
        df.iloc[noindex, 4] = konsumen
        df.iloc[noindex, 5] = dataDist[5]
        df.iloc[noindex, 6] = kota_tujuan
        df.iloc[noindex, 7] = tanggal

        df.to_csv(file_distribusi, index=False)

        df = pd.read_csv(file_distribusi)
        print(f'\n{df}')

        while True:

            il = input("\nApakah anda ingin mengubah data lagi ? [y]/[t] ")
            if il == "y" or il == "Y" or il == "t" or il == "T":
                os.system('cls')
                break

        if il == "t" or il == "T":
            break
            distributor()

    return 0


def hapus_dhp():

    while True:

        os.system('cls')

        df = pd.read_csv(file_distribusi)
        print(df)

        noindex = int(input("\nMasukkan nomor data yang ingin dihapus : "))
        df.drop([noindex], axis=0, inplace=True)

        df.index = range(0, len(df))

        df.to_csv(file_distribusi, index=False)

        df = pd.read_csv(file_distribusi)
        print(df)

        while True:

            il = input("\nApakah anda ingin menghapus data lagi ? [y]/[t] ")
            if il == "y" or il == "Y" or il == "t" or il == "T":
                os.system('cls')
                break

        if il == "t" or il == "T":
            break
            distributor()

    return 0


# ============================
# Main Program

while True:

    Opening()

    while True:

        il = input("\nApakah anda ingin input lagi ? [y]/[t] ")
        if il == "y" or il == "Y" or il == "t" or il == "T":
            os.system('cls')
            break

    if il == "t" or il == "T":
        break
