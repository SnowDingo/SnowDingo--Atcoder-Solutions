# -*- coding: utf-8 -*-
import math
N, L, R = map(int,input().split())
As = list(input().split())
for i in range(0,len(As)):
    As[i] = int(As[i])
Answer = []
i = 0
if L >= As[0]:
    Xi = L
else:
    Xi = As[0]
y = Xi + 1
while L<=Xi<=y<=R:
    if abs(Xi - As[0]) <= abs(y - As[0]):
        Answer.append(abs(Xi-As[i]))
    Xi +=1
    y += 1
print(Answer)