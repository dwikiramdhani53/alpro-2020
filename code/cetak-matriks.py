# cetak matriks
baris, kolom = map(int, input().split())
isi = list(map(int, input().split()))
 
for i in range(baris):
    for j in range(kolom):
        if(j==kolom-1):
            print(isi[kolom*i + j])
        else:
            print(isi[kolom*i + j], end=' ')