# -*- coding: utf-8 -*-
N, S, M, L = map(int,input().split())
money = []
for i in range(0,100):
    for x in range(0,100):
        for z in range(0,100):
            if z*12 + x * 8 + i * 6 >= N:
                money.append(z*L + x*M + S * i)
print(min(money))