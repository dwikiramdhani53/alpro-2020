# Menghitung Deret Bilangan
n = int(input())
bil = list(map(int, input().split()))

jumlah = 0
for i in range(n):
    jumlah += bil[i]
print(jumlah)