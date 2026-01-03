import bisect

# Daftar terurut
sorted_list = [1, 3, 4, 7, 9]

# Menyisipkan elemen 5 ke dalam daftar terurut
bisect.insort(sorted_list, 5)

print("Daftar setelah penyisipan:", sorted_list)
# Fungsi: Menyisipkan elemen ke dalam daftar terurut secara otomatis.
# Kondisi: Ketika Anda ingin menjaga urutan daftar saat menambahkan elemen baru.
