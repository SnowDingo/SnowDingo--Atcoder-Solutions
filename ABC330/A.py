# -*- coding: utf-8 -*-
N, L = map(int,input().split())
As = list(input().split())
for i in range(0,len(As)):
    As[i] = int(As[i])
count = 0
for i in range(0,len(As)):
    if As[i] >= L:
        count +=1
print(count)