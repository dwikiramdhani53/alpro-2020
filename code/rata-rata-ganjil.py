# Menghitung Rata-Rata Ganjil
a, b = map(int, input().split())

jumlah = 0
count = 0
for i in range(a, b+1):
    if(i%2 == 0):
        continue
    count += 1
    jumlah += i

print(int(jumlah/count))