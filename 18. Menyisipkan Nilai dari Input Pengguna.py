import bisect

sorted_list = []

while True:
    value = input("Masukkan angka (atau 'exit' untuk keluar): ")
    if value.lower() == 'exit':
        break
    number = int(value)
    bisect.insort(sorted_list, number)

print("Daftar terurut akhir:", sorted_list)
# Fungsi: Menggunakan input pengguna untuk membangun daftar terurut.
# Kondisi: Ketika Anda ingin menerima data dari pengguna dan menyimpannya dalam urutan.
