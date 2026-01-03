import bisect

# Daftar terurut
sorted_list = [1, 3, 3, 7, 9]

# Mencari posisi untuk elemen 3 menggunakan bisect_left
index = bisect.bisect_left(sorted_list, 3)

print("Posisi kiri untuk elemen 3 berada di indeks:", index)
# Fungsi: Menemukan posisi kiri tempat elemen dapat disisipkan.
# Kondisi: Ketika Anda ingin menemukan indeks terendah untuk elemen yang bersamaan.
