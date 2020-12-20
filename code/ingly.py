# ingly
kata = input()
panjang_kata = len(kata)

if panjang_kata < 3:
    print(kata)
else:
    if kata[-3:] == 'ing':
        print(kata + 'ly')
    else:
        print(kata + 'ing')