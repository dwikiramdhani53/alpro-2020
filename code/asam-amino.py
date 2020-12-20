# asam amino
kode_asam_amino = {
    'Ala':'A',
    'Arg':'R',
    'Asn':'N',
    'Asp':'D',
    'Cys':'C',
    'Glu':'E',
    'Gln':'Q',
    'Gly':'G',
    'His':'H',
    'Ile':'I',
    'Leu':'L',
    'Lys':'K',
    'Met':'M',
    'Phe':'F',
    'Pro':'P',
    'Ser':'S',
    'Thr':'T',
    'Trp':'W',
    'Tyr':'Y',
    'Val':'V',
}

s = input().split('-')
for k in s:
    print(kode_asam_amino.get(k), end='')
print()