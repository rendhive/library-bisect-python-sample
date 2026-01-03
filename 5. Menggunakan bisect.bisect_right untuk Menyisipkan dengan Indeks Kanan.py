import bisect

# Daftar terurut
sorted_list = [1, 3, 3, 7, 9]

# Mencari posisi untuk elemen 3 menggunakan bisect_right
index = bisect.bisect_right(sorted_list, 3)

print("Posisi kanan untuk elemen 3 berada di indeks:", index)
# Fungsi: Menemukan posisi kanan tempat elemen dapat disisipkan.
# Kondisi: Ketika Anda ingin menemukan indeks tertinggi untuk elemen yang bersamaan.
