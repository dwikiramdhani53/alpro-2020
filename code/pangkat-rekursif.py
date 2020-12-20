# pangkat rekursif
def pangkat(n, p):
    if p == 0:
        return 1
    elif p > 0:
        return n * pangkat(n, p-1)
    else:
        return 1/n * pangkat(n, p+1)

a, b = map(int, input().split())
print("%E" % pangkat(a, b))