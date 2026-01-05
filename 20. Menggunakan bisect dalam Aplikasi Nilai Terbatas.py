import bisect

grades = [92, 85, 75, 60]

new_grade = 80
bisect.insort(grades, new_grade)

print("Daftar nilai setelah menyisipkan nilai baru:", grades)
# Fungsi: Mengelola nilai siswa dalam urutan.
# Kondisi: Ketika Anda perlu memasukkan nilai baru tanpa mengubah urutan.
