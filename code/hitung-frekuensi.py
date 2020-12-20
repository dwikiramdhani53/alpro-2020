# Hitung frekuensi
s = input().lower()
s_key = list(dict.fromkeys(s))
s_key.sort()
for k in s_key:
    if k.isalpha():
        c = s.count(k)
        print(k + ':', c)