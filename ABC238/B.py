# -*- coding: utf-8 -*-
N = int(input())
As = list(map(int,input().split()))
max = 360
angle = 0
currentangles = []
for i in range(0,N):
    angle += As[i]
    currentangles.append(As[i])
print(currentangles)