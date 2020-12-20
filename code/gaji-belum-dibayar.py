## gaji belum dibayar
s = input()
s_reverse = s[::-1].lower()
vocal = ['a', 'i', 'u', 'e', 'o']
for v in vocal:
    s_reverse = s_reverse.replace(v, '%')
print(s_reverse)