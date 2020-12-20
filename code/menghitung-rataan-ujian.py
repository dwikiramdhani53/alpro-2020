# Menghitung rataan ujian
uts, uas, tugas = map(int, input().split())
na = ((uts + uas)*0.4 + tugas*0.2)
print("%.2f" % na)