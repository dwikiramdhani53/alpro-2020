# tarif parkir
waktu = int(input())
harga = 2000
if(waktu >= 60):
    add = int(waktu/60)*1000
    harga += add
if(harga > 8000):
    harga = 8000
print(harga)