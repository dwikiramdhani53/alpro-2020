# searching
def cari(x, source):
    for i in range(len(source)):
        if(source[i] == x):
            return i
    return -1

n = int(input())
l = list(map(int, input().split()))
x = int(input())

hasil = cari(x, l)
if(hasil == -1):
    print("Tidak Ada")
else :
    print("Ada")
print(hasil)