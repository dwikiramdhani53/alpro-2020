# fungsi faktorial rekursif
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)
 
n = input()
n = int(n.replace('!', ''))
print(faktorial(n))