# -*- coding: utf-8 -*-
N = int(input())
As = list(input().split())
for i in range(0,len(As)):
    As[i] = int(As[i])
maxnum = max(As)
As = [item for item in As if item != maxnum]
for i in range(0,len(As)):
    As[i] = int(As[i])
print(max(As))