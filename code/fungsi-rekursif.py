# fungsi rekursif
def jumlahDigit(n):
    if n < 10:
        return n
    else:
        return n%10 + jumlahDigit(n//10)
n = int(input())
print(jumlahDigit(n))