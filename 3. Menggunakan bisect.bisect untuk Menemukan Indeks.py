import bisect

# Daftar terurut
sorted_list = [1, 3, 4, 7, 9]

# Mencari posisi untuk elemen 5
index = bisect.bisect(sorted_list, 5)

print("Posisi elemen 5 seharusnya berada di indeks:", index)
# Fungsi: Menemukan indeks tempat elemen seharusnya berada dalam daftar terurut.
# Kondisi: Ketika Anda perlu mengetahui di mana elemen baru dapat disisipkan.
