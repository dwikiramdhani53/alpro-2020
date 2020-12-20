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
print(' '.join([str(elem) for elem in teks]))