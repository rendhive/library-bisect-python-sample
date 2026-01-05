import bisect

inventory = [10, 20, 30, 40]

def add_stock(new_stock):
    bisect.insort(inventory, new_stock)

add_stock(25)

print("Inventaris setelah menambahkan stok baru:", inventory)
# Fungsi: Mengelola inventaris barang dengan menambahkan stok baru.
# Kondisi: Ketika Anda perlu menjaga inventaris terurut secara otomatis.
