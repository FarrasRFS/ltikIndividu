# Contoh Function
# def penjumlahan(a, b):
#     hasil = a + b
#     return hasil

# penjumlahan(2, 3)

# Contoh Procedure
# def greeting(nama):
#     print(f"Halo, {nama}!")

# greeting("Sasa")

def volumeBalok (p, l, t):
    volume = p * l * t
    return volume
print(volumeBalok(10, 5, 10))

# Keyword Arguments
def pengurangan(a, b):
    print(f"Hasilnya adalah {a - b}")

# menggunakan keyword arguments
pengurangan(b = 2, a = 5)

# tanpa keyword arguments
pengurangan(2, 5)
