import method


mtd = method.mtd_tiket
mtd.identitas(26)


print(" ________________________________________________________")
print("\n \t    SELAMAT DATANG DI TEKKOM AIRWAYS")
print("_________________________________________________________")
print("         RUTE\t\t   Waktu\t\tHarga")
print("1. SEMARANG-BALI\t 07.05 WIB \t     Rp 700.000")
print("2. SEMARANG-SURABAYA\t 12.35 WIB\t     Rp 600.000")
print("3. SEMARANG-JAKARTA\t 16.55 WIB \t     Rp 500.000")
print("_________________________________________________________")


def pemesanan(): 
    jmlh = int(input("Jumlah Penumpang : ")) 
    print ("Masukan nama Penumpang") 
    for i in range (int(jmlh)): 
        i += 1 
        n = input("Penumpang ke-{}: ".format(i)) 
    tot=jmlh*harga 
    print("\nTotal Harga Rp",tot) 
    print("__________________________________") 
    email=input("Masukkan Alamat Email Anda: ") 
    print("----------------------------------") 
    print("\nTerima Kasih Telah Memilih Terbang Bersama Kami") 
    print("\nE-Ticket Anda Akan Dikirimkan Melalui Email", email) 
    print("\n<<<Tetap Patuhi Protokol Kesehatan>>>") 
    print("-----------------------------------------------") 
rute= int(input("\nMasukan Pilihan Rute : "))
if (rute == 1):
    harga = 700000
    pemesanan()
elif (rute == 2):
    harga = 600000
    pemesanan()
elif (rute == 3):
    harga = 500000
    pemesanan()
else:
    print("\n**Pilihan Rute Belum Tersedia**")
