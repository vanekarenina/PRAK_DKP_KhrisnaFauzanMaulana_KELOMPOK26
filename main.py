
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
