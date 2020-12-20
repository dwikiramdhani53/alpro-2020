# Akar Persamaan Kuadrat
import math
a, b, c = map(int, input().split())
d = b*b - 4*a*c
if(d < 0):
	print("Tidak memiliki akar real.")
else:
	x1 = (-b + math.sqrt(d))/(2*a)
	x2 = (-b - math.sqrt(d))/(2*a)
	print("%g %g" % (x1, x2))