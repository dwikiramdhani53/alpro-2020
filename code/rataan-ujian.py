# Menghitung rataan ujian (Fungsi)
def rataanUjian(uts, uas, tugas):
    na = (uts + uas)* 0.4 + tugas*0.2
    return na

n_uts, n_uas, n_tugas = map(int, input().split())
print("%.2f" % rataanUjian(n_uts, n_uas, n_tugas))