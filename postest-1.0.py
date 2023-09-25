#Dibuat oleh Noor Lintang Bhaskara (2309116030) Sistem Informasi A'23
print("Tugas Postest #1")
def login():
    nama = input("Masukan nama : ")
    nim = input("Masukan nim : ")
    password    = input("masukan password : ") 
    
    if nama == "Lintang" and nim == "2309116030" and password == "inforsa": 
        print("Berhasil Login! ")
    else:
        print("Login gagal, Silahkan cek ulang kembali!")
login()

print("===========================================================")
print("Program menghitung volume bangun ruang")
print("1. Bola")
print("2. Tabung")
print("3. Limas Segitiga")

operasi  =float(input("masukan operasi sisi (1/2/3): "))

import math
if operasi == 1:

    print("Operasi mencari volume bola")
    r = int(input("jari jari = "))
    v = 4/3
    volume = 4/3*22/7*r*r*r
    print("hasilnya adalah = ", volume)

elif operasi == 2:

    print("Operasi mencari volume tabung")
    phi = 3.14
    r = int(input("masukkan jari jari = "))
    t = int(input("masukkan tinggi = "))
    hasil = phi*r*r*t

    print("jumlah volume tabung", hasil)

elif operasi == 3:

    print("Operasi mencari volume Limas Segitiga")
    luas_alas = float(input("Masukkan Luas Alas: "))
    tinggi = float(input("Masukkan Tinggi Limas: "))
    sisi = float(input("Masukkan Sisi Limas: "))

    volume = 1/3 * luas_alas * tinggi * sisi
    print ("Volume Limas adalah %d" %volume)
else:
    print("Operasi tidak tersedia")
    