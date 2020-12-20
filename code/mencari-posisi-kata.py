# mencari posisi kata
paragraf = input().lower()
kata = input().lower()

found = paragraf.find(kata) + 1
if found:
    print(found)
else:
    print("KATA TIDAK DITEMUKAN")