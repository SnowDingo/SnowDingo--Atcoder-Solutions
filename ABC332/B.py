# -*- coding: utf-8 -*-
K, G, M = map(int,input().split())
KG = [0,0]
for i in range (0,K):
    if KG[0] == G:
        KG[0] = 0
    elif KG[1] == 0:
        KG[1] = M
    else:
        while True:
            if KG[1] == 0:
                break
            if KG[0] == G:
                break
            KG[1] = KG[1] -1
            KG[0] = KG[0] + 1
print(str(KG[0]) + " "+ str(KG[1]))