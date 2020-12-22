# kamus sederhana
ganti = {
    'aku': 'I',
    'saya': 'I',
    'kamu': 'you',
    'dia': 'he',
    'mereka': 'they',
    'kita': 'we',
    'kami': 'we'
}

teks = list(input().split())
for i in range(len(teks)):
    if teks[i] in ganti:
        teks[i] = ganti[teks[i]]
    if i == len(teks)-1:
        print(teks[i])
    else:
        print(teks[i], end=' ')
# print(' '.join([str(elem) for elem in teks]))