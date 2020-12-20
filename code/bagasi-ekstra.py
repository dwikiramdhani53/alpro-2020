# Bagasi Ekstra
import math

n = int(input())
beratKoper = list(map(float, input().split()))
batas = int(input())
biayaEkstra = int(input())

totalBerat = sum(beratKoper)
if(totalBerat > batas):
    ekstra = totalBerat - batas
    biaya = biayaEkstra * math.ceil(ekstra)
    print('bagasi ekstra %.1f kg, biaya ekstra %d rupiah' % (ekstra, biaya))
else:
    print('tidak ada bagasi ekstra')