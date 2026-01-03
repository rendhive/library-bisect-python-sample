import bisect

sorted_list = [1, 2, 3, 4, 5, 6]
position = bisect.bisect(sorted_list, 4)

if position > 0 and sorted_list[position - 1] == 4:
    print("Elemen 4 ditemukan di posisi:", position - 1)
else:
    print("Elemen 4 tidak ditemukan.")
# Fungsi: Mencari elemen dalam daftar terurut.
# Kondisi: Ketika Anda ingin mengetahui apakah elemen tertentu ada dalam daftar terurut.
