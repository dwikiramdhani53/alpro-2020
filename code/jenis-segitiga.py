# Jenis Segitiga
a, b, c = map(int, input().split())

if a == b == c :
    print("Segitiga sama-sisi", end='')
elif (a < 90 and b < 90 and c < 90):
    print("Segitiga lancip", end='')
    if (a == b or a == c or b == c):
        print(" sama-kaki", end='')
elif (a > 90 or b > 90 or c > 90):
    print("Segitiga tumpul", end='')
    if (a == b or a == c or b == c):
        print(" sama-kaki", end='')
elif (a == 90 or b == 90 or c == 90):
    print("Segitiga siku-siku", end='')
    if (a == b or a == c or b == c):
        print(" sama-kaki", end='')
print()