import bisect

sorted_list = [20, 40, 60, 80]
print("Sebelum penyisipan:", sorted_list)

bisect.insort(sorted_list, 50)
print("Setelah menyisipkan 50:", sorted_list)
# Fungsi: Menyisipkan elemen di lokasi yang tepat dalam daftar terurut.
# Kondisi: Ketika Anda perlu menjaga urutan data saat menyisipkan elemen baru.
