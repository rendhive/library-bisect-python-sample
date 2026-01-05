import bisect

sorted_list = [2, 4, 6, 8, 10]
insert_value = 7

index = bisect.bisect_left(sorted_list, insert_value)

print("Indeks untuk menyisipkan nilai 7:", index)
# Fungsi: Menentukan indeks yang tepat untuk menyisipkan nilai baru.
# Kondisi: Ketika Anda ingin menemukan lokasi penyisipan tanpa benar-benar menyisipkannya.
