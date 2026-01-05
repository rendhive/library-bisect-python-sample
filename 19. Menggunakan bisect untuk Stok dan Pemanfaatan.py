import bisect

stock_levels = [15, 25, 30, 45]

def adjust_stock(level):
    bisect.insort(stock_levels, level)

adjust_stock(20)

print("Tingkat stok saat ini:", stock_levels)
# Fungsi: Mengadaptasi dan menyesuaikan stok secara teratur.
# Kondisi: Ketika Anda perlu terus mengelola dan menyesuaikan stok.
