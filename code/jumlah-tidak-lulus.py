# jumlah tidak lulus
n = int(input())
nilai = list(map(int, input().split()))
batas = float(input())
dibawah = 0
for i in nilai:
    if i < batas:
        dibawah += 1
print("%d dari %d siswa tidak lulus, rataan kelas %.1f" % (dibawah, n, sum(nilai)/n))