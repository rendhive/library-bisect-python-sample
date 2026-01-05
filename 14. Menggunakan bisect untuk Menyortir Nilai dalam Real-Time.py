import bisect
import random

# Membuat daftar terurut dibalik
sorted_list = []

for _ in range(10):
    value = random.randint(1, 100)
    bisect.insort(sorted_list, value)

print("Daftar terurut secara real-time:", sorted_list)
# Fungsi: Menjaga daftar terurut saat menambahkan nilai acak secara langsung.
# Kondisi: Ketika Anda perlu mengurutkan data dengan pembaruan konstan.
