# nilai lulus
uts, uas, up, tugas = map(float, input().split())
na = (uts + uas)*0.35 + up*0.25 + tugas*0.05
if(na < 40):
	print("TIDAK LULUS")
else:
	print("LULUS")