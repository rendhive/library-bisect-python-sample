import bisect

data = [1, 2, 3, 4, 5, 6, 7, 8]
cut_off = 4

index = bisect.bisect(data, cut_off)

lower_half = data[:index]
upper_half = data[index:]

print("Setengah bawah:", lower_half)
print("Setengah atas:", upper_half)
# Fungsi: Mempisahkan list terurut menjadi dua bagian berdasarkan batas.
# Kondisi: Ketika Anda perlu membagi data berdasarkan titik potong.
