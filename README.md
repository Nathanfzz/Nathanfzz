excc## Mini Project
## Nama:Dinathan Fahrezi
## NIM:2409116050

Flowchart:![flowchart mini project drawio](https://github.com/user-attachments/assets/e03c4568-d62b-43f4-9312-cc0c59c5c51d)
Terminal:![Screenshot 2024-09-30 222411](https://github.com/user-attachments/assets/b311bd98-95f7-464e-8b4f-8f81320a00d1)

Penjelasan:

Baris 1 =  getpass digunakan untuk menyembunyikan password nim.
Baris 4 - 18 = register yang digunakan untuk login, nama dan password harus sama dengan yang diketik di register, while true digunakan untuk looping, pass digunakan untuk mengulang didalam loop, break digunakan untuk keluar dari loop atau lanjut ke loop berikutnya.
baris 20 - 35 = memasukan harga dan jumlah barang, jika diatas 250000 mendapat diskon 25% jika dibawah tidak mendapat diskon, jika ingin lanjut menggunakan program ketik iya maka program akan loop, jika ingin berhenti ketik tidak maka program  akan berhenti, != artinya tidak sama dengan artinya diprogram ini jika inputan tidak sama dengan "iya" maka program akan break.
1. Import dan persiapan
   import getpass
Modul getpass diimpor untuk meminta kata sandi pengguna dengan aman tanpa menampilkannya di layar.

2.Registrasi
  print("===================Program Menghitung Diskon===================")
  print("Registrasi")
  nama_1 = input("Masukkan nama baru anda: ")
  nim_1 = input("Masukkan NIM sebagai password anda: ")
Program dimulai dengan pesan selamat datang dan meminta pengguna untuk mendaftar dengan memasukkan nama dan NIM (nomor induk mahasiswa), yang berfungsi sebagai kata sandi.

3.Loop login
while True:
    print("silahkan login")
    nama = input("Nama: ")
    nim = getpass.getpass("NIM: ")
    
    if nama_1 == nama and nim_1 == nim:
        print("Anda berhasil login")
        break
    else:
        print("Nama atau password anda salah ")

Program memasuki loop di mana ia meminta pengguna untuk masuk dengan nama dan kata sandi (NIM). Jika nama dan kata sandi yang dimasukkan cocok dengan yang terdaftar, program mencetak pesan sukses dan keluar dari loop. Jika tidak, program memberi tahu pengguna bahwa ada kesalahan dan meminta mereka lagi.

4.Loop perhitungan diskon
while True:
    harga_barang = int(input("Harga Barang:RP.")) 
    jumlah_barang = int(input("Jumlah Barang: "))
    total_harga = jumlah_barang * harga_barang 
    
Setelah login berhasil, program masuk ke loop lain untuk menghitung diskon. Program meminta pengguna untuk memasukkan harga barang dan jumlahnya, kemudian menghitung total harga.

5.Logika diskon
if total_harga > 250000:
    diskon = 0.25 * total_harga 
    harga_setelah_diskon = total_harga - diskon
    print(f"RP.{harga_setelah_diskon}")
else:
    print(f"RP.{total_harga}")

Jika total harga melebihi 250.000, diskon sebesar 25% diterapkan. Program menghitung harga setelah diskon dan mencetaknya. Jika total harga 250.000 atau kurang, program hanya mencetak total harga.

6.Keluar dari progam
if input("Apakah anda ingin melanjutkan perhitungan? (iya/tidak): ") != "iya":
    print("Terima kasih, anda berhasil keluar dari program perhitungan")
    break
Setelah menampilkan harga (dengan atau tanpa diskon), program menanyakan kepada pengguna apakah mereka ingin melanjutkan. Jika pengguna menjawab dengan selain "iya", program mengucapkan terima kasih dan keluar.






