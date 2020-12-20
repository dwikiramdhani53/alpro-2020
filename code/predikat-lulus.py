# Predikat lulus
ipk = float(input())
ls = int(input())
C = int(input())
D = int(input())
ulang = input()
sanksi = input()

if(ipk > 3.5):
    if(ls <= 60 and C <= 1 and D == 0 and ulang == 'N' and sanksi == 'N'):
        print("Cum Laude")
    elif(D == 0 and sanksi == 'N'):
        print("Sangat Memuaskan")
    else:
        print("Memuaskan")
elif(ipk > 2.75):
    if(ls <= 60 and D == 0 and sanksi == 'N'):
        print("Sangat Memuaskan")
    else:
        print("Memuaskan")
else:
	print("Memuaskan")