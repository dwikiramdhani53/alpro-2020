# matriks diagonal
n = int(input())
dt = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if i == j:
            if j == n-1:
                print(dt[i])
            else:
                print(dt[i], end=' ')
        else:
            if j == n-1:
                print('0')
            else:
                print('0', end=' ')