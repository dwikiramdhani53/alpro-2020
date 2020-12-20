# fibonacci kasus kecil
def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
 
n = int(input())
for i in range(n):
    a = int(input())
    print(f(a))