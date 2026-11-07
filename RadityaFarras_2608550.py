# NAMA : Raditya Farras Sudrajat
# NIM  : 2608550

# Latihan - 1
# 1. Deret Fibonacci dengan menggunakan fungsi.
def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

jumlah = int(input("Masukkan jumlah deret Fibonacci : "))
fibonacci(jumlah)

# 2. Menghitung volume tabung yang dibuat dalam sebuah fungsi.
def volumeTabung(r, t):
    return 3.14 * r * r * t

r = float(input("Masukkan jari jari : "))
t = float(input("Masukkan tinggi : "))

volume = volumeTabung(r, t)
print("Volume tabung =", volume)

# 3. Menghitung fungsi nilai total dan nilai rata-ratanya berdasarkan nilai 
#    yang diinputkan dari nilai total dimana banyaknya angka tidak dideklarasikan.
def hitungNilai(angka):
    total = sum(angka)
    rata_rata = total / len(angka)

    print("Total =", total)
    print("Rata-rata =", rata_rata)

data = input("Masukkan angka : ")
angka = list(map(int, data.split(",")))

hitungNilai(angka)

# Latihan - 2
# Membuat sebuah menu login yang dapat memberi kesempatan user untuk 
# memasukkan password kembali ketika dia salah sebanyak 3 kali.
usernameBenar = "Daspro2023"
passwordBenar = "Latihan"

kesempatan = 3

while kesempatan > 0:
    password = input("Masukkan password : ")

    if password == passwordBenar:
        print("Login berhasil!")
        break
    else:
        kesempatan -= 1
        print("Password salah!")

        if kesempatan > 0:
            print("Sisa kesempatan :", kesempatan)
        else:
            print("Keluar dari menu login.")
    
# Latihan - 3
# Aira diminta guru Olahraganya untuk menghitung waktu teman-temannya 
# mulai berlari dan selesai berlari. 
def hitungSelisih(jam1, menit1, detik1, jam2, menit2, detik2):
    mulai = jam1 * 3600 + menit1 * 60 + detik1
    selesai = jam2 * 3600 + menit2 * 60 + detik2

    selisih = selesai - mulai

    jam = selisih // 3600
    menit = (selisih % 3600) // 60
    detik = selisih % 60

    print("Hasil:", jam, "jam -", menit, "menit -", detik, "detik")


print("Input mulai :")
jam1 = int(input("Jam : "))
menit1 = int(input("Menit : "))
detik1 = int(input("Detik : "))

print("\nInput selesai :")
jam2 = int(input("Jam : "))
menit2 = int(input("Menit : "))
detik2 = int(input("Detik : "))

hitungSelisih(jam1, menit1, detik1, jam2, menit2, detik2)