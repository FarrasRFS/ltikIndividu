# # Contoh Function
# # def penjumlahan(a, b):
# #     hasil = a + b
# #     return hasil

# # penjumlahan(2, 3)

# # Contoh Procedure
# # def greeting(nama):
# #     print(f"Halo, {nama}!")

# # greeting("Sasa")

# def volumeBalok (p, l, t):
#     volume = p * l * t
#     return volume
# print(volumeBalok(10, 5, 10))

# # Keyword Arguments
# def pengurangan(a, b):
#     print(f"Hasilnya adalah {a - b}")

# # menggunakan keyword arguments
# pengurangan(b = 2, a = 5)

# # tanpa keyword arguments
# pengurangan(2, 5)

# # Latihan - 3
# # Aira diminta guru Olahraganya untuk menghitung waktu teman-temannya 
# # mulai berlari dan selesai berlari. 
# def hitungSelisih(jam1, menit1, detik1, jam2, menit2, detik2):
#     mulai = jam1 * 3600 + menit1 * 60 + detik1
#     selesai = jam2 * 3600 + menit2 * 60 + detik2

#     selisih = selesai - mulai

#     jam = selisih // 3600
#     menit = (selisih % 3600) // 60
#     detik = selisih % 60

#     print("Hasil:", jam, "jam -", menit, "menit -", detik, "detik")


# print("Input mulai :")
# jam1 = int(input("Jam : "))
# menit1 = int(input("Menit : "))
# detik1 = int(input("Detik : "))

# print("\nInput selesai :")
# jam2 = int(input("Jam : "))
# menit2 = int(input("Menit : "))
# detik2 = int(input("Detik : "))

# hitungSelisih(jam1, menit1, detik1, jam2, menit2, detik2)