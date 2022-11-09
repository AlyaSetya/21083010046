# IMPORT BUILT-IN LIBRARY
from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

# INISIALISASI FUNCTION
def cetak(i):
    if (i+1)%2==0:
       print(i+1, "Genap - ID proses", getpid())
       sleep(1)
    else:
       print(i+1, "Ganjil - ID proses", getpid())
       sleep(1)

# INPUT NILAI
n = int(input("Masukkan Range Angka : "))

# SEKUENSIAL
print("Sekuensial")

sekuensial_awal = time()

for i in range(n):
    cetak(i)

sekuensial_akhir = time()

# MULTIPROCESSING -> PROCESS
print("Multiprocessing.Process")

kumpulan_proses = []

proses_awal = time()

for i in range(n):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()

for i in kumpulan_proses
    p.join()

proses_akhir = time()

# MULTIPROCESSING -> POOL
print("Multiprocessing.Pool")

pool_awal = time()

pool = Pool()
pool.map(cetak, range (0,n))
pool.close

pool_akhir = time()

# PERBANDINGAN WAKTU EKSEKUSI
print("Waktu eksekusi Sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi Multiprocessing.Process :", proses_akhir - proses_awal, "detik")
print("Waktu eksekusi Multiprocessing.Pool :", pool_akhir - pool_awal, "detik")

