# persentase umur
n = int(input())
l = list(map(int, input().split()))

l.sort()
l_key = list(dict.fromkeys(l))
for i in l_key:
    percent = l.count(i) / n
    print(i, "%.2f" % percent)