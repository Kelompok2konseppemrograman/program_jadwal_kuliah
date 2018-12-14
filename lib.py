def option():
    print("\n")
    print("1. Menyimpan biodata")
    print("2. Tampilkan semua biodata")
    print("3. Keluar Program")
    pilihan = int(input("Masukkan pilihan anda: "))
    return pilihan

def saving():  
    file = open("database.txt", "a")
    nama = str(input("Masukkan nama: "))
    tgl = str(input("Masukkan tanggal lahir: "))
    asal = str(input("Masukkan asal daerah: "))
    file.write("Nama: {}\n".format(nama))
    file.write("Tanggal lahir: {}\n".format(tgl))
    file.write("Asal Daerah: {}\n".format(asal))
    file.write("\n")
    file.write("\n")
    
def read():
    display = open("database.txt", "r")
    print("\nBiodata yang disimpan adalah sebagai berikut:")
    print(display.read())
           
