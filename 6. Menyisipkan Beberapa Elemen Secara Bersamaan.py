import bisect

sorted_list = [1, 2, 4, 5]

# Elemen yang akan disisipkan
elements_to_insert = [3, 6, 7]

for element in elements_to_insert:
    bisect.insort(sorted_list, element)

print("Daftar setelah menyisipkan beberapa elemen:", sorted_list)
# Fungsi: Menyisipkan beberapa elemen ke dalam daftar terurut satu per satu.
# Kondisi: Ketika Anda ingin menambahkan beberapa elemen ke dalam daftar sekaligus.
