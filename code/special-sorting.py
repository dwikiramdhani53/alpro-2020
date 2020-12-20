# Special Sorting
def sort_descending(source):
    for i in range(len(source)):
        max = i
        for j in range(i, len(source)):
            if(source[j] > source[max]):
                max = j
        temp = source[i]
        source[i] = source[max]
        source[max] = temp
    
    return source

def special_sort(source):
    genap = list()
    ganjil = list()
    for i in source:
        if(i%2 == 0):
            genap.append(i)
        else:
            ganjil.append(i)
    genap = sort_descending(genap)
    ganjil = sort_descending(ganjil)
    return genap + ganjil

n = int(input())
l = list(map(int, input().split()))

if(n != len(l)):
    print("Data tidak sesuai")
else:
    hasil = special_sort(l)
    for i in range(len(hasil)):
        print(hasil[i], end=" ")