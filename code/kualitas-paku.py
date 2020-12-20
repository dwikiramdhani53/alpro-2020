# kualitas paku
from math import ceil

n = int(input())
panjang_paku = list(map(float, input().split()))
bawah, atas = map(float, input().split())
biaya = int(input())

memenuhi = 0
tidak_memenuhi = 0
for x in panjang_paku:
    if bawah <= x <= atas:
        memenuhi += 1
    else:
        tidak_memenuhi += ceil(x)

if tidak_memenuhi:
    print("%d%% paku memenuhi standar, kerugian %d rupiah" % (round(memenuhi/n * 100), tidak_memenuhi * biaya))
else:
    print("100% paku memenuhi standar")
