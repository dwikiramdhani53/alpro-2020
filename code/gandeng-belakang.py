# gandeng belakang
n = int(input())
minLen = 999
kata = []
for i in range(n):
    kata_input = input()
    if len(kata_input) < minLen:
        minLen = len(kata_input)
    kata.append(kata_input)

for k in kata:
    print(k[len(k)-minLen:], end='')
print()