import bisect

priority_queue = []

# Menambahkan elemen dengan prioritas
def add_task(task, priority):
    bisect.insort(priority_queue, (priority, task))

add_task('Clean the house', 3)
add_task('Do the laundry', 1)
add_task('Prepare dinner', 2)

print("Tugas berdasarkan prioritas:")
while priority_queue:
    print(bisect.heappop(priority_queue)[1])
# Fungsi: Mengelola dan mengurutkan semua tugas berdasarkan prioritas.
# Kondisi: Ketika Anda perlu melacak dan menangani daftar tugas dengan prioritas.
