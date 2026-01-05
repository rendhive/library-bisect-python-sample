import bisect

# Daftar tuple dengan elemen terurut berdasarkan elemen pertama
sorted_tuples = [(1, 'A'), (3, 'B'), (5, 'C')]
new_tuple = (4, 'D')

# Menyisipkan tuple di tempat yang sesuai
bisect.insort(sorted_tuples, new_tuple)

print("Daftar tuple setelah penyisipan:", sorted_tuples)
# Fungsi: Menyisipkan tuple dalam daftar yang sudah terurut.
# Kondisi: Ketika Anda bekerja dengan tuple dan perlu menjaga urutan.
