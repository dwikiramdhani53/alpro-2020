# binsearch
def binsearch(source, bawah, atas, x):
    if(atas >= bawah):
        tengah = (atas + bawah) // 2

        if(source[tengah] == x):
            return tengah
        elif(source[tengah] > x):
            return binsearch(source, bawah, tengah-1, x)
        else:
            return binsearch(source, tengah+ 1, atas, x)
    else:
        return -1

n = int(input())
l = list(map(int, input().split()))
x = int(input())

print(binsearch(l, 0, n, x))