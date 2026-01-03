import bisect
import random

# Membuat daftar terurut dari angka acak
random_list = random.sample(range(0, 100), 10)
sorted_list = []

for number in random_list:
    bisect.insort(sorted_list, number)

print("Daftar terurut dari angka acak:", sorted_list)
# Fungsi: Mengurutkan daftar angka acak secara manual menggunakan bisect.
# Kondisi: Ketika Anda memiliki data yang tidak terurut dan perlu mengurutkannya sambil menambahkannya.
