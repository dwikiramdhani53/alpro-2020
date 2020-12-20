# ganti huruf
kata = input()
depan = kata[0]
belakang = kata[1:]

print(depan + belakang.replace(depan, '_'))