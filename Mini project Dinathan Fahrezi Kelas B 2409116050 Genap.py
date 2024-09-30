
import getpass

print("===================Program Menghitung Diskon===================")
print("Registrasi")
nama_1 = input("Masukkan nama baru anda: ")
nim_1 =input("Masukkan NIM sebagai password anda: ")
while True :
    print("silahkan login")
    nama = input("Nama: ")
    nim = getpass.getpass("NIM: ")
    
    if nama_1==nama and nim_1==nim:
        print("Anda berhasil login")
        break
    else :
        print("Nama atau password anda salah ")
        pass

while True:
    harga_barang = int(input("Harga Barang:RP.")) 
    jumlah_barang = int(input("Jumlah Barang: "))
    total_harga = jumlah_barang * harga_barang 
    if total_harga > 250000 :
        diskon = 0.25 * total_harga 
        harga_setelah_diskon = total_harga - diskon
        print(f"RP.{harga_setelah_diskon}")
        pass
    else :
        print(f"RP.{total_harga}")

        
    if input("Apakah anda ingin melanjutkan perhitungan? (iya/tidak): ") !="iya":
        print("Terima kasih, anda berhasil keluar dari program perhitungan")
        break