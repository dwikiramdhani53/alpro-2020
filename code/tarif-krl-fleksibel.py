# Tarif KRL Fleksibel
MIN, K, S, MAKS = map(int, input().split())
N = int(input())

tarif = MIN
if(N > K):
    add = (N-K)*S
    tarif += add
if(tarif > MAKS):
    tarif = MAKS
print(tarif)