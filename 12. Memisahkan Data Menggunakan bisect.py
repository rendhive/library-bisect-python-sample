import bisect

# Data tidak terurut
data = [1, 3, 5, 7, 9]

# Memisahkan data berdasarkan kriteria
cut_off = 5
index = bisect.bisect(data, cut_off)

smaller_than_cut = data[:index]
greater_than_cut = data[index:]

print("Data lebih kecil dari 5:", smaller_than_cut)
print("Data lebih besar atau sama dengan 5:", greater_than_cut)
# Fungsi: Memisahkan data berdasarkan nilai potongan.
# Kondisi: Ketika Anda perlu membagi daftar terurut menjadi dua bagian.
