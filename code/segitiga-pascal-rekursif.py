# segitiga pascal rekursif - (masih blm acc)
def binom(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binom(n-1, k-1) + binom(n-1, k)

n = int(input())
for i in range(n):
    print("  "*(n-i-1), end='')
    for j in range(i+1):
        if j == i:
            print("%4u" % binom(i, j))
        else:
            print("%4u" % binom(i, j), end=' ')