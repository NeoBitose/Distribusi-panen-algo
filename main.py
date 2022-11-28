import pandas as pd, os, time, csv

file_panen = "data_panen.csv"
file_distribusi = "data_distribusi.csv"

def petani():

    while True :

        os.system ('cls')
        print("\nPilihan Menu Petani")
        print("1. Tambah data hasil panen")
        print("2. Tampil data hasil panen")
        print("3. Edit data hasil panen")
        print("4. Hapus data hasil panen")
        print("5. Menu awal")

        while True:

            pilihan = int(input("\nMasukkan pilihan : "))

            if pilihan == 1:
                os.system ('cls')
                tambah_hp()
                break
            elif pilihan == 2:
                os.system ('cls')
                tampil_hp()   
                break       
            elif pilihan == 3:
                os.system ('cls')
                edit_hp()     
                break      
            elif pilihan == 4:
                os.system ('cls')
                hapus_hp()
                break
            elif pilihan == 5:
                break

        if pilihan == 5:
            os.system ('cls')
            Opening()
            break
            

    return 0

def distributor():

    while True:

        os.system('cls')
        print("\nPilihan Menu Distributor")
        print("1. Tambah distribusi hasil panen")
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
            os.system ('cls')
            Opening()
            break

    return 0

def konsumen():
    
    while True:

        os.system('cls')
        df = pd.read_csv(os.path.join(os.getcwd(), file_distribusi))
        print(df)

        while True :

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
    print("2. Distribusi")
    print("3. Konsumen")
    print("4. Keluar")

    while True :

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

        df = pd.read_csv(os.path.join(os.getcwd(), file_panen))
        print(df)

        petani = input("\nNama petani : ")
        komoditas = input("Jenis Komoditas : ")
        berat = input("Berat hasil panen : ")
        kota = input("Asal kota : ")

        data_panen = [petani,komoditas,berat,kota]

        with open(file_panen,'a',newline='') as file :
            writer = csv.writer(file, delimiter=",")
            writer.writerow(data_panen)
        
        print("\n")
        df = pd.read_csv(os.path.join(os.getcwd(), file_panen))
        print(df)

        while True :

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

        df = pd.read_csv(os.path.join(os.getcwd(), file_panen))
        print(df)

        while True :

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

        df = pd.read_csv(file_panen)
        print(df)

        noindex = input("\nMasukkan nomor data : ")

        petani = input("Nama petani : ")
        komoditas = input("Jenis Komoditas : ")
        berat = input("Berat hasil panen : ")
        kota = input("Asal kota : ")

        df.iloc[int(noindex), 0] = petani
        df.iloc[int(noindex), 1] = komoditas
        df.iloc[int(noindex), 2] = berat
        df.iloc[int(noindex), 3] = kota

        df.to_csv(file_panen, index=False)

        df = pd.read_csv(file_panen)
        print(df)

        while True :

            il = input("\nApakah anda ingin mengubah data lagi ? [y]/[t] ")
            if il == "y" or il == "Y" or il == "t" or il == "T":
                os.system('cls')
                break
        
        if il == "t" or il == "T":
            break
            petani()

    return 0
    
def hapus_hp():

    while True :

        df = pd.read_csv(file_panen)
        print(df)

        noindex = int(input("\nMasukkan nomor data yang ingin dihapus : "))
        df.drop([noindex], axis=0, inplace=True)
        df.index = range(0, len(df))
        df.to_csv(file_panen, index=False)

        df = pd.read_csv(file_panen)
        print(df)

        while True :

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

        dfhp = pd.read_csv(os.path.join(os.getcwd(), file_distribusi))
        print(dfhp)
        df = pd.read_csv(os.path.join(os.getcwd(), file_panen))
        print(f'\ndf')

        dfdhp = pd.read_csv(os.path.join(os.getcwd(), file_distribusi))

        distributor = input("\nNama distributor : ")
        petani = input("Nama petani : ")
        komoditas = input("Jenis Komoditas : ")
        berat = input("Berat hasil panen : ")
        konsumen = input("Nama konsumen : ")
        kota_asal = input("Asal kota : ")
        kota_tujuan = input("kota tujuan : ")
        tanggal = input("tanggal pengiriman : ")

        data_distribusi = [distributor,petani,komoditas,berat,konsumen,kota_asal,kota_tujuan,tanggal]

        with open(file_distribusi,'a',newline='') as file :
            writer = csv.writer(file, delimiter=",")
            writer.writerow(data_distribusi)
        
        dfhp = pd.read_csv(os.path.join(os.getcwd(), file_distributor))
        print(dfhp)

        while True :

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

        while True :

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

        df = pd.read_csv(file_distribusi)
        print(df)

        noindex = int(input("\nMasukkan nomor data : "))

        distributor = input("Nama distributor : ")
        petani = input("Nama petani : ")
        komoditas = input("Jenis Komoditas : ")
        berat = input("Berat hasil panen : ")
        konsumen = input("Nama konsumen : ")
        kota_asal = input("Asal kota : ")
        kota_tujuan = input("kota tujuan : ")
        tanggal = input("tanggal pengiriman : ")

        df.iloc[noindex, 0] = distributor
        df.iloc[noindex, 1] = petani
        df.iloc[noindex, 2] = komoditas
        df.iloc[noindex, 3] = berat
        df.iloc[noindex, 4] = konsumen
        df.iloc[noindex, 5] = kota_asal
        df.iloc[noindex, 6] = kota_tujuan
        df.iloc[noindex, 7] = tanggal

        df.to_csv(file_distribusi, index=False)

        df = pd.read_csv(file_distribusi)
        print(df)

        while True :

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

        df = pd.read_csv(file_distribusi)
        print(df)

        noindex = int(input("\nMasukkan nomor data yang ingin dihapus : "))
        df.drop([noindex], axis=0, inplace=True)
        df.index = range(0, len(df))
        df.to_csv(file_distribusi, index=False)

        df = pd.read_csv(file_distribusi)
        print(df)

        while True :

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

while True :

    Opening()

    while True :

        il = input("\nApakah anda ingin input lagi ? [y]/[t] ")
        if il == "y" or il == "Y" or il == "t" or il == "T":
            os.system('cls')
            break
    
    if il == "t" or il == "T":
        break



