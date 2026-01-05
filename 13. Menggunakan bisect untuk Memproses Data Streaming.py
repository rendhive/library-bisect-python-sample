import bisect

iterations = [10, 20, 30, 40]
sorted_data = []

for number in iterations:
    bisect.insort(sorted_data, number)

print("Data terurut:", sorted_data)
# Fungsi: Memproses dan menjaga data terurut dari pembaruan streaming.
# Kondisi: Ketika Anda mendapatkan data baru secara bertahap dan perlu menjaga urutan.
